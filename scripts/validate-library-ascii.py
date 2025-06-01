#!/usr/bin/env python3
"""
Simple test runner for prompt library validation.
This script runs basic checks that can be automated in CI/CD.
"""

import subprocess
import sys
from pathlib import Path


def run_markdown_lint():
    """Run markdownlint on all markdown files."""
    print("Running markdown lint checks...")
    try:
        result = subprocess.run(
            ["markdownlint", "**/*.md", "--config", ".markdownlint.json"],
            capture_output=True,
            text=True,
            cwd=Path.cwd(),
        )

        if result.returncode == 0:
            print("PASS: Markdown lint passed")
            return True
        else:
            print("FAIL: Markdown lint failed:")
            print(result.stdout)
            print(result.stderr)
            return False
    except FileNotFoundError:
        print("SKIP: markdownlint not found, skipping")
        return True


def run_template_compliance():
    """Run template compliance checker."""
    print("Running template compliance checks...")
    try:
        result = subprocess.run(
            ["python", "scripts/check-template-compliance.py"],
            capture_output=True,
            text=True,
            cwd=Path.cwd(),
        )

        print(result.stdout)
        if result.stderr:
            print(result.stderr)

        return result.returncode == 0
    except Exception as e:
        print(f"FAIL: Template compliance check failed: {e}")
        return False


def check_required_files():
    """Check that all required files exist."""
    print("Checking required files...")
    required_files = [
        "README.md",
        "CONTRIBUTING.md",
        "LICENSE",
        "SECURITY.md",
        ".markdownlint.json",
        ".markdown-link-check.json",
        ".spellcheck.yml",
        "scripts/check-template-compliance.py",
    ]

    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)

    if missing_files:
        print(f"FAIL: Missing required files: {', '.join(missing_files)}")
        return False
    else:
        print("PASS: All required files present")
        return True


def check_directory_structure():
    """Check that expected directory structure exists."""
    print("Checking directory structure...")
    required_dirs = [
        "development",
        "writing",
        "business",
        "analysis",
        "creative",
        "education",
        "productivity",
        "templates",
        "examples",
        "scripts",
        ".github",
    ]

    missing_dirs = []
    for dir_path in required_dirs:
        if not Path(dir_path).is_dir():
            missing_dirs.append(dir_path)

    if missing_dirs:
        print(f"FAIL: Missing required directories: {', '.join(missing_dirs)}")
        return False
    else:
        print("PASS: All required directories present")
        return True


def main():
    """Run all validation checks."""
    print("Prompt Library Validation Suite")
    print("=" * 40)

    checks = [
        check_required_files,
        check_directory_structure,
        run_template_compliance,
        run_markdown_lint,
    ]

    passed = 0
    total = len(checks)

    for check in checks:
        if check():
            passed += 1
        print()

    print("=" * 40)
    print(f"Results: {passed}/{total} checks passed")

    if passed == total:
        print("SUCCESS: All validation checks passed!")
        return 0
    else:
        print("FAIL: Some validation checks failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
