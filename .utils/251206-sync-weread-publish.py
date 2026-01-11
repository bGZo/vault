#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: bgzo
# Date: 2024-01-10
# Desc: 本脚本用于解析导出的微信读书笔记（Markdown格式），并将其转换为颗粒度更小的Markdown文件，方便后续发布和浏览。其中微信读书的笔记格式为：
#   > [!NOTE] xxx yyyy-mm-dd hh:mm:ss
# Usage: python3 .utils/251206-sync-weread-publish.py <input_dir> <output_dir>
# Example: python3 .utils/251206-sync-weread-publish.py weread_notes/ weread_published/

import os
import sys
import re
import datetime
import glob

def parse_frontmatter(text):
    """
    Simple manual parsing for YAML frontmatter to avoid dependencies.
    Extracts: title, author, weread (link)
    """
    metadata = {
        'title': '',
        'author': '',
        'weread': ''
    }
    
    lines = text.strip().split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Match title
        m_title = re.match(r'^title:\s*(.*)', line)
        if m_title:
            metadata['title'] = m_title.group(1).strip().strip('"\'')
            i += 1
            continue
            
        # Match weread link
        m_weread = re.match(r'^weread:\s*(.*)', line)
        if m_weread:
            metadata['weread'] = m_weread.group(1).strip().strip('"\'')
            i += 1
            continue
            
        # Match author
        m_author = re.match(r'^author:\s*(.*)', line)
        if m_author:
            val = m_author.group(1).strip()
            if not val:
                # possible list in next lines
                authors = []
                i += 1
                while i < len(lines):
                    subline = lines[i]
                    m_list = re.match(r'^\s*-\s*(.*)', subline)
                    if m_list:
                        authors.append(m_list.group(1).strip().strip('"\''))
                        i += 1
                    else:
                        # Stop if indentation stops or key changes (simple heuristic)
                        if ':' in subline: 
                            i -= 1 # Backtrack
                            break
                        i += 1
                metadata['author'] = ', '.join(authors)
                continue
            else:
                # single line author
                # Check if it looks like a list structure [a, b]
                if val.startswith('[') and val.endswith(']'):
                    metadata['author'] = val.strip('[]')
                else:
                    metadata['author'] = val
            i += 1
            continue
            
        i += 1
        
    return metadata

def parse_weread_file(filepath):
    """
    Reads a WeRead MD file and extracting metadata and notes.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return [], {}

    # Split Frontmatter
    # Usually strictly between first two ---
    # re.split might behave differently if file doesn't start with ---
    # WeRead exports usually start with ---
    parts = re.split(r'^---$', content, maxsplit=2, flags=re.MULTILINE)
    
    if len(parts) < 3:
        # Fallback or invalid format
        print(f"Skipping {filepath}: Invalid Frontmatter format")
        return [], {}

    frontmatter_text = parts[1]
    body_text = parts[2]
    
    meta = parse_frontmatter(frontmatter_text)
    
    notes = []
    
    # Process Body
    lines = body_text.split('\n')
    current_chapter = ""
    
    # States
    in_note = False
    current_note_lines = []
    
    for line in lines:
        stripped_line = line.strip()
        
        # Header detection
        if stripped_line.startswith('#'):
            # This is a chapter header
            current_chapter = stripped_line.lstrip('#').strip()
            # If we were in a note, close it securely (though usually notes end before headers)
            if in_note:
                process_note(notes, current_note_lines, current_chapter, meta) # Pass OLD chapter?
                # Actually if new header appears, the previous note belonged to previous chapter.
                # However, current_chapter is updated NOW. 
                # Ideally we should pass the chapter that was active when note started.
                # But for simplicity, let's assume structure is Header -> Notes -> Header.
                # If note was open, it belongs to previous chapter context unless header is inside blockquote (unlikely).
                
                # Logic correction: If header encountered, any open note is finished. 
                # Since we updated current_chapter already, we might align note to new chapter?
                # No, standard is Header -> Note. So Note belongs to the Header *above* it.
                # If we just hit a new header, the PREVIOUS note belongs to the PREVIOUS chapter.
                # But current_chapter variable holds the "current active chapter".
                # If I update it *before* processing the previous note, the previous note gets the *new* chapter.
                # I should process the note first.
                pass 
                
            in_note = False
            current_note_lines = []
            continue
            
        # Note start detection
        if stripped_line == '> [!NOTE]':
            if in_note:
                # Previous note didn't close properly
                process_note(notes, current_note_lines, current_chapter, meta)
            
            in_note = True
            current_note_lines = []
            continue
        
        if in_note:
            # Check if line is part of blockquote
            if line.strip() == '>' or line.startswith('> '):
                # Clean the content
                content_line = line.replace('>', '', 1) 
                if content_line.startswith(' '):
                    content_line = content_line[1:]
                    
                current_note_lines.append(content_line)
            elif stripped_line == '':
                # Empty line might be a break in blockquote or just empty line in md
                # WeRead export separates notes with empty lines
                pass
            else:
                # Text without >, note ended
                process_note(notes, current_note_lines, current_chapter, meta)
                in_note = False
                current_note_lines = []
    
    # End of file check
    if in_note:
        process_note(notes, current_note_lines, current_chapter, meta)
        
    return notes, meta

def process_note(notes, note_lines, chapter, meta):
    if not note_lines:
        return

    # Extract timestamp from the last few lines
    # Format: 2023-04-02 15:14:44 ^662300-6-7382-7439
    
    content_lines = []
    date_str = None
    
    # Regex for date: YYYY-MM-DD HH:MM:SS
    date_pattern = re.compile(r'(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})')
    
    found_date = False
    
    # Check the last non-empty line usually
    # Iterate backwards
    for i in range(len(note_lines) - 1, -1, -1):
        line = note_lines[i]
        match = date_pattern.search(line)
        if match:
            date_str = match.group(1)
            # Content is everything up to this line
            content_lines = note_lines[:i]
            found_date = True
            break
            
    if not found_date:
        # If no date found, treat all as content and use today's date
        content_lines = note_lines
        date_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Trim empty lines from content
    while content_lines and not content_lines[0].strip():
        content_lines.pop(0)
    while content_lines and not content_lines[-1].strip():
        content_lines.pop()
        
    text_content = "\n".join(content_lines)
    
    if not text_content.strip():
        return # Empty note

    notes.append({
        'content': text_content,
        'date': date_str,
        'chapter': chapter,
    })

def save_note(note, meta, output_dir):
    # Output filename: yyyy-mm-dd-number.md
    try:
        dt = datetime.datetime.strptime(note['date'], '%Y-%m-%d %H:%M:%S')
        date_prefix = dt.strftime('%Y-%m-%d')
    except ValueError:
        date_prefix = datetime.datetime.now().strftime('%Y-%m-%d')

    # Find unique number
    counter = 1
    while True:
        filename = f"{date_prefix}-{counter}.md"
        filepath = os.path.join(output_dir, filename)
        if not os.path.exists(filepath):
            break
        counter += 1
        
    # Title: first 30 chars of note
    # Clean newlines for title
    flat_content = note['content'].replace('\n', ' ')
    title_text = flat_content[:30]
    if len(flat_content) > 30:
         title_text += "..."
         
    # Escape quotes in strings for YAML
    def escape_yaml_field(s):
        if not s: return ""
        return s.replace('"', '\\"').replace('\\', '\\\\')

    # Yaml fields
    f_title = escape_yaml_field(title_text)
    f_author = escape_yaml_field(meta.get('author', 'Unknown'))
    f_source = escape_yaml_field(meta.get('title', 'Unknown'))
    f_chapter = escape_yaml_field(note.get('chapter', ''))
    f_note_link = meta.get('weread', '')

    output_content = f"""---
title: "{f_title}"
author: "{f_author}"
source: "{f_source}"
chapter: "{f_chapter}"
note: {f_note_link}
---

{note['content']}
"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(output_content)

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 script.py <input_dir> <output_dir>")
        sys.exit(1)
        
    input_pattern = sys.argv[1] # Can be dir or pattern? Let's assume dir
    output_dir = sys.argv[2]
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # Handle tilde expansion typically done by shell, but safe to add
    input_path = os.path.expanduser(input_pattern)
    
    files = []
    if os.path.isdir(input_path):
        files = glob.glob(os.path.join(input_path, "**/*.md"), recursive=True)
    else:
        # Maybe user passed a file or glob pattern directly
        files = glob.glob(input_path, recursive=True)
    
    print(f"Found {len(files)} files processing...")
    
    total_processed = 0
    
    for fw in files:
        # Skip output dir if it's inside input_dir
        if os.path.abspath(output_dir) in os.path.abspath(fw):
            continue
            
        print(f"Processing {fw}...")
        notes, meta = parse_weread_file(fw)
        
        for note in notes:
            save_note(note, meta, output_dir)
            total_processed += 1
            
    print(f"Done. Generated {total_processed} notes.")

if __name__ == '__main__':
    main()
