# AI Safety and Freshness Gates

Use these in addition to the generic tutorial quality gates from `tutorialize-skill`.

## Safety gate

- [ ] Does the chapter say what the AI can see?
- [ ] Does it say what the AI may change?
- [ ] Does it prevent learners from pasting secrets, private data, unreleased research, or personal information?
- [ ] Does it explain permission prompts in human language?
- [ ] Does it require human confirmation before sending email, publishing, deleting, buying, or contacting other people?
- [ ] Does it use disposable/sample data for first exercises?
- [ ] Does it explain how to stop, undo, or narrow the task?

## Freshness gate

Record “as of YYYY-MM-DD” plus source/command for:

- install instructions;
- model/tool names;
- pricing, quota, and availability;
- UI screenshots and labels;
- CLI flags and default permissions;
- API key setup;
- SMTP provider requirements;
- third-party agent tools.

Prefer official docs or direct command output. If official docs are unavailable, label the claim as field-tested and include the test date.

## AI-specific anti-patterns

- Starting with API configuration before the learner sees value.
- Teaching automation before permissions and rollback.
- Letting the AI send messages without human review.
- Presenting model behavior as stable forever.
- Using secret-looking placeholders that learners may copy literally.
- Showing impressive demos with no verification path.
- Treating polished prose as correctness evidence.
