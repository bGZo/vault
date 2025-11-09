import os
import re
import urllib.parse
from pathlib import Path
from datetime import datetime
import html2text


def extract_datetime_from_filename(filename):
    """从文件名提取时间戳（优先处理）"""
    timestamp_pattern = r" \((\d+_\d+_\d{4} \d+_\d+_\d+ [AP]M)\)\.html$"
    match = re.search(timestamp_pattern, filename, re.IGNORECASE)

    if match:
        try:
            dt_str = match.group(1).replace("_", " ")
            return datetime.strptime(dt_str, "%m %d %Y %I %M %S %p")
        except:
            pass
    return None


def extract_metadata(html_content, filename):
    """混合来源提取元数据"""
    # 优先从文件名获取时间
    dt = extract_datetime_from_filename(filename)

    # 次选从 HTML 注释获取
    if not dt:
        match = re.search(
            r"saved date:\s*(.*?)\s+-->",
            html_content,
            re.DOTALL | re.IGNORECASE
        )
        if match:
            try:
                dt_str = match.group(1).split("(")[0].strip()
                return datetime.strptime(dt_str, "%a %b %d %Y %H:%M:%S %Z%z")
            except:
                pass

    # 最后使用当前时间
    return datetime.now()


def clean_filename(filename):
    """清理文件名中的时间戳部分"""
    # 移除时间戳模式
    cleaned = re.sub(
        r" \(\d+_\d+_\d{4} \d+_\d+_\d+ [AP]M\)\.html$",
        "",
        filename,
        flags=re.IGNORECASE
    )
    # 移除扩展名和 URL 编码
    return urllib.parse.unquote(cleaned.replace(".html", "")).strip()


def generate_front_matter(input_path, url, dt):
    """生成带清理标题的 Front Matter"""
    filename = os.path.basename(input_path)
    title = clean_filename(filename)

    iso_date = dt.strftime("%Y-%m-%dT%H:%M:%S%z")
    return f"""---
title: "{title}"
created: {iso_date}
modified: {iso_date}
source: {url}
tags:
tags-link:
type: archive-web
---

"""


def convert_singlefile_html_to_md(input_path, output_dir):
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        # 提取元数据
        url_match = re.search(r"url:\s*(.*?)\s+saved date:", html_content)
        url = url_match.group(1).strip() if url_match else "unknown"
        dt = extract_metadata(html_content, os.path.basename(input_path))

        # 处理高亮
        html_content = re.sub(
            r"<mark\b[^>]*>(.*?)</mark>",
            r"==\1==",
            html_content,
            flags=re.DOTALL
        )

        # 生成输出路径
        clean_name = sanitize_filename(clean_filename(os.path.basename(input_path))) + ".md"
        relative_path = os.path.relpath(input_path, input_directory)
        output_path = os.path.join(output_dir, os.path.dirname(relative_path), clean_name)
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)

        # 转换内容
        h = html2text.HTML2Text()
        h.body_width = 0
        md_content = generate_front_matter(input_path, url, dt) + h.handle(html_content)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(md_content)

    except Exception as e:
        print(f"转换失败 {input_path}: {str(e)}")


def batch_convert_html_to_md(input_dir, output_dir):
    for root, _, files in os.walk(input_dir):
        for filename in files:
            if filename.lower().endswith(".html"):
                input_path = os.path.join(root, filename)
                convert_singlefile_html_to_md(input_path, output_dir)
                print(f"已转换: {input_path} -> {os.path.join(output_dir, sanitize_filename(clean_filename(filename)))}.md")


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
    return f'~{safe_name}'


if __name__ == "__main__":
    input_directory = "/Users/bgzo/Library/Mobile Documents/iCloud~md~obsidian/Documents/wiki/archives/archived_web/"  # 替换为输入目录
    output_directory = "/Users/bgzo/Library/Mobile Documents/iCloud~md~obsidian/Documents/wiki/.utils/html_convert"  # 替换为输出目录
    batch_convert_html_to_md(input_directory, output_directory)