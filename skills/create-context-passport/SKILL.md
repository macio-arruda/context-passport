---
name: create-context-passport
description: Create a portable AI context handoff pack from a long conversation, project thread, browser chat export, or coding-agent session. Use when the user wants to move work between ChatGPT, Claude, Codex, Cursor, Gemini, or another AI tool without losing decisions, status, risks, and next steps.
---

# Create Context Passport

Use this skill to convert messy AI history into a structured, portable context pack.

## Outputs

Create the smallest useful set of files for the user's destination:

- `context-passport.md` for browser-chat or project knowledge transfer.
- `agent-handoff.md` for coding-agent session transfer.
- `resume-prompt.md` for copy/paste continuation.
- `CONTINUE.md`, `AGENTS.md`, or `CLAUDE.md` when the destination benefits from project-level files.

## Workflow

1. Identify the source and destination.
   - Source examples: ChatGPT browser chat, Claude chat, exported Markdown, exported JSON, current Codex session, project notes.
   - Destination examples: ChatGPT, Claude, Codex, Claude Code, Cursor, Gemini, generic Markdown.

2. Extract operational context.
   - Original goal.
   - How the goal evolved.
   - Chronology.
   - Confirmed facts.
   - Assumptions.
   - Decisions and rationale.
   - Rejected or deprioritized paths.
   - Current status.
   - Risks and caveats.
   - Open questions.
   - Sources and attachments.
   - User preferences.
   - Next actions.

3. Choose the right template.
   - Browser/project migration: use `templates/context-passport.md`.
   - Agent/coding migration: use `templates/agent-handoff.md`.
   - Generic continuation: include `templates/resume-prompt.md`.

4. Write the files.
   - Prefer a `context-passport/` or `handoff/` folder inside the current project unless the user gives a path.
   - Use clear filenames with dates when creating multiple packs.
   - Do not include secrets, credentials, access tokens, private keys, or unnecessary personal data.

5. Validate the result.
   - The next AI can understand the task without the raw transcript.
   - Confirmed facts are separated from assumptions.
   - Open questions and next actions are explicit.
   - Missing sources are called out.
   - Sensitive data is removed or flagged.

## Quality bar

A good Context Passport is not a transcript summary. It is a rehydration artifact.

It should answer:

- What are we doing?
- Why are we doing it?
- What has already happened?
- What did we decide?
- What should not be repeated?
- What is still uncertain?
- What should the next agent do first?

