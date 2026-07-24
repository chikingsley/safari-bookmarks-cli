# AGENTS.md

## Setup

- Install project dependencies with `uv sync --locked --dev`.
- Run the full local gate with `just check`.
- Run supply-chain checks with `just audit`.
- Install the local pre-push gate with `just install-hooks` when working in a clone.

## CI / Local Gates

- Treat `just check` and `just audit` as the source of truth for this repo's quality and supply-chain gate.
- GitHub-hosted Actions may be unavailable on this account; verify remote Actions with a live probe before relying on them.
- The local pre-push hook runs `just check` and `just audit`; bypass only for emergency pushes with `SKIP_LOCAL_CI=1`.

## Dependency Changes

- Treat new runtime dependencies and dependency upgrades as security-sensitive changes.
- Before changing dependencies, inspect the current state with `uv tree --outdated --locked`.
- Prefer targeted upgrades when fixing a vulnerability; use broad `uv lock --upgrade` only when the resulting diff stays reviewable.
- After dependency changes, run `just check` and `just audit`.
- Do not add new package indexes, direct URLs, Git dependencies, or install scripts unless the user explicitly asks and the risk is documented.

## Security Review Focus

- Preserve the MCP server's default write safety: writes require `dry_run=True` unless the server is started with `--confirm-write`, and `--readonly` must block writes.
- Be careful around `~/Library/Safari/Bookmarks.plist`; write paths should keep backups, use atomic replacement, and preserve existing file permissions.
- Review bookmark tree mutations for cycles, root deletion, malformed paths, and dry-run persistence bugs.
- Keep GitHub Actions least-privilege: explicit permissions, pinned third-party actions, no persisted checkout credentials, and no dependency caches in release or publish jobs.

## Review Guidelines

- For dependency bumps, check both behavior and supply-chain risk: lockfile diff, vulnerability audit, release notes for direct dependencies, and CI workflow changes.
- Prioritize bugs that can corrupt bookmarks, silently write to the real Safari plist, leak credentials, or weaken release/publish controls.
