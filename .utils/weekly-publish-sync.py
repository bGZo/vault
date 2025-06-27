#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import glob
from pathlib import Path
import opencc
import frontmatter

def load_markdown_file(file_path):
    """
    使用frontmatter库加载Markdown文件
    返回: frontmatter.Post对象
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        post = frontmatter.load(f)
    return post

def has_draft_tag(post):
    """
    检查frontmatter中是否包含draft标签
    post: frontmatter.Post对象
    """
    # 直接通过属性访问metadata
    tags = post.get('tags', [])
    
    if not tags:
        return False
    
    # tags可能是字符串或列表
    if isinstance(tags, str):
        tags = [tags]
    elif not isinstance(tags, list):
        return False
    
    # 检查是否包含draft标签（不区分大小写）
    return any(str(tag).lower() == 'draft' for tag in tags)

def convert_to_traditional(text):
    """
    将简体中文转换为繁体中文
    """
    # 创建简体到繁体的转换器
    converter = opencc.OpenCC('s2t')  # s2t: Simplified to Traditional
    return converter.convert(text)

def process_markdown_file(input_path, output_dir):
    """
    处理单个Markdown文件
    """
    try:
        # 使用frontmatter库加载文件
        post = load_markdown_file(input_path)
        
        # 检查是否有draft标签
        if has_draft_tag(post):
            print(f"跳过草稿文件: {input_path}")
            return
        
        # 获取纯内容（不包含front matter）
        content_without_front_matter = post.content
        
        # 转换为繁体中文
        traditional_content = convert_to_traditional(content_without_front_matter)
        
        # 准备输出文件路径
        filename = os.path.basename(input_path)
        output_path = os.path.join(output_dir, filename)
        
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
            if has_draft_tag(post):
                skipped_count += 1
                print(f"跳过草稿文件: {file_path}")
                continue
            
            process_markdown_file(file_path, args.out)
            processed_count += 1
            
        except Exception as e:
            print(f"处理文件 {file_path} 时出错: {str(e)}")
    
    print(f"\n处理完成!")
    print(f"成功处理: {processed_count} 个文件")
    print(f"跳过草稿: {skipped_count} 个文件")
    print(f"总文件数: {len(markdown_files)} 个文件")

if __name__ == '__main__':
    main()