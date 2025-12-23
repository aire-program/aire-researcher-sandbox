"""Verify internal markdown links in documentation files."""

from __future__ import annotations

import re
import sys
from pathlib import Path


def check_links(root_dir: Path) -> None:
    """Scan markdown and notebook files for broken internal links."""
    markdown_files = list(root_dir.rglob("*.md"))
    notebook_files = list(root_dir.rglob("*.ipynb"))
    all_files = markdown_files + notebook_files
    errors: list[str] = []

    print(f"Checking {len(all_files)} files for broken links...")

    for file_path in all_files:
        try:
            content = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            content = file_path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue

        matches = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content)

        for _text, url in matches:
            if url.startswith(("http", "#", "mailto:")):
                continue

            clean_url = url.split("#")[0].split("?")[0]
            if not clean_url:
                continue

            target_path = (file_path.parent / clean_url).resolve()
            if not target_path.exists():
                repo_root_target = (root_dir / clean_url).resolve()
                if not repo_root_target.exists():
                    errors.append(
                        f"Broken link in {file_path.relative_to(root_dir)}: "
                        f"{url} -> {target_path}"
                    )

    if errors:
        print("\nFound broken links:")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)
    else:
        print("\nAll local links verified successfully.")


if __name__ == "__main__":
    check_links(Path.cwd())
