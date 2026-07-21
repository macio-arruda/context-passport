# Prompt: Agent Session To Handoff

Use this prompt inside a coding agent session when you want another agent to continue the work.

```text
Create an Agent Handoff Kit for the current project/session.

Generate a Markdown handoff with:

1. Objective
2. Current working directory or project context
3. Current branch and repository state, if known
4. Files created, edited, or inspected
5. What has been completed
6. What is in progress
7. What remains pending
8. Key decisions and rationale
9. Rejected approaches
10. Important technical context
11. Commands or checks already run
12. Verification status
13. Known risks or blockers
14. Next actions in priority order
15. Resume prompt for the next agent

Also generate destination-specific variants when useful:

- CONTINUE.md for generic agent continuity
- AGENTS.md for Codex-style project instructions
- CLAUDE.md for Claude Code-style project memory

Rules:

- Do not invent file changes.
- Use absolute paths when referring to local files.
- Mark unknowns clearly.
- Separate user-made changes from agent-made changes when known.
- Include enough detail for a fresh agent to continue without rediscovery.
```

