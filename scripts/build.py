import os
import datetime
import pytz
import subprocess

SOURCE_DIR = 'filters'
OUTPUT_FILE = 'filter.txt'

def get_version_from_git():
    """
    根据 Git 提交总数计算版本号。
    格式: 2.X.Y.Z
    机制: Z 满 100 进 Y，Y 满 100 进 X。
    """
    try:
        # 获取 Git 提交总数
        # rev-list --count HEAD 会返回当前分支的提交数量
        count_str = subprocess.check_output(['git', 'rev-list', '--count', 'HEAD']).decode().strip()
        total_commits = int(count_str)
    except Exception:
        # 如果本地没有 git 环境或报错，回退到默认值
        print("Warning: Could not get git commit count. Using default version.")
        total_commits = 0

    # 进位逻辑 (Base 100)
    z = total_commits % 100
    y = (total_commits // 100) % 100
    x = total_commits // 10000
    
    # 第一位固定为 2
    return f"2.{x}.{y}.{z}"

def main():
    # 1. 计算动态版本号
    version = get_version_from_git()
    print(f"Generated Version: {version}")

    # 2. 准备时间戳 (ISO 8601 格式)
    tz = pytz.timezone('Asia/Shanghai')
    current_time = datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    
    header = [
        "! Title: Focus Filter",
        "! Description: A Focus Filter for AdGuard that remove recommended feeds, distracting elements, and \"doom-scrolling\" traps from various websites.",
        f"! Last modified: {current_time}",
        f"! Version: {version}",
        "! Expires: 24 hours",
        "! Homepage: https://github.com/malagebidi/Focus-Filter",
        "! License: https://github.com/malagebidi/Focus-Filter/blob/main/LICENSE",
        "!"
    ]

    # 3. 读取并处理规则
    rules = set()
    if os.path.exists(SOURCE_DIR):
        for filename in os.listdir(SOURCE_DIR):
            if filename.endswith(".txt"):
                filepath = os.path.join(SOURCE_DIR, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('!'):
                            rules.add(line)

    # 4. 排序
    sorted_rules = sorted(list(rules))

    # 5. 写入文件
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(header) + '\n')
        f.write('\n'.join(sorted_rules))
        f.write('\n')

    print(f"Build complete: {len(sorted_rules)} rules merged into {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
