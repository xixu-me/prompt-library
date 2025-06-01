#!/usr/bin/env python3
"""
Internal file link checker for the prompt library.
This script validates internal file links (relative paths) while ignoring external HTTP(S) links.
"""

import argparse
import re
import sys
from pathlib import Path


def find_markdown_files(root_path: Path) -> list[Path]:
    """Find all markdown files in the repository."""
    return list(root_path.rglob("*.md"))


def extract_internal_links(content: str, file_path: Path) -> list[tuple[str, int, str]]:
    """
    Extract internal file links from markdown content.
    Returns list of tuples: (link_text, line_number, link_target)
    """
    internal_links = []
    lines = content.split("\n")

    # Patterns for different markdown link formats
    patterns = [
        # [text](path) - standard markdown links
        r"\[([^\]]*)\]\(([^)]+)\)",
        # [text]: path - reference-style links
        r"^\s*\[([^\]]+)\]:\s*(.+)$",
    ]

    for line_num, line in enumerate(lines, 1):
        for pattern in patterns:
            matches = re.finditer(pattern, line, re.MULTILINE)
            for match in matches:
                link_text = match.group(1)
                link_target = match.group(2).strip()

                # Skip HTTP(S) links
                if link_target.startswith(("http://", "https://")):
                    continue

                # Skip mailto links
                if link_target.startswith("mailto:"):
                    continue

                # Skip fragment-only links (anchors within same page)
                if link_target.startswith("#"):
                    continue

                # Remove fragment part from file links
                clean_target = link_target.split("#")[0]

                # Skip empty targets
                if not clean_target:
                    continue

                internal_links.append((link_text, line_num, clean_target))

    return internal_links


def resolve_relative_path(source_file: Path, target_path: str) -> Path:
    """Resolve a relative path from the source file's directory."""
    source_dir = source_file.parent

    # Handle different path formats
    if target_path.startswith("./"):
        target_path = target_path[2:]
    elif target_path.startswith("../"):
        # Keep the ../ for proper resolution
        pass

    return (source_dir / target_path).resolve()


def check_file_links(root_path: Path, verbose: bool = False) -> tuple[int, int]:
    """
    Check all internal file links in markdown files.
    Returns tuple: (total_links_checked, broken_links_count)
    """
    markdown_files = find_markdown_files(root_path)
    total_links = 0
    broken_links = 0

    print(f"🔍 Checking internal file links in {len(markdown_files)} markdown files...")

    for md_file in markdown_files:
        try:
            content = md_file.read_text(encoding="utf-8")
            internal_links = extract_internal_links(content, md_file)

            if verbose and internal_links:
                print(f"\n📄 {md_file.relative_to(root_path)}")

            for link_text, line_num, link_target in internal_links:
                total_links += 1

                # Resolve the target path
                try:
                    resolved_path = resolve_relative_path(md_file, link_target)

                    # Check if the target file exists
                    if not resolved_path.exists():
                        broken_links += 1
                        print(
                            f"❌ BROKEN LINK in {md_file.relative_to(root_path)}:{line_num}"
                        )
                        print(f"   Link text: '{link_text}'")
                        print(f"   Target: '{link_target}'")
                        print(f"   Resolved to: {resolved_path}")
                        print()
                    elif verbose:
                        print(f"   ✅ Line {line_num}: '{link_text}' → {link_target}")

                except Exception as e:
                    broken_links += 1
                    print(
                        f"❌ ERROR resolving link in "
                        f"{md_file.relative_to(root_path)}:{line_num}"
                    )
                    print(f"   Link text: '{link_text}'")
                    print(f"   Target: '{link_target}'")
                    print(f"   Error: {e}")
                    print()

        except Exception as e:
            print(f"❌ ERROR reading file {md_file.relative_to(root_path)}: {e}")
            continue

    return total_links, broken_links


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Check internal file links in markdown files"
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Root directory to scan (default: current directory)",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Show all links checked, not just broken ones",
    )

    args = parser.parse_args()

    if not args.root.exists():
        print(f"❌ Root directory does not exist: {args.root}")
        return 1

    print("🔗 Internal File Link Checker")
    print("=" * 40)
    print(f"Root directory: {args.root.absolute()}")
    print()

    total_links, broken_links = check_file_links(args.root, args.verbose)

    print("=" * 40)
    print("📊 Results:")
    print(f"   Total internal links checked: {total_links}")
    print(f"   Broken links found: {broken_links}")

    if broken_links == 0:
        print("🎉 All internal file links are valid!")
        return 0
    else:
        print(f"❌ Found {broken_links} broken internal file links")
        return 1


if __name__ == "__main__":
    sys.exit(main())
