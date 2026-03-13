---
description: Save progress. Triggers: /save-progress
---

# /save-progress

## Steps

### 1. Finish to safe point
Ensure current edits are in compilable/runnable state.

### 2. Update HANDOFF.md
Set status=interrupted, record:
- task description, start/interrupt time, conversation-id chain
- completed / in-progress / pending items
- decisions, modified files
- current snapshot: file being edited, phase, next step, running services
- dependencies changed

### 3. Show summary
```
✅ Progress saved!
📋 Task: [description]
📊 Progress: X/Y completed
📝 Interrupted at: [current work]
📄 HANDOFF.md updated

🔄 To resume: /resume-work (in new chat)
```