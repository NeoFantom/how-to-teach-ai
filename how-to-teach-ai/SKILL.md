---
name: how-to-teach-ai
description: Design, write, audit, and maintain beginner-friendly AI literacy and AI Agent tutorials by applying tutorialize-skill plus AI-specific teaching rules. Use when Codex needs to create an AI tutorial, teach ordinary people AI tools, split AI lessons for office/admin versus research audiences, explain AI Agent basics, plan install-and-first-task experiences, teach prompting/workflow/validation, cover AI safety/privacy/API keys/permissions, or freshness-check AI tool facts such as Codex, Claude Code, OpenAI APIs, SMTP, models, and CLI behavior.
---

# How to Teach AI

Use this skill **after or alongside `$tutorialize-skill`**. The general tutorial method lives there. This skill only adds AI/Agent-specific curriculum, sequencing, risk, and freshness rules.

## Credit and source of inspiration

This skill is inspired by a structured study of [`stormzhang/ai-coding-guide`](https://github.com/stormzhang/ai-coding-guide), with gratitude and explicit credit. It does **not** copy the original tutorial text, images, or chapter content. It applies the generalized `tutorialize-skill` method to AI education.

## Dependency contract

First use `tutorialize-skill` to establish:

- audience contract;
- curriculum ladder;
- chapter safe-loop template;
- Markdown/assets/source hygiene;
- pedagogy, factual, render, and reader-trial quality gates.

Then use this skill to specialize those gates for AI.

## AI teaching objective

Teach ordinary people to use AI agents for real work without mystifying them or pushing them into unsafe automation. The first success should come early; risky power should come later.

A good AI tutorial teaches:

```text
why AI Agent matters
→ what it is in human language
→ minimum computer/files/command-line literacy
→ accounts/network/API key concepts only when needed
→ install or open one usable tool
→ first safe task
→ how to read the agent interface and permission prompts
→ how to ask for work using plans and validation
→ office or research workflows
→ privacy, secrets, permissions, and human review
→ stronger automation only after risk literacy
```

## Audience split

Keep a shared foundation, then branch by real work.

### Ordinary office/admin track

Emphasize visible productivity and familiar artifacts:

- collecting and organizing invoices or reimbursement materials;
- cleaning spreadsheets and registration forms;
- summarizing project progress;
- drafting schedules and notices;
- writing and formatting emails;
- generating Word-style reports with validation-driven review.

### Researcher track

Start from the same basics but move faster into computer-only research work:

- literature notes and extraction;
- data cleaning and analysis;
- simulation or numerical scripts;
- plotting and figure checks;
- report drafting;
- reproducible workflows.

Boundary: do not teach equipment control, lab hardware operation, or any workflow where an agent can physically affect instruments unless a separate safety system exists.

## AI-specific sequencing rules

1. **Do not start with API keys or command lines.** Start with the learner's real task and explain why a technical step is necessary.
2. **Make the agent visible before making it abstract.** Let learners run or observe a small task before deep theory.
3. **Explain the interface as a cockpit.** Teach input area, plan/trace area, file changes, permission prompts, cancel/stop, and final summary.
4. **Teach files and folders early.** Many nontechnical learners fail because they do not know what material the agent can see.
5. **Teach permissions before automation.** Read/write access, shell commands, email sending, API calls, and external publication all need human-readable gates.
6. **Teach validation-driven work.** The learner should ask the agent to plan, act, verify, and show evidence instead of accepting polished text blindly.
7. **Keep humans in the final approval loop.** Emails, reports, public posts, data deletion, purchases, and messages to other people require human confirmation.

## AI-specific chapter requirements

Every AI chapter should include the generic tutorial loop plus:

- what the AI can and cannot see;
- what data should not be pasted or uploaded;
- what the learner must review manually;
- what success evidence the agent should provide;
- how to stop, undo, or narrow the task;
- which claims are version-sensitive and when they were checked.

Use `references/ai-curriculum-map.md` for a default curriculum and `references/ai-safety-and-freshness.md` for AI-specific review gates.

## AI facts and freshness

AI tools change quickly. Treat these as unstable until verified:

- model names, prices, quotas, and availability;
- install commands and CLI flags;
- Codex, Claude Code, OpenCode, OpenClaw, MIMOcode, Workybody, or similar tool behavior;
- OpenAI, Anthropic, Tencent, Xiaomi, or third-party API setup;
- permission defaults, sandbox modes, approval prompts;
- UI labels, screenshots, keyboard shortcuts;
- SMTP provider rules and email security requirements.

When the tutorial affects real tool usage, verify with official docs or actual local commands and write “截至 YYYY-MM-DD”. Use `scripts/ai_freshness_scan.py` to create a review queue.

## Suggested AI tutorial source layout

```text
tutorial/
├── README.md
├── basics/
│   ├── 01-what-is-ai-agent.md
│   ├── 02-files-and-folders.md
│   ├── 03-command-line-without-fear.md
│   ├── 04-accounts-network-api-keys.md
│   ├── 05-first-safe-agent-loop.md
│   └── assets/
├── office/
│   ├── 01-email.md
│   ├── 02-spreadsheet.md
│   ├── 03-invoices.md
│   ├── 04-event-registration.md
│   └── assets/
├── research/
│   ├── 01-literature-notes.md
│   ├── 02-data-analysis.md
│   ├── 03-simulation-script.md
│   ├── 04-report-and-figures.md
│   └── assets/
├── workflows/
│   ├── 01-how-to-ask.md
│   ├── 02-plan-execute-verify.md
│   ├── 03-validation-driven-reports.md
│   ├── 04-email-with-smtp.md
│   └── assets/
├── safety/
│   ├── 01-data-boundaries.md
│   ├── 02-permissions.md
│   ├── 03-secrets-and-api-keys.md
│   └── assets/
├── faq.md
├── glossary.md
└── anti-patterns.md
```

## Stop condition

An AI tutorial increment is ready only when:

- a beginner can complete one real AI-assisted task;
- the learner knows what the agent saw and changed;
- risky actions are gated by human approval;
- version-sensitive tool facts have dates and sources;
- the lesson passes the generic `tutorialize-skill` quality gates.
