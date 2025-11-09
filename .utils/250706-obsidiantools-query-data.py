# https://github.com/mfarragher/obsidiantools
#!/usr/bin/env python3
"""
Obsidian GTD Todo 标签查询脚本
使用 obsidiantools 查询所有包含 #gtd/todo 标签的页面
"""

import os
import traceback
from pathlib import Path
# from obsidiantools.api import Vault
import obsidiantools.api as otools

def find_gtd_todo_pages(vault_path: str, tag: str = "#gtd/todo") -> list:
    """
    在 Obsidian 库中查找包含指定标签的所有页面

    Args:
        vault_path: Obsidian 库的路径
        tag: 要搜索的标签，默认为 "#gtd/todo"

    Returns:
        包含标签的页面列表
    """
    vault = otools.Vault(vault_path).connect().gather()
    # 初始化 Vault 对象，并连接和收集数据
    # vault = Vault(vault_path).connect().gather()
    print('连接数据库完成')
    # 存储匹配的页面
    matching_pages = []

    # 获取所有笔记的元数据
    notes_df = vault.get_note_metadata()
    # notes_df = vault.get_all_file_metadata()

    # 遍历所有笔记
    for note_path in notes_df.index:
        try:
            # 获取笔记的源文本
            source_text = vault.get_source_text(note_path)

            # 检查是否包含目标标签
            if tag in source_text:
                # 获取笔记标题（去掉 .md 扩展名）
                title = Path(note_path).stem

                # 获取笔记的标签
                note_tags = vault.get_tags(note_path)

                matching_pages.append({
                    'title': title,
                    'path': note_path,
                    'full_path': os.path.join(vault_path, note_path),
                    'tags': note_tags,
                    'backlinks_count': notes_df.loc[note_path, 'n_backlinks'],
                    'wikilinks_count': notes_df.loc[note_path, 'n_wikilinks']
                })

        except Exception as e:
            print(f"读取笔记 {note_path} 时出错: {e}")

    return matching_pages


def display_results(pages: list, tag: str = "#gtd/todo"):
    """
    显示查询结果

    Args:
        pages: 包含标签的页面列表
        tag: 搜索的标签
    """
    if not pages:
        print(f"未找到包含 {tag} 标签的页面")
        return

    print(f"找到 {len(pages)} 个包含 {tag} 标签的页面:\n")
    print("-" * 80)

    for i, page in enumerate(pages, 1):
        print(f"{i}. 📝 {page['title']}")
        print(f"   📁 路径: {page['path']}")
        print(f"   🔗 反链数: {page['backlinks_count']}")
        print(f"   📎 Wiki链接数: {page['wikilinks_count']}")
        if page['tags']:
            print(f"   🏷️  所有标签: {', '.join(page['tags'])}")
        print(f"   📂 完整路径: {page['full_path']}")
        print("-" * 80)


def get_tag_statistics(vault_path: str, tag: str = "#gtd/todo") -> dict:
    """
    获取标签统计信息

    Args:
        vault_path: Obsidian 库的路径
        tag: 要统计的标签

    Returns:
        标签统计信息
    """
    # 初始化 Vault 对象，并连接和收集数据
    vault = Vault(vault_path).connect().gather()

    stats = {
        'total_files': 0,
        'files_with_tag': 0,
        'tag_count': 0
    }

    # 获取所有笔记的元数据
    notes_df = vault.get_note_metadata()
    stats['total_files'] = len(notes_df)

    # 遍历所有笔记
    for note_path in notes_df.index:
        try:
            # 获取笔记的源文本
            source_text = vault.get_source_text(note_path)

            if tag in source_text:
                stats['files_with_tag'] += 1
                # 计算标签出现次数
                stats['tag_count'] += source_text.count(tag)

        except Exception as e:
            print(f"读取笔记 {note_path} 时出错: {e}")

    return stats


def main():
    """主函数"""
    # 设置你的 Obsidian 库路径
    vault_path = '/Users/bgzo/Library/Mobile Documents/iCloud~md~obsidian/Documents/vault/how-to'
    # input("请输入 Obsidian 库的路径: ").strip()

    # 验证路径是否存在
    if not os.path.exists(vault_path):
        print(f"错误: 路径 {vault_path} 不存在")
        return

    # 设置要搜索的标签
    # tag = input("请输入要搜索的标签 (默认: #gtd/todo): ").strip()
    # if not tag:
    tag = "#gtd/todo"

    print(f"\n正在搜索包含 {tag} 的页面...")

    try:
        # 查找包含标签的页面
        pages = find_gtd_todo_pages(vault_path, tag)

        # 显示结果
        display_results(pages, tag)

        # 显示统计信息
        print(f"\n统计信息:")
        stats = get_tag_statistics(vault_path, tag)
        print(f"总文件数: {stats['total_files']}")
        print(f"包含标签的文件数: {stats['files_with_tag']}")
        print(f"标签总出现次数: {stats['tag_count']}")

        # 可选：保存结果到文件
        save_option = input("\n是否保存结果到文件? (y/n): ").strip().lower()
        if save_option == 'y':
            save_results_to_file(pages, tag, vault_path)

    except Exception as e:
        print(f"查询过程中出错: {e}")
        traceback.print_exc()


def save_results_to_file(pages: list, tag: str, vault_path: str):
    """
    保存查询结果到文件

    Args:
        pages: 页面列表
        tag: 搜索的标签
        vault_path: 库路径
    """
    try:
        output_file = f"gtd_todo_results_{tag.replace('#', '').replace('/', '_')}.txt"

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"Obsidian GTD Todo 查询结果\n")
            f.write(f"库路径: {vault_path}\n")
            f.write(f"搜索标签: {tag}\n")
            f.write(f"查询时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"找到 {len(pages)} 个匹配页面\n\n")
            f.write("-" * 60 + "\n")

            for i, page in enumerate(pages, 1):
                f.write(f"{i}. {page['title']}\n")
                f.write(f"   路径: {page['path']}\n")
                f.write(f"   完整路径: {page['full_path']}\n")
                f.write("-" * 60 + "\n")

        print(f"结果已保存到: {output_file}")

    except Exception as e:
        print(f"保存文件时出错: {e}")


if __name__ == "__main__":
    from datetime import datetime

    main()