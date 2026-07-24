from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

import truststore
from pip_audit._cli import audit


def main() -> int:
    os.environ.setdefault("UV_SYSTEM_CERTS", "1")
    with tempfile.NamedTemporaryFile(prefix="safari-bookmarks-mcp-", suffix=".requirements.txt") as file:
        requirements_path = Path(file.name)
        subprocess.run(
            [
                "uv",
                "export",
                "--locked",
                "--format",
                "requirements.txt",
                "--no-emit-project",
                "--output-file",
                str(requirements_path),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
        )
        truststore.inject_into_ssl()
        sys.argv = [
            "pip-audit",
            "-r",
            str(requirements_path),
            "--disable-pip",
            "--no-deps",
            *sys.argv[1:],
        ]
        return audit()


if __name__ == "__main__":
    raise SystemExit(main())
