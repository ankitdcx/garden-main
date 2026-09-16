# Release-verification qualification

This package is bounded test evidence for the v15.7 working candidate. It does not establish production qualification, canonical admission, or promotion authority.

Install the exact assurance environment:

```bash
python -m venv /tmp/garden-assurance-venv
/tmp/garden-assurance-venv/bin/pip install -r requirements/assurance.txt
```

Run the focused tests and regenerate the receipts:

```bash
PYTHONPATH=implementation:implementation/tests /tmp/garden-assurance-venv/bin/python -m unittest implementation.tests.test_release_verification -v
PYTHONPATH=implementation:implementation/tests /tmp/garden-assurance-venv/bin/python scripts/qualify_release_verification.py
```

The ordinary core test environment may omit these upstream assurance packages; the focused test module then skips with an installation instruction. The qualification runner intentionally requires them and fails if they are absent.

The persistent TUF metadata cache is caller-owned and must be durably associated with exactly one authenticated repository identity. Reusing, discarding, or replacing it outside that binding can defeat rollback history. Receipts bind both the bootstrap root hash and the active trusted-root version/hash observed from that cache after refresh.

The signed rotation fixture demonstrates an authorized root transition that revokes old online role keys. It does not claim recovery from total root-key compromise. Such recovery requires a surviving independently authenticated trust anchor or explicit out-of-band procedure; there is no automatic trust reset.
