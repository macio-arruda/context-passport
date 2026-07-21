# Product Strategy

## Core thesis

AI memory is useful, but tool-specific memory creates lock-in. Professionals, students, researchers, and builders need a way to move context between AI environments without dragging an entire raw transcript or starting from scratch.

Context Passport is a lightweight standard and workflow for AI context portability.

## What already exists

Adjacent products and patterns include:

- chat exporters that save conversations as Markdown, JSON, PDF, or HTML;
- official memory import/export flows;
- coding-agent session management commands;
- `CONTINUE.md`-style project state files;
- MCP-based memory and context layers;
- browser extensions that bridge chats into local editors.

These are useful, but many focus on preserving raw content rather than creating an operational handoff.

## Differentiation

Context Passport focuses on curated continuity:

- not "save this chat";
- not only "summarize this chat";
- not only "import my memories";
- but "prepare another agent to continue this work correctly".

The package should preserve the reasoning trail that matters:

- goals;
- decisions;
- rejected paths;
- current status;
- responsibilities;
- risks;
- unresolved questions;
- next actions;
- source references;
- destination-specific instructions.

## Product 1: Context Passport

Audience:

- students;
- consultants;
- researchers;
- knowledge workers;
- people using AI primarily in browser chats.

Problem:

> "I cannot switch tools because my useful history is stuck in this chat."

Promise:

> Convert important AI conversations into portable context packs.

Primary artifacts:

- `context-passport.md`;
- `project-brief.md`;
- `decisions.md`;
- `open-questions.md`;
- `resume-prompt.md`.

Launch angle:

> You are not locked into one AI. You just need to carry your context properly.

## Product 2: Agent Handoff Kit

Audience:

- developers;
- data scientists;
- technical leads;
- product builders;
- people using Codex, Claude Code, Cursor, Windsurf, Gemini CLI, or other agents.

Problem:

> "My agent did a lot of work, but another agent has no idea what happened."

Promise:

> Generate a structured handoff so any agent can resume a technical project safely.

Primary artifacts:

- `handoff.md`;
- `CONTINUE.md`;
- `AGENTS.md`;
- `CLAUDE.md`;
- `agent_context.json`.

Launch angle:

> Switch agents without losing the thread.

## MVP scope

The first version should be deliberately simple:

- Markdown templates;
- prompts;
- one Codex skill;
- local validation script;
- optional redaction helper;
- examples with anonymized data.

No browser extension, scraping, authentication, or private API access in the first release.

## Future automation

Potential roadmap:

1. Parse ChatGPT and Claude exported JSON files.
2. Generate project-level passports from many conversations.
3. Add browser extension export button.
4. Add MCP server for live retrieval.
5. Add destination adapters for Codex, Claude Code, Cursor, and ChatGPT Projects.
6. Add sensitive-data detection.
7. Add diff-based handoff updates.

## Public content ideas

Article 1:

> You are not locked into one AI tool. You are missing a context passport.

Article 2:

> Agent Handoff: how to move work between Codex, Claude Code, and Cursor without starting over.

Article 3:

> Memory is not enough. Context portability is the next AI workflow skill.
