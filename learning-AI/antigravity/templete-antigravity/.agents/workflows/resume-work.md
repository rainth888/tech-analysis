---
description: Resume work. Triggers: /resume-work
---

# /resume-work

## Steps

### 1. Read context
Read `HANDOFF.md` (required), `task.md`, `implementation_plan.md` (if exist).
If no HANDOFF.md → tell user, end workflow.

### 2. Show resume summary
```
🔄 Resume Summary
📋 Task: [description]
🕐 Interrupted: [time]
📊 Progress: X/Y
✅ Completed: [items]
▶️ Interrupted at: [work in progress]
📌 Next: [next step]

Continue from interrupt point? (Enter to continue, or give new instructions)
```

### 3. Resume
1. Update HANDOFF.md: status=in-progress, new conversation-id, save previous id
2. Continue from interrupt point
3. Follow task-management workflow