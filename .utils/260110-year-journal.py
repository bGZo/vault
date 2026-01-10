#!/usr/bin/env python3
# coding: utf-8
# File: .utils/260110-year-journal.py
# Date: 2024-01-10
# Author: bgzo
# Description: 这个脚本用于生成一个年份模板，一次性输出今年的所有周记，用户可以指定输出周记的年份和周记的星期数作为周记日，比如我个人习惯每周六总结过去一周的事情，所以我会指定周记的星期数为6。
# 具体效果如下：
# - W01: [[journals/2026/20260103]]
# - W02: [[journals/2026/20260110]]
# ....
# Usage: python3 .utils/260110-year-journal.py -y <year> -w <week_day> [-d <directory>]
# Example: python3 .utils/260110-year-journal.py -y 2026 -w 6 -d "journals/2026"

import argparse
from datetime import date, timedelta
import sys
import os

def main():
    parser = argparse.ArgumentParser(description="Generate weekly journal index for a year.")
    parser.add_argument("-y", "--year", type=int, required=True, help="Year (e.g. 2026)")
    parser.add_argument("-w", "--weekday", type=int, required=True, help="Weekday 1-7 (1=Monday, 7=Sunday)")
    parser.add_argument("-d", "--dir", type=str, default="", help="Optional directory prefix (e.g. journals/2026)")

    args = parser.parse_args()

    year = args.year
    target_weekday = args.weekday
    directory = args.dir

    if not (1 <= target_weekday <= 7):
        print("Error: Weekday must be between 1 (Monday) and 7 (Sunday).")
        sys.exit(1)

    # Start from Jan 1st of the specified year
    current_date = date(year, 1, 1)

    # Calculate days to add to reach the first target_weekday
    # isoweekday() returns 1 for Monday, 7 for Sunday
    current_weekday = current_date.isoweekday()
    days_ahead = target_weekday - current_weekday
    
    if days_ahead < 0:
        days_ahead += 7

    current_date += timedelta(days=days_ahead)

    week_count = 1
    
    while current_date.year == year:
        date_str = current_date.strftime("%Y%m%d")
        
        if directory:
            # Ensure proper separator if user didn't include it, though os.path.join handles most.
            # However, for wiki links [[path/to/file]], we usually want forward slashes regardless of OS.
            link_path = os.path.join(directory, date_str).replace("\\", "/")
        else:
            link_path = date_str
            
        print(f"- [ ] W{week_count:02d}: [[{link_path}|{date_str}]]")
        
        # Move to next week
        current_date += timedelta(days=7)
        week_count += 1

if __name__ == "__main__":
    main()


