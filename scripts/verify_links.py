import re
from pathlib import Path
import sys

def check_links(root_dir: Path):
    markdown_files = list(root_dir.rglob("*.md"))
    notebook_files = list(root_dir.rglob("*.ipynb"))
    
    all_files = markdown_files + notebook_files
    errors = []

    print(f"Checking {len(all_files)} files for broken links...")

    for file_path in all_files:
        try:
            content = file_path.read_text(encoding="utf-8")
        except Exception as e:
            # Notebooks might need special handling if we parse JSON, but simple text search works for links
            try:
                content = file_path.read_text(encoding="utf-8", errors="ignore")
            except:
                continue

        # Find all markdown links: [text](url)
        matches = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content)
        
        for text, url in matches:
            if url.startswith("http") or url.startswith("#") or url.startswith("mailto:"):
                continue
            
            # Handle relative links
            # Remove query params or anchors
            clean_url = url.split("#")[0].split("?")[0]
            if not clean_url:
                continue

            target_path = (file_path.parent / clean_url).resolve()
            
            if not target_path.exists():
                # Check if it's a path relative to repo root (sometimes used in Colab badges)
                repo_root_target = (root_dir / clean_url).resolve()
                if not repo_root_target.exists():
                     errors.append(f"Broken link in {file_path.relative_to(root_dir)}: {url} -> {target_path}")

    if errors:
        print("\nFound broken links:")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)
    else:
        print("\nAll local links verified successfully.")

if __name__ == "__main__":
    check_links(Path.cwd())
