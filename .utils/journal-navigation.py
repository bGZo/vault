import os
import re
from datetime import datetime

# 配置参数
JOURNAL_DIR = '/Users/bgzo/Library/Mobile Documents/iCloud~md~obsidian/Documents/wiki/journals/'
JOURNAL_DIR = JOURNAL_DIR + "2019"  # 日记目录
FILE_EXT = ".md"  # 日记文件扩展名
NAV_PATTERN = re.compile(  # 导航栏正则模式
    r'^<< \[\[.*\]\] \| \[\[.*\]\] \| \[\[.*\]\] >>\n?',
    flags=re.MULTILINE
)


def get_valid_journal_entries():
    """获取所有有效的日记条目（按日期排序）"""
    entries = []

    for filename in os.listdir(JOURNAL_DIR):
        # 去除扩展名并验证基本格式
        basename = os.path.splitext(filename)[0]
        if len(basename) != 8 or not basename.isdigit():
            continue

        # 验证日期有效性
        try:
            date = datetime.strptime(basename, "%Y%m%d").date()
            entries.append((basename, date))
        except ValueError:
            continue

    # 按日期排序
    return sorted(entries, key=lambda x: x[1])


def process_journals(sorted_entries):
    """处理所有日记文件"""
    sorted_files = [entry[0] for entry in sorted_entries]

    for idx, (basename, _) in enumerate(sorted_entries):
        # 获取相邻文件
        prev_file = sorted_files[idx - 1] if idx > 0 else None
        next_file = sorted_files[idx + 1] if idx < len(sorted_files) - 1 else None

        # 构建导航栏
        year = basename[:4]
        nav_line = generate_nav_line(prev_file, year, next_file)

        # 更新文件内容
        file_path = os.path.join(JOURNAL_DIR, f"{basename}{FILE_EXT}")
        update_file_content(file_path, nav_line)


def generate_nav_line(prev_file, year, next_file):
    """生成导航栏字符串"""
    prev_link = f"[[journals/{year}/{prev_file}|Prev]]" if prev_file else f"[[journals/{year}/index|Prev]]"
    year_link = f"[[journals/{year}/index|{year}]]"
    next_link = f"[[journals/{year}/{next_file}|Next]]" if next_file else f"[[journals/{year}/index|Next]]"

    return f"<< {prev_link} | {year_link} | {next_link} >>\n\n"


def update_file_content(file_path, nav_line):
    """更新文件内容（保留元数据）"""
    try:
        with open(file_path, "r+", encoding="utf-8") as f:
            content = f.read()

            # 移除旧导航栏
            new_content = NAV_PATTERN.sub("", content)

            # 处理YAML front matter
            if new_content.startswith("---\n"):
                end_yaml = new_content.find("\n---", 4)
                if end_yaml != -1:
                    yaml_block = new_content[:end_yaml + 4]
                    rest_content = new_content[end_yaml + 4:].lstrip()
                    new_content = yaml_block + "\n\n" + nav_line + rest_content
                else:
                    new_content = nav_line + new_content
            else:
                new_content = nav_line + new_content.lstrip()

            # 写入更新内容
            f.seek(0)
            f.write(new_content)
            f.truncate()
    except FileNotFoundError:
        print(f"警告：文件 {file_path} 不存在，已跳过")


if __name__ == "__main__":
    sorted_entries = get_valid_journal_entries()
    process_journals(sorted_entries)
    print(f"成功更新 {len(sorted_entries)} 篇日记的导航栏")