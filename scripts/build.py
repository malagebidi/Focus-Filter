import os
import datetime
import pytz
import subprocess

SOURCE_DIR = 'filters'
OUTPUT_FILE_BASIC = 'filter.txt'
OUTPUT_FILE_ZEN = 'filter_zen.txt'

def get_version_from_git():
    """
    根据 Git 提交总数计算版本号。
    只计算 filters 目录和 scripts 目录的变动。
    格式: 2.X.Y.Z
    """
    try:
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

def write_rules_to_file(filename, rules, title_suffix, version, current_time):
    """
    辅助函数：将规则写入文件
    """
    title = "Focus Filter"
    if title_suffix:
        title += f" {title_suffix}"

    header = [
        f"! Title: {title}",
        "! Description: A Focus Filter for AdGuard that remove recommended feeds, distracting elements, and \"doom-scrolling\" traps from various websites.",
        f"! Last modified: {current_time}",
        f"! Version: {version}",
        "! Expires: 12 hours",
        "! Homepage: https://github.com/malagebidi/Focus-Filter",
        "! License: https://github.com/malagebidi/Focus-Filter/blob/main/LICENSE",
        "!"
    ]

    sorted_rules = sorted(list(rules))

    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(header) + '\n')
        f.write('\n'.join(sorted_rules))
        f.write('\n')
    
    print(f"Build complete: {len(sorted_rules)} rules merged into {filename}")

def main():
    # 1. 计算动态版本号
    version = get_version_from_git()
    print(f"Generated Version: {version}")

    # 2. 准备时间戳
    tz = pytz.timezone('Asia/Shanghai')
    current_time = datetime.datetime.now(tz).isoformat(timespec='seconds')
    
    # 3. 读取并处理规则
    basic_rules = set() # 仅存放基本规则
    all_rules = set()   # 存放基本 + Zen 规则

    if os.path.exists(SOURCE_DIR):
        for filename in os.listdir(SOURCE_DIR):
            if filename.endswith(".txt"):
                filepath = os.path.join(SOURCE_DIR, filename)
                
                # 每个文件开始前，重置 Zen 模式标记
                is_zen_mode = False 
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        
                        # 检查是否遇到分隔符
                        # 注意：要在检查 startswith('!') 之前检查这个，因为它也是以 ! 开头的
                        if "! --- ZEN ---" in line:
                            is_zen_mode = True
                            continue

                        # 忽略空行和注释
                        if not line or line.startswith('!'):
                            continue
                        
                        # 逻辑核心：
                        # 1. 无论是否在 Zen 模式，都加入 all_rules (用于 filter_zen.txt)
                        all_rules.add(line)
                        
                        # 2. 只有还没进入 Zen 模式的规则，才加入 basic_rules (用于 filter.txt)
                        if not is_zen_mode:
                            basic_rules.add(line)

    # 4. 写入文件 (调用辅助函数)
    
    # 生成 filter.txt (仅包含基本规则)
    write_rules_to_file(OUTPUT_FILE_BASIC, basic_rules, "", version, current_time)

    # 生成 filter_zen.txt (包含所有规则)
    write_rules_to_file(OUTPUT_FILE_ZEN, all_rules, "(ZEN Mode)", version, current_time)

if __name__ == "__main__":
    main()
