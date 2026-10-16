import os
import datetime
import pytz
import subprocess
import hashlib
import base64

# 配置部分
SOURCE_DIR = 'filters'
OUTPUT_FILE = 'filter.txt'            # 最终规则文件名

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

def write_rules_to_file(filename, rules, version, current_time):
    sorted_rules = sorted(list(rules))

    # 1. 先准备除去 Checksum 的头部
    header_lines = [
        "[Adblock Plus 2.0]",
        f"! Version: {version}",
        "! Title: Focus Filter",
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

    # 4. 将 Checksum 插入到头部
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
    rules = set() # 所有有效规则

    # 5. 读取所有规则
    if os.path.exists(SOURCE_DIR):
        for filename in os.listdir(SOURCE_DIR):
            if filename.endswith(".txt"):
                filepath = os.path.join(SOURCE_DIR, filename)

                with open(filepath, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()

                        # 跳过空行和注释
                        if not line or line.startswith('!'):
                            continue

                        rules.add(line)
    else:
        print(f"Error: Directory '{SOURCE_DIR}' not found.")
        return

    # 6. 生成最终规则文件
    write_rules_to_file(OUTPUT_FILE, rules, version, current_time)

if __name__ == "__main__":
    main()
