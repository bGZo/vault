#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import glob
from pathlib import Path
import opencc
import frontmatter
import re

"""
Global Variables:
"""
SENSITIVE_TAGS = {
    'flamewar',  # 争议相关
    'love/letter',      # 私情相关
    'sex',              # 性相关
    'politics',         # 政治相关
    'religion',         # 宗教相关
    'pointless',        # 无意义内容
    'spam',             # 垃圾内容
    'private',          # 私人内容
    'relationship',     # 关系相关
    'privacy',          # 隐私相关
}


def process_obsidian_content(content):
    """
    处理Obsidian特有的双链语法，转换为通用Markdown格式

    1. [[link]] -> link（纯文本）
    2. [[link|display]] -> display（显示文本）
    3. [[#heading]] -> heading（标题链接）
    4. [[file#heading]] -> file > heading（文件中的标题）
    5. [[file#heading|display]] -> display（带显示文本的文件标题链接）
    6. ![[embed]] -> （移除嵌入内容）
    7. [[file.png]] -> file.png（图片链接转为文本）
    """

    # 1. 处理嵌入语法 ![[...]]，直接删除
    content = re.sub(r'!\[\[([^\]]+)\]\]', '', content)

    # 2. 处理带显示文本的双链 [[link|display]]
    def replace_display_link(match):
        full_link = match.group(1)
        if '|' in full_link:
            _, display_text = full_link.split('|', 1)
            return display_text.strip()
        return full_link

    content = re.sub(r'\[\[([^\]]+\|[^\]]+)\]\]', replace_display_link, content)

    # 3. 处理文件中的标题链接 [[file#heading]]
    def replace_file_heading_link(match):
        link_content = match.group(1)
        if '#' in link_content:
            file_part, heading_part = link_content.split('#', 1)
            if file_part.strip():
                return f"{file_part.strip()} > {heading_part.strip()}"
            else:
                return heading_part.strip()
        return link_content

    content = re.sub(r'\[\[([^|\]]+#[^|\]]+)\]\]', replace_file_heading_link, content)

    # 4. 处理简单的双链 [[link]]
    content = re.sub(r'\[\[([^|\]]+)\]\]', r'\1', content)

    # 5. 清理多余的空行（由于删除嵌入内容可能产生）
    content = re.sub(r'\n\s*\n\s*\n', r'\n\n', content)

    # 6. 清理行首行尾的空白
    lines = content.split('\n')
    cleaned_lines = [line.rstrip() for line in lines]
    content = '\n'.join(cleaned_lines)

    return content


def load_markdown_file(file_path):
    """
    使用frontmatter库加载Markdown文件
    返回: frontmatter.Post对象
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        post = frontmatter.load(f)
    return post

def filter_not_plan_article(post, filename=None):
    """
    判断是否是需要跳过的文章
    跳过条件:
    1. 如果是 INDEX 文件
    2. 包含特定标签: SENSITIVE_TAGS
    3. 不存在指定 title
    """
    if filename is not None and filename.lower() == 'index.md':
        return True

    title = post.get('title', '')
    if not title or not isinstance(title, str) or title.strip() == '':
        return True

    tags = post.get('tags', [])
    if not tags:
        return False

    # tags可能是字符串或列表
    if isinstance(tags, str):
        tags = [tags]
    elif not isinstance(tags, list):
        return False
    tags_lower = {str(tag).lower() for tag in tags}

    # 集合交集:判断是否有交集。
    return bool(SENSITIVE_TAGS & tags_lower)

def convert_to_traditional(text):
    """
    将简体中文转换为繁体中文
    """
    # 创建简体到繁体的转换器
    converter = opencc.OpenCC('s2t')  # s2t: Simplified to Traditional
    return converter.convert(text)

def process_markdown_file(input_path, filename, output_dir):
    """
    处理单个Markdown文件
    """
    try:
        # 使用frontmatter库加载文件
        post = load_markdown_file(input_path)
        
        # 检查是否有draft标签
        # if filter_not_plan_article(post, filename):
        #     print(f"跳过文件: {input_path}")
        #     return
        
        # 获取纯内容（不包含front matter）
        content_without_front_matter = post.content

        # 处理Obsidian特有的双链语法
        content_format_without_wikilink = process_obsidian_content(content_without_front_matter)

        # 转换为繁体中文
        traditional_content = convert_to_traditional(content_format_without_wikilink)

        # 准备输出文件路径
        output_path = os.path.join(output_dir, filename + '.md')

        # 写入输出文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(traditional_content)
        
        print(f"处理完成: {input_path} -> {output_path}")
        
    except Exception as e:
        print(f"处理文件 {input_path} 时出错: {str(e)}")

def show_file_metadata(input_path):
    """
    显示文件的front matter信息（调试用）
    """
    try:
        post = load_markdown_file(input_path)
        print(f"\n文件: {input_path}")
        print(f"Front Matter 属性:")
        for key, value in post.metadata.items():
            print(f"  {key}: {value}")
        print(f"内容长度: {len(post.content)} 字符")
    except Exception as e:
        print(f"读取文件 {input_path} 的metadata时出错: {str(e)}")

def main():
    # 设置命令行参数
    parser = argparse.ArgumentParser(description='将Markdown文件从简体中文转换为繁体中文')
    parser.add_argument('--folder', required=True, help='要处理的文件夹路径')
    parser.add_argument('--out', required=True, help='输出文件夹路径')
    parser.add_argument('--debug', action='store_true', help='显示文件的front matter信息')
    
    args = parser.parse_args()
    
    # 检查输入文件夹是否存在
    if not os.path.exists(args.folder):
        print(f"错误: 输入文件夹 '{args.folder}' 不存在")
        return
    
    if not os.path.isdir(args.folder):
        print(f"错误: '{args.folder}' 不是一个文件夹")
        return
    
    # 创建输出文件夹（如果不存在）
    try:
        Path(args.out).mkdir(parents=True, exist_ok=True)
        print(f"输出文件夹: {args.out}")
    except Exception as e:
        print(f"错误: 无法创建输出文件夹 '{args.out}': {str(e)}")
        return
    
    # 查找所有Markdown文件
    markdown_patterns = [
        os.path.join(args.folder, '*.md'),
        os.path.join(args.folder, '*.markdown'),
        os.path.join(args.folder, '**', '*.md'),
        os.path.join(args.folder, '**', '*.markdown')
    ]
    
    markdown_files = []
    for pattern in markdown_patterns:
        markdown_files.extend(glob.glob(pattern, recursive=True))
    
    # 去重
    markdown_files = list(set(markdown_files))
    
    if not markdown_files:
        print(f"在文件夹 '{args.folder}' 中没有找到Markdown文件")
        return
    
    print(f"找到 {len(markdown_files)} 个Markdown文件")
    
    # 如果开启debug模式，显示所有文件的metadata
    if args.debug:
        print("\n=== DEBUG模式: 显示所有文件的Front Matter ===")
        for file_path in markdown_files:
            show_file_metadata(file_path)
        print("\n=== DEBUG模式结束 ===")
    
    # 处理每个文件
    processed_count = 0
    skipped_count = 0
    
    for file_path in markdown_files:
        try:
            post = load_markdown_file(file_path)
            if filter_not_plan_article(post, os.path.basename(file_path)):
                skipped_count += 1
                print(f"跳过文件: {file_path}")
                continue
            # 提取文章标题
            filename = post.get('title', os.path.basename(file_path))
            process_markdown_file(file_path, filename, args.out)
            processed_count += 1
            
        except Exception as e:
            print(f"处理文件 {file_path} 时出错: {str(e)}")
    
    print(f"\n处理完成!")
    print(f"成功处理: {processed_count} 个文件")
    print(f"跳过: {skipped_count} 个文件")
    print(f"总文件数: {len(markdown_files)} 个文件")

if __name__ == '__main__':
    main()