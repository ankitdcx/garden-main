# Reviewer Connectivity Rule

User requirement:
- DeepSeek, Qwen and Gemini phone apps do not have direct GitHub read/write access.
- The human will not manually copy review text between apps.

Therefore the project uses two transport layers.

## Layer A — durable project state

GitHub remains the authoritative coordination/evidence store for the lead and any connected ChatGPT workers.

The lead stores:
- frozen review packets;
- source hashes;
- role assignments;
- finding ledger;
- coverage ledger;
- integrated candidate;
- reviewer receipts/results once returned;
- release-gate state.

## Layer B — external phone-model handoff

DeepSeek, Qwen and Gemini are external phone reviewers.

They do not need GitHub access.

The human is never asked to copy large review prompts or model answers.

Allowed minimum-effort handoff methods, in preference order:

1. FILE IN / FILE OUT
   - Lead generates one frozen UTF-8 .txt review packet per external reviewer.
   - Human uploads that file to the named model app.
   - The packet tells the model to return its result as a UTF-8 .txt file when the app supports file creation/export.
   - Human uploads the returned file to the Lead chat.
   - Lead hashes the exact returned bytes and stores the frozen result in GitHub.

2. FILE IN / PUBLIC SHARE LINK OUT
   - Human uploads the lead-generated frozen packet file to the model app.
   - Model completes the review.
   - Human creates the app's public/shareable conversation link and sends only that link to the Lead.
   - Lead retrieves the public result when technically accessible, freezes the exact retrieved content, hashes it, and stores it in GitHub.

3. FILE IN / APP SHARE-TO-CHAT
   - If the client supports sending the model result directly into ChatGPT as a file/share object without copy/paste, that is acceptable.
   - Lead freezes and hashes what was received.

Forbidden as the normal workflow:
- asking the human to copy/paste long review prompts;
- asking the human to copy/paste long reviewer answers;
- paraphrasing an external review before freezing it;
- pretending an app was repo-connected when it was not;
- silently substituting an OpenRouter model for the requested named phone-app reviewer.

If none of the allowed return methods is available for a model, its lane is:
    BLOCKED_NO_NONMANUAL_RETURN_PATH

A blocked reviewer does not count as completed.

## Blindness

Each external reviewer receives only:
- the frozen common source packet;
- its role-specific assignment.

It must not receive peer outputs before its result is frozen.

## Identity / evidence

For every external result the lead records:
- reviewer name;
- app/provider as stated by the user/app;
- packet hash;
- return method;
- raw-result hash;
- retrieval timestamp;
- whether peer exposure occurred before freeze.

External reviewers are evidence sources, not Garden authority.

This is a transport rule, not Garden semantic authority.
