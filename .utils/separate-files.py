import re
import os
from datetime import datetime


class Node:
    def __init__(self, indent, content):
        self.indent = indent
        self.content = content
        self.children = []


def parse_lines(lines):
    """解析文本行并构建层级树结构"""
    root = Node(-1, "")
    stack = [root]
    for line in lines:
        stripped = line.lstrip()
        indent = len(line) - len(stripped)
        while stack[-1].indent >= indent:
            stack.pop()
        parent = stack[-1]
        node = Node(indent, stripped)
        parent.children.append(node)
        stack.append(node)
    return root


def generate_subcontent(node, base_indent):
    """生成调整缩进后的子内容"""
    lines = []
    current_indent = node.indent - base_indent
    if current_indent < 0:
        current_indent = 0
    lines.append(" " * current_indent + node.content)
    for child in node.children:
        lines.extend(generate_subcontent(child, base_indent))
    return lines


def sanitize_filename(title):
    """清理标题生成安全文件名"""
    title = re.sub(r'[\\/*?:"<>|]', '_', title)
    return title.strip() + '.md'


def process_file(input_path, output_dir):
    """处理输入文件并生成输出"""
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = [line.rstrip('\n') for line in f]

    root = parse_lines(lines)
    os.makedirs(output_dir, exist_ok=True)

    for node in root.children:
        # 提取标题和URL
        title_match = re.match(r'^- \[([^\]]+)\]\(([^)]+)\)', node.content)
        if title_match:
            title, url = title_match.groups()
        else:
            plain_match = re.match(r'^- (.*)', node.content)
            if not plain_match:
                continue
            title, url = plain_match.group(1), None

        # 生成front matter
        now = datetime.now().replace(microsecond=0)
        front_matter = [
            "---",
            f'title: "{title}"',
            f'created: {now.isoformat()}',
            f'modified: {now.isoformat()}',
        ]
        if url:
            front_matter.append(f'source: {url}')
        front_matter.extend([
            'tags:',
            'tags-link:',
            'type: archive-web',
            '---\n'
        ])

        # 生成内容
        content_lines = []
        for child in node.children:
            content_lines.extend(generate_subcontent(child, node.indent))

        # 写入文件
        filename = sanitize_filename(title)
        output_path = os.path.join(output_dir, filename)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(front_matter))
            f.write('\n'.join(content_lines))
        print(f"Created: {output_path}")


if __name__ == '__main__':
    # 配置输入输出路径
    INPUT_FILE = "input.md"
    OUTPUT_DIR = "output"

    process_file(INPUT_FILE, OUTPUT_DIR)