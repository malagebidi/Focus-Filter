import os
import datetime
import pytz # 如果需要特定时区，或者直接用 UTC

# 配置
SOURCE_DIR = 'filters'
OUTPUT_FILE = 'filter.txt'

# 头部信息模板 (AdBlock 格式)
HEADER_TEMPLATE = """! Title: Focus Filter
! Description: 个人自用过滤规则，专注于中文互联网内容的净化
! Homepage: https://github.com/malagebidi/Focus-Filter
! Last modified: {timestamp}
! Expires: 24 hours (update frequency)
!
"""

def main():
    rules = set() # 使用 set 自动去重
    
    # 1. 遍历读取所有规则文件
    if not os.path.exists(SOURCE_DIR):
        print(f"Error: Directory {SOURCE_DIR} not found.")
        return

    for filename in os.listdir(SOURCE_DIR):
        if filename.endswith(".txt"):
            filepath = os.path.join(SOURCE_DIR, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                print(f"Reading {filename}...")
                for line in f:
                    line = line.strip()
                    # 跳过空行和以 ! 开头的注释行（也可以选择保留注释）
                    if line and not line.startswith('!'):
                        rules.add(line)

    # 2. 排序规则 (为了 Git Diff 好看，建议排序)
    sorted_rules = sorted(list(rules))

    # 3. 生成时间戳
    # 建议使用 UTC 时间或北京时间
    tz = pytz.timezone('Asia/Shanghai')
    current_time = datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S %Z')

    # 4. 写入最终文件
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(HEADER_TEMPLATE.format(timestamp=current_time))
        for rule in sorted_rules:
            f.write(rule + '\n')
            
    print(f"Success! Merged {len(sorted_rules)} rules into {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
