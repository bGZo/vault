import os
import re
import glob

# Source and destination directories
source_dir = "/Users/bgzo/Library/Mobile Documents/iCloud~md~obsidian/Documents/vault/templates"
dest_dir = "/Users/bgzo/Library/Mobile Documents/iCloud~md~obsidian/Documents/vault/templaters"

# Ensure destination directory exists
os.makedirs(dest_dir, exist_ok=True)

# Regex patterns for Obsidian Core Templates
# {{title}} -> <% tp.file.title %>
pattern_title = re.compile(r"\{\{title\}\}")

# {{date}} -> <% tp.date.now("YYYY-MM-DD") %> 
# Note: Core defaults check. Usually system format, but often assumes YYYY-MM-DD in user minds.
# Safest is to stick to YYYY-MM-DD if no format specified, or maybe just tp.date.now().
# Let's use ("YYYY-MM-DD") for {{date}} and ("HH:mm") for {{time}} as sensible defaults.
pattern_date_default = re.compile(r"\{\{date\}\}")
pattern_time_default = re.compile(r"\{\{time\}\}")

# {{date:FORMAT}} -> <% tp.date.now("FORMAT") %>
pattern_date_format = re.compile(r"\{\{date:(.*?)\}\}")

# {{time:FORMAT}} -> <% tp.date.now("FORMAT") %>
pattern_time_format = re.compile(r"\{\{time:(.*?)\}\}")


def convert_content(content):
    # Order matters slightly. Specific formats should be handled.
    # Actually regex with capture groups handles formatting.
    
    # Handle {{date:Format}} and {{time:Format}}
    content = pattern_date_format.sub(r'<% tp.date.now("\1") %>', content)
    content = pattern_time_format.sub(r'<% tp.date.now("\1") %>', content)
    
    # Handle simple {{date}} and {{time}} and {{title}}
    content = pattern_title.sub(r'<% tp.file.title %>', content)
    content = pattern_date_default.sub(r'<% tp.date.now("YYYY-MM-DD") %>', content)
    content = pattern_time_default.sub(r'<% tp.date.now("HH:mm") %>', content)
    
    return content

files = glob.glob(os.path.join(source_dir, "*.md"))

print(f"Found {len(files)} files to process.")

for file_path in files:
    filename = os.path.basename(file_path)
    dest_path = os.path.join(dest_dir, filename)
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    new_content = convert_content(content)
    
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print(f"Converted {filename}")
