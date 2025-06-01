#!/usr/bin/env python3
"""
Template Compliance Checker for Prompt Library

This script validates that all prompt files follow the standard template structure
and reports any missing or incorrectly formatted sections.
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

# Required sections in the correct order
REQUIRED_SECTIONS = [
    "Description",
    "Usage",
    "Prompt",
    "Example Input",
    "Example Output",
    "Variations",
    "Tips",
    "Related Prompts",
    "Tags",
]


def extract_sections(content: str) -> Dict[str, str]:
    """Extract sections from markdown content."""
    sections = {}
    current_section = None
    current_content = []

    lines = content.split("\n")

    for line in lines:
        # Check if this is a section header (## Section Name)
        section_match = re.match(r"^## (.+)$", line.strip())
        if section_match:
            # Save previous section
            if current_section:
                sections[current_section] = "\n".join(current_content).strip()

            # Start new section
            current_section = section_match.group(1)
            current_content = []
        else:
            # Add content to current section
            if current_section:
                current_content.append(line)

    # Save last section
    if current_section:
        sections[current_section] = "\n".join(current_content).strip()

    return sections


def validate_prompt_file(file_path: Path) -> Tuple[bool, List[str]]:
    """Validate a single prompt file against the template."""
    errors = []

    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        return False, [f"Could not read file: {e}"]

    # Extract sections
    sections = extract_sections(content)

    # Check for required sections
    missing_sections = []
    for required_section in REQUIRED_SECTIONS:
        if required_section not in sections:
            missing_sections.append(required_section)
        elif not sections[required_section].strip():
            errors.append(f"Section '{required_section}' is empty")

    if missing_sections:
        errors.append(f"Missing required sections: {', '.join(missing_sections)}")

    # Check section order
    found_sections = [s for s in REQUIRED_SECTIONS if s in sections]
    section_headers = []

    for line in content.split("\n"):
        section_match = re.match(r"^## (.+)$", line.strip())
        if section_match:
            section_name = section_match.group(1)
            if section_name in REQUIRED_SECTIONS:
                section_headers.append(section_name)

    if section_headers != found_sections:
        errors.append(
            f"Sections are not in the correct order. Expected: {', '.join(REQUIRED_SECTIONS)}"
        )

    # Validate specific section content
    if "Tags" in sections:
        tags_content = sections["Tags"].strip()
        if not tags_content.startswith("`") or not tags_content.endswith("`"):
            errors.append("Tags section should be formatted as code with backticks")

    if "Prompt" in sections:
        prompt_content = sections["Prompt"].strip()
        if not prompt_content.startswith("```") or not prompt_content.endswith("```"):
            errors.append(
                "Prompt section should contain a properly formatted code block"
            )

    return len(errors) == 0, errors


def find_prompt_files(root_path: Path) -> List[Path]:
    """Find all prompt markdown files."""
    prompt_files = []

    # Skip template files and root-level docs
    skip_patterns = [
        "template",
        "README",
        "CONTRIBUTING",
        "SECURITY",
        "LICENSE",
    ]

    for md_file in root_path.rglob("*.md"):
        # Skip if it's in .github, templates, or examples directory
        excluded_dirs = [".github", "templates", "examples"]
        if any(excluded_dir in md_file.parts for excluded_dir in excluded_dirs):
            continue

        # Skip if filename contains skip patterns
        if any(pattern.lower() in md_file.name.lower() for pattern in skip_patterns):
            continue

        prompt_files.append(md_file)

    return sorted(prompt_files)


def main():
    """Main function to run compliance checks."""
    root_path = Path(".")

    print("Prompt Library Template Compliance Checker")
    print("=" * 50)

    prompt_files = find_prompt_files(root_path)

    if not prompt_files:
        print("ERROR: No prompt files found!")
        return 1

    print(f"Found {len(prompt_files)} prompt files to validate")
    print()

    total_files = len(prompt_files)
    valid_files = 0

    for file_path in prompt_files:
        relative_path = file_path.relative_to(root_path)
        is_valid, errors = validate_prompt_file(file_path)

        if is_valid:
            print(f"PASS: {relative_path}")
            valid_files += 1
        else:
            print(f"FAIL: {relative_path}")
            for error in errors:
                print(f"   * {error}")
            print()

    print("=" * 50)
    print(f"Summary: {valid_files}/{total_files} files passed validation")

    if valid_files == total_files:
        print("SUCCESS: All prompt files are compliant with the template!")
        return 0
    else:
        print(f"WARNING: {total_files - valid_files} files need attention")
        return 1


if __name__ == "__main__":
    sys.exit(main())
