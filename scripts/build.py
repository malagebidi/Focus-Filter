import os
import datetime
import pytz
import subprocess

SOURCE_DIR = 'filters'
OUTPUT_FILE = 'filter.txt'

def get_version_from_git():
    """
    根据 Git 提交总数计算版本号。
    只计算 filters 目录和 scripts 目录的变动。
    格式: 2.X.Y.Z
    """
    try:
        # 修改点：指定统计路径，排除干扰
        output = subprocess.check_output(
            ['git', 'rev-list', '--count', 'HEAD', '--', 'filters', 'scripts']
        ).decode().strip()
        total_commits = int(output)
    except Exception as e:
        print(f"Warning: Could not get git commit count: {e}. Using default version.")
        total_commits = 0

    # 进位逻辑 (Base 100)
    z = total_commits % 100
    y = (total_commits // 100) % 100
    x = total_commits // 10000
    
    return f"2.{x}.{y}.{z}"

def main():
    # 1. 计算动态版本号
    version = get_version_from_git()
    print(f"Generated Version: {version}")

    # 2. 准备时间戳
    tz = pytz.timezone('Asia/Shanghai')
    current_time = datetime.datetime.now(tz).isoformat(timespec='seconds')
    
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
