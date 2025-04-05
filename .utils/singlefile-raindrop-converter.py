import os
import re
from bs4 import BeautifulSoup
import html2text
from pathlib import Path


def convert_singlefile_html_to_md(input_path, output_path):
    """转换单个 HTML 文件为 Markdown"""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # 处理高亮标记（SingleFile 的高亮通常是黄色背景）
        html_content = re.sub(
            r'<mark[^"]*">(.*?)</mark>',
            r'==\1==',  # 使用 == 包裹表示高亮（部分 Markdown 解析器支持）
            html_content,
            flags=re.IGNORECASE
        )

        # 使用 html2text 转换
        h = html2text.HTML2Text()
        h.body_width = 0  # 禁用换行
        h.ignore_links = False  # 保留链接
        h.ignore_images = True  # 忽略图片（可选）
        md_content = h.handle(html_content)

        # 创建输出目录
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)

    except Exception as e:
        print(f"转换失败 {input_path}: {str(e)}")


def batch_convert_html_to_md(input_dir, output_dir):
    """批量转换目录中的 HTML 文件"""
    for root, _, files in os.walk(input_dir):
        for filename in files:
            if filename.lower().endswith('.html'):
                input_path = os.path.join(root, filename)
                relative_path = os.path.relpath(input_path, input_dir)
                output_path = os.path.join(output_dir, relative_path[:-5] + '.md')
                convert_singlefile_html_to_md(input_path, output_path)
                print(f"已转换: {input_path} -> {output_path}")


if __name__ == "__main__":
    input_directory = "/Users/bgzo/Library/Mobile Documents/iCloud~md~obsidian/Documents/wiki/archives/archived_web/zmt/"  # 替换为输入目录
    output_directory = "/Users/bgzo/Library/Mobile Documents/iCloud~md~obsidian/Documents/wiki/.utils/html_convert"  # 替换为输出目录
    batch_convert_html_to_md(input_directory, output_directory)