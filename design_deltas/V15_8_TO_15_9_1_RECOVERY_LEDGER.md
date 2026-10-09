# v15.8 → v15.9 → v15.9.1 delta recovery ledger

This folder set preserves **source-defined added clauses**, not the full five-file releases. None of the three candidates is promoted to canonical by these commits.

| Version | Recovered source content | Still unresolved |
|---|---|---|
| v15.8 | Five exact version-labelled additions: USER_ADDED_CLAUSES, SYSTEM_ADDED_CLAUSES, TECHNICAL_ADDED_CLAUSES, ANNEXURE_ADDED_CLAUSES, THEORIES_ADDED_CLAUSES. | A machine-computed semantic comparison against every v15.7 source, including any changes made inside inherited sections, has not been certified. |
| v15.9 | Exact 338-line P001–P037 consolidated review source, plus five original reviewed closure tails and detailed P037 corrective behavior. | The consolidation points to external packet evidence and UpgradeTraceabilityTable; exact accepted clause-by-clause deltas in P001–P036 cannot be proven complete without those frozen packet artifacts and a v15.8 comparison. The v15.9 documents are a documentation rewire, not purely appended patches. |
| v15.9.1 | Five exact GCSC additions from earlier source editions plus detailed GCSC/SAL/SAC semantic contracts. | The manifest-verified COMPLETE archive includes additional final suffixes not present in the earlier five-file editions. Its exact additional clauses have not been copied or independently verified here. |

**Rule for consumers:** A delta is not a full independent release; resolve inherited behavior through the predecessor and retain exact source status. No silent fallback from UNKNOWN to PASS. No self-admission. Do not use these files to assert complete no-loss migration until the remaining source-specific comparisons are finished.

**Source locations:** v15.8 combined master historical Library; v15.9 complete reviewed five-file Library sources and consolidated upgrade; v15.9.1 earlier five-file Library sources; TREE_CORE_v0.8.1 exact source binding.
