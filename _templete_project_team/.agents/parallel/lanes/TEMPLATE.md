# Parallel Role Task Lane

- task_id: `T000-ROLE`
- role_id: `PM | PO | AR | BE | FE | QA | OPS | AI`
- actor_id: `<role>-<tool-or-model>-<session-short-id>`
- status: `TODO | IN_PROGRESS | PAUSED | AWAITING_REVIEW | AWAITING_DEPLOY | AWAITING_TEST | AWAITING_USER_CONFIRMATION | BLOCKED | COMPLETED`
- stage: `P0 | P1 | P2 | P3 | P4 | P5 | P6 | P7`
- branch: `<branch>`
- starting_head: `<commit>`
- owned_paths:
  - `<exact-file-or-narrow-directory-within-role-OWNERS>`
- resources:
  - `<task-metadata | collab-board | git-index | backend-build | frontend-build | test-env | staging-env | ...>`
- upstream_handoffs: `<HO-xxx / API-xxx / TC-xxx required before starting>`
- output_artifacts: `<files and HO/IS/RV/CR numbers produced>`
- stable_features: `<feature IDs in _CHECKLISTS.md and approval state, or none>`
- last_heartbeat: `<ISO-8601 timestamp>`
- next_action: `<next concrete action>`
- verification: `<commands run and acceptance gates>`
- rollback: `<safe rollback boundary; human approval required where applicable>`
