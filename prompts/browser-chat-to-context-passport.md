# Prompt: Browser Chat To Context Passport

Use this prompt inside a browser AI chat when you want to turn the current conversation into a portable context pack.

```text
You are a context portability specialist. Convert this conversation into a Context Passport that another AI tool can use to continue the work without reading the full raw transcript.

Before generating the final document, check whether this conversation contains multiple unrelated topics.

If it does, first create a Topic Map with:

- each topic name;
- a one-sentence summary;
- the current status;
- whether it deserves a separate Context Passport;
- which topic appears to be the main one.

Then follow this decision rule:

- if there is one main topic, generate a focused Context Passport for it and put other topics in a section called "Parallel or out-of-scope topics";
- if there are multiple important topics and the user did not ask for one specific topic, stop after the Topic Map and ask which passport to generate first;
- if the user requested a specific topic, ignore the others and generate only that passport.

Do not mix unrelated topics into one Context Passport just to finish in one response.

Create a Markdown document with the following sections:

1. Title
2. Purpose of the passport
3. Original user goal
4. How the goal evolved
5. Chronology of important events
6. Confirmed facts
7. Decisions made
8. Rejected or deprioritized paths
9. Current status
10. Open questions
11. Risks and caveats
12. User preferences, tone, and working style
13. Relevant sources, files, links, and attachments
14. Terms and definitions
15. Next recommended actions
16. Resume prompt for another AI

Rules:

- Separate confirmed facts from assumptions.
- Keep unrelated topics separate. Do not mix decisions from one topic into another.
- Preserve names, dates, constraints, and decisions when they matter.
- Do not include secrets, credentials, tokens, private keys, or personal data unless absolutely required.
- If source files or attachments were discussed but are not available, say so explicitly.
- Make the output useful for both a human and a future AI agent.
- Be concise where possible, but do not omit operationally important context.

Delivery format:

- If this platform can create a downloadable file, prefer creating a file named `context-passport.md`.
- If a downloadable file is not possible, output the complete content directly in the chat inside one Markdown code block.
- Before the block, write: `Suggested file: context-passport.md`.
- Do not invent a download link. Only provide a link if the platform actually created the file.
- After the block, write one short instruction: `Copy the block above, save it as context-passport.md, or paste it directly into the next AI tool.`
```
