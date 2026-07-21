# Prompt: Accessible Context To Context Passport

Use this prompt in a new AI chat or project when you want to create a Context Passport from the context this tool can already reference, instead of exporting one chat at a time.

This is useful when your work is spread across project chats, saved memories, previous conversations, uploaded files, or a long-running workspace.

Important: this is a best-effort accessible-context workflow. The AI must not claim that it searched or exported everything unless the platform actually provides that access. If access is limited, it should say what is missing and tell you how to gather the missing material.

Recommendation: select the strongest model or reasoning mode available before pasting this prompt.

```text
I want to create a Context Passport from the context that is accessible to you in this AI workspace, not only from this current chat.

Context Passport is a structured handoff document that lets me continue work in another AI tool without losing goals, decisions, constraints, pending questions, and current status.

First, do not generate the final passport yet.

Start by creating a Context Inventory.

Use only context you can genuinely reference in this workspace, such as:

- this current conversation;
- previous chats you are allowed to reference;
- project memory;
- project files;
- saved memories;
- instructions available in this workspace;
- any source material I paste or attach here.

Do not pretend you have searched every chat, project, file, or memory if you do not have that level of access.

Create a Context Inventory with these sections:

1. Scope I asked for
2. Context sources you can access or infer
3. Context sources you cannot access
4. Topic inventory
5. Confidence level for each topic
6. Important gaps or missing sources
7. Suggested manual search terms, if needed
8. Recommended Context Passports to generate
9. Which passport should be generated first and why

For each topic, include:

- topic name;
- one-sentence summary;
- likely source or location;
- current status;
- important decisions already known;
- open questions;
- whether it should become a separate Context Passport.

After the inventory, stop and ask me which passport I want to generate first.

If I already named a specific theme, generate the Context Inventory for that theme and then ask whether to proceed with the final passport.

When I approve a specific topic, generate a Markdown document with these sections:

1. Title
2. Purpose of the passport
3. Original user goal
4. How the goal evolved
5. Chronology of important events
6. Confirmed facts
7. Assumptions and uncertain points
8. Decisions made
9. Rejected or deprioritized paths
10. Current status
11. Open questions
12. Risks and caveats
13. User preferences, tone, and working style
14. Relevant sources, files, links, and attachments
15. Terms and definitions
16. Next recommended actions
17. Resume prompt for another AI

Rules:

- Separate confirmed facts from assumptions.
- Separate unrelated topics. Do not force multiple projects into one passport.
- Keep source limitations visible.
- Do not include secrets, credentials, tokens, private keys, or unnecessary personal data.
- If source files or attachments were mentioned but are not available, say so explicitly.
- Make the output useful for both a human and a future AI agent.

Delivery format:

- If this platform can create a downloadable file, prefer creating `context-inventory.md` for the inventory and `context-passport-[topic].md` for the final passport.
- If a downloadable file is not possible, output the complete content directly in the chat inside one Markdown code block.
- Do not invent a download link. Only provide a link if the platform actually created the file.
```
