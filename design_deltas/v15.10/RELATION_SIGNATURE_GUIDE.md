# GCSC Relation Signature — Candidate Guide

[JSON candidate](GCSC_RELATION_SIGNATURE_CANDIDATE.json) defines source/target object classes and modes for 24 Core Relations to support **bounded semantic plausibility screening** in GCSC. It is not a change to the Core Relation registry.

GCSC can use these proposed signatures to generate typed relation motifs. SAL must still determine semantic admissibility using contextual, Form, facet and authority constraints; matching a broad source/target pair is not sufficient for admission. SAC may derive candidate artifacts only from qualified uncovered obligations; no generation step creates authority.

**Known unresolved issue:** `PROCESS_PLACEHOLDER` appears in the `controls` target list but is not a Core Object. The JSON explicitly flags its removal or proper modeling before admission. Binary `delegates` also does not encode full delegation scope; compatibility predicates and further context are required for several relations.

**Status:** candidate for adversarial review, not verified or canonical.
