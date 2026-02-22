# safari-bookmarks-mcp

Manage Safari bookmarks through an MCP server or CLI.

Built on [safari-bookmarks-cli](https://github.com/evilmarty/safari-bookmarks-cli) by Marty (evilmarty), extended with MCP support and modern tooling. Apache 2.0.

> **macOS note:** 10.14+ requires Full Disk Access for the terminal app you're running from.

## MCP server

Add to your client config — `uvx` handles installation automatically:

**`.mcp.json`** (Claude Code, project scope):
```json
{
  "mcpServers": {
    "safari-bookmarks": {
      "command": "uvx",
      "args": ["safari-bookmarks-mcp", "--file", "~/Library/Safari/Bookmarks.plist"]
    }
  }
}
```

Or use the bootstrap command to generate config for Claude Code, OpenCode, Codex, and Gemini:

```shell
uvx safari-bookmarks-mcp bootstrap --client claude --client opencode --scope local --write
```

Scopes: `local` (project-level), `global` (user-level), `both`.

**Server flags:**
- `--readonly` — block all write operations
- `--confirm-write` — allow writes (default requires `dry_run=True` per call)

**Tools:** `list_bookmarks`, `search_bookmarks`, `snapshot`, `add_bookmark`, `add_folder`, `move_item`, `remove_item`, `edit_item`, `empty_folder`. All write tools accept `dry_run=True` to preview changes without saving.

## CLI

```shell
uvx --from safari-bookmarks-mcp safari-bookmarks --help
```

```shell
safari-bookmarks list
safari-bookmarks list "BookmarksMenu"
safari-bookmarks add --title "Example" --url "http://example.com" "BookmarksMenu"
safari-bookmarks add --title "New Folder" --list "BookmarksBar"
safari-bookmarks move "BookmarksMenu" "Example" --to "BookmarksBar" "New Folder"
safari-bookmarks remove "BookmarksBar" "New Folder"
safari-bookmarks empty "BookmarksBar" "New Folder"
```

Default file: `~/Library/Safari/Bookmarks.plist`. Override with `-f <path>`.

## Development

```shell
git clone https://github.com/chikingsley/safari-bookmarks-mcp.git
just setup   # create .venv and install deps
just check   # ruff + ty + pytest
```
