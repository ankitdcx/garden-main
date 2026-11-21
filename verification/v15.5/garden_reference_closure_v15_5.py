#!/usr/bin/env python3
from pathlib import Path
import re, json, hashlib, collections, sys

ROOT=Path(sys.argv[1]) if len(sys.argv)>1 else Path('.')
FILES=sorted(ROOT.glob('Garden_*_v15.5_FULL_2026-09-12.txt'))
ANN=next(p for p in FILES if 'Annexure' in p.name)
texts={p:p.read_text(encoding='utf-8').splitlines() for p in FILES}
ann_lines=texts[ANN]
results={}
unresolved=[]

# 1) Current semantic anchors [H-*]/[S-*]/[T-*]/[TH-*]/[RA-*]/[A-*].
anchor_pat=re.compile(r'\[((?:H|S|T|TH|RA|A)-[A-Z0-9][A-Z0-9._-]*)\]')
refs=collections.defaultdict(list); defs=collections.defaultdict(list)
for p,lines in texts.items():
    for i,l in enumerate(lines,1):
        for m in anchor_pat.finditer(l):
            token=m.group(1)
            # explicit negative declaration is not a normative reference
            if re.search(r'no\s+\['+re.escape(token)+r'\]\s+anchor\s+is\s+created',l,re.I):
                continue
            refs[token].append((p.name,i))
        for m in re.finditer(r'^\s*\[((?:H|S|T|TH|RA|A)-[A-Z0-9][A-Z0-9._-]*)\]',l): defs[m.group(1)].append((p.name,i))
        for m in re.finditer(r'SemanticAnchor\s*:\s*\[((?:H|S|T|TH|RA|A)-[A-Z0-9][A-Z0-9._-]*)\]',l): defs[m.group(1)].append((p.name,i))
missing=[x for x in refs if x not in defs]
results['semantic_anchors']={'referenced':len(refs),'defined':len(defs),'unresolved':missing}
unresolved += [('semantic_anchor',x) for x in missing]

# 2) Numeric Annexure references [A.NN].
numrefs=collections.defaultdict(list); numdefs=set()
for p,lines in texts.items():
    for i,l in enumerate(lines,1):
        for m in re.finditer(r'\[(A\.\d+)\]',l): numrefs[m.group(1)].append((p.name,i))
for i,l in enumerate(ann_lines,1):
    for m in re.finditer(r'(?:^\s*|@N\|)(A\.\d+)\b',l): numdefs.add(m.group(1))
missing=[x for x in numrefs if x not in numdefs]
results['numeric_annexure_refs']={'referenced':len(numrefs),'defined':len(numdefs),'unresolved':missing}
unresolved += [('numeric_annexure',x) for x in missing]

# 3) SchemaID references. Accepted definitions: @CAT rows, legacy @N/current schema rows, or explicit predecessor->current aliases.
schema_pat=re.compile(r'\b(SCHEMA-[A-Z0-9-]+)\b')
srefs=collections.defaultdict(list); sdefs=collections.defaultdict(list)
for p,lines in texts.items():
    for i,l in enumerate(lines,1):
        for x in schema_pat.findall(l): srefs[x].append((p.name,i))
for i,l in enumerate(ann_lines,1):
    for pat in [r'@CAT\|(SCHEMA-[A-Z0-9-]+)\|',r'@N\|(SCHEMA-[A-Z0-9-]+)\s+(?:FOUNDATIONAL_CONTRACT|GENERATED_[A-Z_]+)',r'^\s*(SCHEMA-[A-Z0-9-]+)\s+(?:FOUNDATIONAL_CONTRACT|GENERATED_[A-Z_]+)']:
        m=re.search(pat,l)
        if m:sdefs[m.group(1)].append(i)
    m=re.search(r'predecessor\s+(SCHEMA-[A-Z0-9-]+)\s+→\s+current\s+(SCHEMA-[A-Z0-9-]+)',l)
    if m:sdefs[m.group(1)].append(i)
missing=[x for x in srefs if x not in sdefs]
results['schema_ids']={'referenced':len(srefs),'resolved_identifiers':len(sdefs),'unresolved':missing}
unresolved += [('schema_id',x) for x in missing]

# 4) Registry references.
reg_pat=re.compile(r'\b(REG-[A-Z0-9][A-Z0-9-]*)\b')
rrefs=collections.defaultdict(list); rdefs=collections.defaultdict(list)
for p,lines in texts.items():
    for i,l in enumerate(lines,1):
        for x in reg_pat.findall(l): rrefs[x].append((p.name,i))
for i,l in enumerate(ann_lines,1):
    for m in re.finditer(r'(?:(?:^|@D\||@N\|)\s*)(REG-[A-Z0-9][A-Z0-9-]*)(?:\s+|\|)?(?:—|-|:|=)',l): rdefs[m.group(1)].append(i)
missing=[x for x in rrefs if x not in rdefs]
results['registries']={'referenced':len(rrefs),'defined':len(rdefs),'unresolved':missing}
unresolved += [('registry',x) for x in missing]

# 5) Invariant/test-like identifiers ending -NNN. Ownership syntax covers @D, @N registry/index rows,
#    legacy plain headings/tests, compact ranges, and explicit compatibility mappings.
idpat=re.compile(r'\b([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+-\d{3})\b')
owned=set()
for l in ann_lines:
    s=l.strip()
    m=re.match(r'@D\|([^|]+)\|',s)
    if m:
        for x in idpat.findall(m.group(1)): owned.add(x)
        tail=m.group(1).split('.')[-1]
        if idpat.fullmatch(tail): owned.add(tail)
    if s.startswith('@N|'):
        for x in idpat.findall(s): owned.add(x)
    m=re.match(r'(?:Policy\.)?([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+-\d{3})(?=\s|:|—|$)',s)
    if m: owned.add(m.group(1))
    if idpat.fullmatch(s): owned.add(s)
    for m3 in re.finditer(r'((?:[A-Z][A-Z0-9]*-)+)(\d{3})\.\.(\d{3})',l):
        pref=m3.group(1); a=int(m3.group(2)); b=int(m3.group(3))
        if b>=a and b-a<=500:
            owned.update(f'{pref}{n:03d}' for n in range(a,b+1))
    if ('→' in l or '->' in l) and (s.startswith('@N|') or 'predecessor' in l.lower() or '→' in l):
        for x in idpat.findall(l): owned.add(x)
irefs=collections.defaultdict(list)
for p,lines in texts.items():
    for i,l in enumerate(lines,1):
        for x in idpat.findall(l):
            if x.startswith(('SCHEMA-','REG-')): continue
            irefs[x].append((p.name,i,l))
missing=[]
for x,occ in irefs.items():
    if x in owned: continue
    # Legacy compact range alias e.g. CULT-001-003 on a line also containing CULT-001..003 is not a distinct ID.
    if all(('..' in row[2] and x.rsplit('-',1)[0] in row[2]) for row in occ): continue
    missing.append(x)
results['invariant_test_ids']={'referenced':len(irefs),'owned_or_mapped':len(owned),'unresolved':sorted(missing)}
unresolved += [('invariant_or_test',x) for x in missing]

# 6) @CAT identity/name integrity and duplicate human alias lint.
cat=[]
for i,l in enumerate(ann_lines,1):
    m=re.match(r'@CAT\|(SCHEMA-[^|]+)\|([^|]+)\|([^|]+)\|(.+)$',l)
    if m: cat.append((m.group(1),m.group(2),m.group(3),m.group(4),i))
byid=collections.defaultdict(list); byname=collections.defaultdict(list)
for row in cat:
    byid[row[0]].append(row); byname[row[2]].append(row)
id_name_conflicts={k:sorted(set(r[2] for r in v)) for k,v in byid.items() if len(set(r[2] for r in v))>1}
dup_names={k:v for k,v in byname.items() if len(v)>1}
# certified disambiguation table
qualified={}
in_dis=False
for l in ann_lines:
    if l.strip()=='CERTIFIED MACHINE QUALIFIED-NAME DISAMBIGUATION': in_dis=True; continue
    if in_dis:
        m=re.match(r'\s*(SCHEMA-[A-Z0-9-]+)\s+([A-Za-z0-9_.]+)\s*$',l)
        if m: qualified[m.group(1)]=m.group(2)
        elif qualified and l.startswith('All other human aliases'): break
unresolved_dup=[]
for name,rows in dup_names.items():
    ids=[r[0] for r in rows]
    if any(i not in qualified for i in ids) or len({qualified.get(i) for i in ids}) != len(ids): unresolved_dup.append(name)
results['catalogue_lint']={
    'cat_rows':len(cat),'unique_schema_ids':len(byid),'schema_id_to_multiple_names':id_name_conflicts,
    'duplicate_bare_names':len(dup_names),'duplicate_bare_names_unresolved':sorted(unresolved_dup),
    'qualified_disambiguation_entries':len(qualified)}
if id_name_conflicts: unresolved.append(('catalogue_schema_id_name_conflict',sorted(id_name_conflicts)))
if unresolved_dup: unresolved.append(('catalogue_duplicate_alias',sorted(unresolved_dup)))

# 7) Common release header consistency.
expected='GARDEN — FULL FIVE-FILE INTEGRATED DESIGN v15.5 — 2026-09-12'
headers={p.name:texts[p][0] if texts[p] else '' for p in FILES}
header_bad=[k for k,v in headers.items() if v!=expected]
results['headers']={'expected':expected,'files':headers,'mismatches':header_bad}
if header_bad: unresolved.append(('header',header_bad))

status='PASS' if not unresolved else 'FAIL'
out={
 'release_id':'Garden-v15.5-2026-09-12',
 'receipt_id':'RCR-GARDEN-v15.5-2026-09-12',
 'scanner_version':'garden_reference_closure_v15_5.py ruleset 1.0',
 'scan_boundary':'five current v15.5 UTF-8 source files; current normative anchors/SchemaIDs/registries/invariant-test IDs plus catalogue identity lint; external bibliographic URLs and historical non-current source files excluded',
 'document_hashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in FILES},
 'results':results,
 'unresolved_references':unresolved,
 'status':status,
 'provenance':'deterministic local structural scan; no semantic/behavioral/physical certification',
 'signature':None
}
print(json.dumps(out,indent=2,ensure_ascii=False))
