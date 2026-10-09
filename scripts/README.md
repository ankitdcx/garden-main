# Manual repository integrity checks

Run locally, on demand, from the repository root:

```bash
python3 scripts/check_corpus.py
```

Uses Python standard library only. **Read-only:** no file modification, no GitHub Actions, no automation, no canonical promotion. Checks JSON parsing, relative Markdown paths, literal local paths in CORPUS_INDEX, five-file source manifest names/byte lengths/SHA-256 and current candidate pointer. Closed/unmerged historical-branch references are informational, not current-tree dependencies.

Exit 0 means the *structural checks implemented here* passed; it does **not** certify external URLs, arbitrary prose references, semantics, authority, tests, no-loss or admission. A nonzero exit reports integrity findings for manual review.
