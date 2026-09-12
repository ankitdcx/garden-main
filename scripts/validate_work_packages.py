from pathlib import Path
import json, sys

required={"work_package_id","priority","title","gap_class","objective","required_outputs","acceptance","status","cmur_roles"}
seen=set()
ok=True
for p in sorted(Path("work_packages").glob("WP-*.json")):
    try:
        d=json.loads(p.read_text(encoding="utf-8"))
        missing=required-set(d)
        if missing:
            print(f"{p}: missing {sorted(missing)}"); ok=False; continue
        if d["work_package_id"] in seen:
            print(f"{p}: duplicate ID"); ok=False
        seen.add(d["work_package_id"])
        if d["gap_class"] not in {"DERIVATION","DESIGN","DISCOVERY","BLOCKED"}:
            print(f"{p}: invalid gap class"); ok=False
        print(f"{p}: OK")
    except Exception as e:
        print(f"{p}: ERROR {e}"); ok=False
sys.exit(0 if ok else 1)
