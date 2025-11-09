#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add or modify draft property in markdown files' frontmatter.

This script:
1. Traverses markdown files in a specified directory (or all files by default)
2. Adds or modifies 'draft' property to the frontmatter
3. Supports setting draft to true or false
4. Skips files that already have draft property (unless --force is used)
5. Shows progress with a progress bar and logs
"""

import os
import re
import sys
import argparse
import time
from pathlib import Path
from typing import Tuple, Optional


def print_progress_bar(current: int, total: int, desc: str = "Progress") -> None:
    """Print a simple progress bar without external dependencies."""
    if total == 0:
        return
    
    percent = 100 * current / total
    bar_length = 40
    filled = int(bar_length * current / total)
    bar = '█' * filled + '░' * (bar_length - filled)
    
    # Use carriage return to overwrite the line
    sys.stdout.write(f'\r{desc}: |{bar}| {percent:.1f}% ({current}/{total})')
    sys.stdout.flush()
    
    if current == total:
        sys.stdout.write('\n')
        sys.stdout.flush()


def is_markdown_file(filepath: Path) -> bool:
    """Check if file is a markdown file."""
    return filepath.suffix.lower() == '.md' and filepath.is_file()


def extract_frontmatter(content: str) -> Tuple[Optional[str], str]:
    """
    Extract YAML frontmatter from markdown content.
    
    Returns:
        Tuple of (frontmatter, remaining_content) or (None, content) if no frontmatter
    """
    # Match YAML frontmatter: starts with --- and ends with ---
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if match:
        return match.group(1), match.group(2)
    return None, content


def has_draft_property(frontmatter: str) -> bool:
    """Check if frontmatter already has draft property."""
    # Look for 'draft:' at the start of a line (with optional spaces)
    return bool(re.search(r'^\s*draft\s*:', frontmatter, re.MULTILINE))


def get_draft_value(frontmatter: str) -> Optional[str]:
    """Extract the draft property value from frontmatter."""
    match = re.search(r'^\s*draft\s*:\s*(.+?)(?:\s*#.*)?$', frontmatter, re.MULTILINE)
    if match:
        return match.group(1).strip().lower()
    return None


def set_draft_property(frontmatter: str, value: bool) -> str:
    """Set draft property to a specific value (true/false)."""
    value_str = 'true' if value else 'false'
    
    # Replace existing draft property
    if has_draft_property(frontmatter):
        new_frontmatter = re.sub(
            r'^\s*draft\s*:\s*.+?(?=\n|$)',
            f'draft: {value_str}',
            frontmatter,
            flags=re.MULTILINE
        )
        return new_frontmatter
    else:
        # Add draft property at the beginning
        return f"draft: {value_str}\n{frontmatter}"


def add_draft_property(frontmatter: str, value: bool = True) -> str:
    """Add draft property at the beginning of frontmatter."""
    value_str = 'true' if value else 'false'
    return f"draft: {value_str}\n{frontmatter}"


def create_frontmatter(body: str, draft_value: bool = True) -> str:
    """Create new frontmatter for files without one."""
    value_str = 'true' if draft_value else 'false'
    return f"---\ndraft: {value_str}\n---\n{body}"


def process_file(filepath: Path, draft_value: bool = True, force: bool = False) -> Tuple[bool, str]:
    """
    Process a single markdown file.
    
    Args:
        filepath: Path to the markdown file
        draft_value: True to set draft to true, False to set draft to false
        force: If True, update existing draft properties; if False, skip them
    
    Returns:
        Tuple of (success, message)
    """
    try:
        content = filepath.read_text(encoding='utf-8')
        
        # Extract frontmatter
        frontmatter, body = extract_frontmatter(content)
        
        if frontmatter is None:
            # No frontmatter exists, create one
            new_content = create_frontmatter(body, draft_value)
            filepath.write_text(new_content, encoding='utf-8')
            return True, "created"
        
        # Check if draft property already exists
        if has_draft_property(frontmatter):
            if not force:
                current_value = get_draft_value(frontmatter)
                return True, f"skipped (draft={current_value})"
            
            # Force update: modify existing draft property
            old_value = get_draft_value(frontmatter)
            new_frontmatter = set_draft_property(frontmatter, draft_value)
            new_content = f"---\n{new_frontmatter}\n---\n{body}"
            filepath.write_text(new_content, encoding='utf-8')
            return True, f"updated (draft={old_value} → {draft_value})"
        
        # Add draft property
        new_frontmatter = add_draft_property(frontmatter, draft_value)
        new_content = f"---\n{new_frontmatter}\n---\n{body}"
        filepath.write_text(new_content, encoding='utf-8')
        return True, "updated"
        
    except Exception as e:
        return False, f"error: {str(e)}"


def get_vault_root() -> Path:
    """Get the vault root directory (parent of .utils directory)."""
    current_file = Path(__file__).resolve()
    vault_root = current_file.parent.parent
    return vault_root


def is_hidden_path(filepath: Path, root: Path) -> bool:
    """Check if filepath contains hidden directories (starting with .)"""
    try:
        rel_path = filepath.relative_to(root)
        return any(part.startswith('.') for part in rel_path.parts)
    except ValueError:
        return False


def collect_markdown_files(scan_dir: Path, exclude_hidden: bool = True) -> list:
    """Collect all markdown files in a directory."""
    md_files = list(scan_dir.rglob('*.md'))
    
    if exclude_hidden:
        md_files = [f for f in md_files if not is_hidden_path(f, scan_dir)]
    
    return sorted(md_files)


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description='Add or modify draft property in markdown files frontmatter',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Add draft: true to all markdown files in vault
  python3 add-draft-properties.py
  
  # Add draft: true to all markdown files in a specific folder
  python3 add-draft-properties.py --folder ./pages
  
  # Set draft: false for all files in a folder (with force)
  python3 add-draft-properties.py --folder ./projects --draft false --force
  
  # Force update all existing draft properties to false
  python3 add-draft-properties.py --draft false --force
        '''
    )
    
    parser.add_argument(
        '--folder',
        type=str,
        default=None,
        help='Target folder to process (relative to vault root or absolute path). Default: entire vault'
    )
    parser.add_argument(
        '--draft',
        choices=['true', 'false'],
        default='true',
        help='Set draft property to true or false. Default: true'
    )
    parser.add_argument(
        '--force',
        action='store_true',
        help='Force update existing draft properties. Default: skip files with draft property'
    )
    parser.add_argument(
        '--include-hidden',
        action='store_true',
        help='Include files in hidden directories (starting with .)'
    )
    
    args = parser.parse_args()
    
    vault_root = get_vault_root()
    draft_value = args.draft.lower() == 'true'
    
    # Determine target directory
    if args.folder:
        # Try as relative path first, then as absolute path
        target_dir = Path(args.folder)
        if not target_dir.is_absolute():
            target_dir = vault_root / target_dir
        
        if not target_dir.exists():
            print(f"❌ Error: Directory not found: {target_dir}")
            sys.exit(1)
        if not target_dir.is_dir():
            print(f"❌ Error: Not a directory: {target_dir}")
            sys.exit(1)
    else:
        target_dir = vault_root
    
    print(f"📁 Vault root: {vault_root}")
    print(f"📂 Target dir: {target_dir}")
    print(f"🔍 Scanning for markdown files...\n")
    
    # Collect all markdown files
    md_files = collect_markdown_files(target_dir, exclude_hidden=not args.include_hidden)
    
    total = len(md_files)
    print(f"📊 Found {total} markdown files")
    print(f"⚙️  draft={str(draft_value).lower()}, force={args.force}\n")
    
    if total == 0:
        print("✨ No markdown files found!")
        return
    
    # Statistics
    stats = {
        'created': 0,
        'updated': 0,
        'skipped': 0,
        'error': 0
    }
    
    errors = []
    
    # Process files with progress bar
    for idx, filepath in enumerate(md_files, 1):
        success, message = process_file(filepath, draft_value=draft_value, force=args.force)
        
        if success:
            if 'created' in message:
                stats['created'] += 1
            elif 'updated' in message:
                stats['updated'] += 1
            elif 'skipped' in message:
                stats['skipped'] += 1
        else:
            stats['error'] += 1
            rel_path = filepath.relative_to(vault_root)
            errors.append(f"  ❌ {rel_path}: {message}")
        
        print_progress_bar(idx, total, desc="Processing")
    
    # Print summary
    print("\n" + "="*70)
    print("📈 Processing Summary")
    print("="*70)
    print(f"✅ Created (new frontmatter):  {stats['created']:>6}")
    print(f"🔄 Updated (added/modified):   {stats['updated']:>6}")
    print(f"⏭️  Skipped (already exists):   {stats['skipped']:>6}")
    print(f"❌ Errors:                     {stats['error']:>6}")
    print(f"📊 Total:                      {total:>6}")
    print("="*70)
    
    if errors:
        print("\n⚠️  Errors encountered:")
        for error in errors[:10]:  # Show first 10 errors
            print(error)
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more errors")
    
    print("\n✨ Done!")


if __name__ == '__main__':
    main()
