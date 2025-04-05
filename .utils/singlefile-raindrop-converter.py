import os
import re
import urllib.parse
from pathlib import Path
from datetime import datetime
import html2text


def extract_metadata(html_content):
    """从 HTML 注释中提取 URL 和保存时间"""
    url, saved_date = "unknown", "unknown"
    match = re.search(
        r"url:\s*(.*?)\s+saved date:\s*(.*?)\s+-->",
        html_content,
        re.DOTALL | re.IGNORECASE
    )
    if match:
        url = match.group(1).strip()
        saved_date = match.group(2).split("(")[0].strip()  # 移除时区描述
    return url, saved_date


def generate_front_matter(input_path, url, saved_date):
    """生成 Markdown Front Matter"""
    filename = os.path.splitext(os.path.basename(input_path))[0]
    title = urllib.parse.unquote(filename)  # 解码 URL 编码字符
    return f"""---
title: "{title}"
created: {saved_date}
modified: {saved_date}
source: {url}
tags:
tags-link:
type: archive-web
---

"""


def convert_singlefile_html_to_md(input_path, output_path):
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        # 提取元数据
        url, saved_date = extract_metadata(html_content)

        # 处理高亮标记（支持任意属性的 <mark> 标签）
        html_content = re.sub(
            r"<mark\b[^>]*>(.*?)</mark>",
            r"==\1==",
            html_content,
            flags=re.DOTALL | re.IGNORECASE
        )

        # 转换 HTML 为 Markdown
        h = html2text.HTML2Text()
        h.body_width = 0
        h.ignore_links = False
        md_content = h.handle(html_content)

        # 添加 Front Matter
        front_matter = generate_front_matter(input_path, url, saved_date)
        md_content = front_matter + md_content

        # 确保输出目录存在
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(md_content)

    except Exception as e:
        print(f"转换失败 {input_path}: {str(e)}")


def batch_convert_html_to_md(input_dir, output_dir):
    for root, _, files in os.walk(input_dir):
        for filename in files:
            if filename.lower().endswith(".html"):
                input_path = os.path.join(root, filename)
                relative_path = os.path.relpath(input_path, input_dir)
                output_path = os.path.join(output_dir, sanitize_filename(relative_path[:-5]) + ".md")
                convert_singlefile_html_to_md(input_path, output_path)
                print(f"已转换: {input_path} -> {output_path}")

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


if __name__ == "__main__":
    input_directory = "/Users/bgzo/Library/Mobile Documents/iCloud~md~obsidian/Documents/wiki/archives/archived_web/zmt/"  # 替换为输入目录
    output_directory = "/Users/bgzo/Library/Mobile Documents/iCloud~md~obsidian/Documents/wiki/.utils/html_convert"  # 替换为输出目录
    batch_convert_html_to_md(input_directory, output_directory)