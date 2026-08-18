# Parallel Task Lane

- task_id: `T000`
- actor_id: `<model-or-provider>-<session-short-id>`
- status: `TODO | IN_PROGRESS | PAUSED | AWAITING_USER_CONFIRMATION | BLOCKED | COMPLETED`
- branch: `<branch>`
- starting_head: `<commit>`
- owned_paths:
  - `<exact-file-or-narrow-directory>`
- resources:
  - `<task-metadata | git-index | build-resource | image-output | target-device | serial-port | flasher | ota-install>`
- stable_features: `<feature IDs and approval state, or none>`
- last_heartbeat: `<ISO-8601 timestamp>`
- next_action: `<next concrete action>`
- verification: `<checks and acceptance gates>`
- rollback: `<safe rollback boundary; user approval still required where applicable>`

