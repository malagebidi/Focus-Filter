import os
import datetime
import pytz
import subprocess
import hashlib
import base64
import re

# 配置部分
SOURCE_DIR = 'filters'
OUTPUT_FILE_BASIC = 'filter.txt'      # 基础版文件名
OUTPUT_FILE_ZEN = 'filter_zen.txt'    # 完整版文件名 (包含 ZEN)
SEPARATOR_KEYWORD = "---ZEN---"       # 用于识别的关键字 (去除空格后)

def get_version_from_git():
    """
    根据 Git 提交总数计算版本号。
    """
    try:
        output = subprocess.check_output(
            ['git', 'rev-list', '--count', 'HEAD', '--', 'filters', 'scripts']
        ).decode().strip()
        total_commits = int(output)
    except Exception as e:
        print(f"Warning: Could not get git commit count: {e}. Using default version.")
        total_commits = 0

    z = total_commits % 100
    y = (total_commits // 100) % 100
    x = total_commits // 10000
    
    return f"2.{x}.{y}.{z}"

def calculate_checksum(lines):
    content = '\n'.join([line for line in lines if not line.startswith('! Checksum:')])
    content += '\n' 
    
    md5 = hashlib.md5(content.encode('utf-8')).digest()
    checksum = base64.b64encode(md5).decode('utf-8').rstrip('=')
    return checksum

def write_rules_to_file(filename, rules, title_suffix, version, current_time):
    title = "Focus Filter"
    if title_suffix:
        title += f" {title_suffix}"

    sorted_rules = sorted(list(rules))
    
    # 1. 先准备除去 Checksum 的头部
    header_lines = [
        "[Adblock Plus 2.0]",
        f"! Version: {version}",
        f"! Title: {title}",
        "! Description: A Focus Filter for AdGuard that remove recommended feeds, distracting elements, and \"doom-scrolling\" traps from various websites.",
        f"! Last modified: {current_time}",
        "! Expires: 2 days (update frequency)",
        "! Homepage: https://github.com/malagebidi/Focus-Filter",
        "! License: https://github.com/malagebidi/Focus-Filter/blob/main/LICENSE",
        "!" 
    ]
    
    # 2. 组合所有内容用于计算 Checksum
    all_content_lines = header_lines + sorted_rules
    
    # 3. 计算 Checksum
    checksum = calculate_checksum(all_content_lines)
    
    # 4. 将 Checksum 插入到头部）
    header_lines.insert(1, f"! Checksum: {checksum}")

    # 5. 写入文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(header_lines) + '\n')
        f.write('\n'.join(sorted_rules))
        f.write('\n')
    
    print(f"Build success: {filename} (Checksum: {checksum})")

def main():
    # 1. 获取版本号
    version = get_version_from_git()
    print(f"Generated Version: {version}")

    # 2. 将版本号传递给 GitHub Actions
    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"version={version}\n")
    
    # 3. 获取时间戳
    tz = pytz.timezone('Asia/Shanghai')
    current_time = datetime.datetime.now(tz).isoformat(timespec='seconds')
    
    # 4. 初始化规则集合
    basic_rules = set() # 基础规则 (不含 ZEN)
    all_rules = set()   # 所有规则 (含 ZEN)

    # 5. 读取并分类规则
    if os.path.exists(SOURCE_DIR):
        for filename in os.listdir(SOURCE_DIR):
            if filename.endswith(".txt"):
                filepath = os.path.join(SOURCE_DIR, filename)
                
                # 重置状态：新文件开始时，默认不是 ZEN 模式
                is_zen_mode = False 
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        
                        # 优化后的分隔符检测：
                        # 去除所有空格并将字符转大写，匹配 "!---ZEN---"
                        # 这样即使你写成 "! --- zen ---" 或 "! - - - ZEN - - -" 也能识别
                        clean_line = line.replace(" ", "").upper()
                        if f"!{SEPARATOR_KEYWORD}" in clean_line:
                            is_zen_mode = True
                            continue # 跳过分隔符这一行

                        # 跳过空行和普通注释 (分隔符已被上面处理)
                        if not line or line.startswith('!'):
                            continue
                        
                        # 逻辑核心：
                        # A. 任何有效规则都加入 all_rules (用于 filter_zen.txt)
                        all_rules.add(line)
                        
                        # B. 只有非 ZEN 模式下的规则，才加入 basic_rules (用于 filter.txt)
                        if not is_zen_mode:
                            basic_rules.add(line)
    else:
        print(f"Error: Directory '{SOURCE_DIR}' not found.")
        return

    # 6. 生成文件
    
    # 生成 filter.txt (仅基础规则)
    write_rules_to_file(OUTPUT_FILE_BASIC, basic_rules, "", version, current_time)

    # 生成 filter_zen.txt (包含所有规则) -> 这里确保了文件会被创建
    write_rules_to_file(OUTPUT_FILE_ZEN, all_rules, "(ZEN Mode)", version, current_time)

if __name__ == "__main__":
    main()
