# Reviewer Connectivity Rule

User requirement: the human will not copy reviewer text between apps.

Therefore:

1. GitHub is the only accepted review transport for this project.
2. Each reviewer reads its frozen assignment/source packet from GitHub.
3. Each reviewer writes its raw result directly to its own GitHub issue/comment/authorized branch artifact.
4. The lead retrieves results from GitHub.
5. The human may open an app and issue a short pointer command such as "follow your Garden v15.10 assignment in GitHub issue #N"; the human does not relay the review body.
6. If an app cannot write to GitHub itself, its lane is BLOCKED_NO_REPO_WRITE.
7. The lead must not ask the human to copy/paste that model's output as a workaround.
8. A blocked app lane may later be enabled by a real connector or replaced only if the human explicitly changes the requested reviewer set.
9. OpenRouter output does not silently count as the named phone-app reviewer.
10. Reviewer identity/provider and return channel are recorded with the result.

This is a transport rule, not Garden semantic authority.
