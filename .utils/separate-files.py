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


def extract_content(node):
    """新核心逻辑：提取内容并移除列表符号"""
    lines = []
    # 移除当前节点的列表符号
    clean_line = re.sub(r'^-\s+', '', node.content, count=1)
    # 保留引用格式的">"
    clean_line = re.sub(r'^>\s+', '> ', clean_line)
    if clean_line.strip():
        lines.append(clean_line)
    # 递归处理子节点
    for child in node.children:
        lines.extend(extract_content(child))
    return lines


def sanitize_filename(title):
    """增强版文件名安全处理函数"""
    # Step 1: 替换所有空格和标点符号为短横线
    safe_name = re.sub(
        r'[\s!\"#\$%&\'\(\)\*\+,\./:;<=>\?@\[\\\]\^`\{\|\}~，。、；：‘’“”《》【】〔〕「」？〈〉…—]+',
        '-',
        title
    )

    # Step 2: 替换非法文件名字符
    safe_name = re.sub(r'[\\/*?:"<>|]', '-', safe_name)

    # Step 3: 合并连续短横线并去除首尾
    safe_name = re.sub(r'-+', '-', safe_name).strip('-')

    # Step 4: 处理空文件名情况
    if not safe_name:
        safe_name = 'untitled'

    # Step 5: 添加波浪线前缀并返回
    return f'~{safe_name}.md'


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

        # 生成正文内容
        body_lines = []
        for child in node.children:
            body_lines.extend(extract_content(child))

        # 优化段落格式：条目间保留一个空行
        formatted_body = '\n\n'.join(body_lines)

        # 写入文件
        filename = sanitize_filename('~'+title)
        output_path = os.path.join(output_dir, filename)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(front_matter))
            f.write(formatted_body)
        #     '\n'.join(
        print(f"Created: {output_path}")


if __name__ == '__main__':
    # 配置输入输出路径
    INPUT_FILE = "input.md"
    OUTPUT_DIR = "output"

    process_file(INPUT_FILE, OUTPUT_DIR)