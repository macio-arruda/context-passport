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

Then:

- if there is one main topic, generate a focused Context Passport for it and put other topics in a section called "Parallel or out-of-scope topics";
- if there are multiple important topics, recommend which separate Context Passports should be generated and ask whether the user wants all of them or only one;
- if the user requested a specific topic, ignore the others and generate only that passport.

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
```
