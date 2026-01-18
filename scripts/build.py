import os
import datetime
import pytz

SOURCE_DIR = 'filters'
OUTPUT_FILE = 'filter.txt'

def main():
    # 1. 准备头部信息 (这是给 AdGuard 识别用的，必须保留)
    tz = pytz.timezone('Asia/Shanghai')
    current_time = datetime.datetime.now(tz).isoformat(timespec='seconds')
    
    header = [
        "! Title: Focus Filter",
        "! Description: A Focus Filter for AdGuard that remove recommended feeds, distracting elements, and \"doom-scrolling\" traps from various websites.",
        f"! Last modified: {current_time}",
        "! Version: 0.0.4.5",
        "! Expires: 24 hours",
        "! Homepage: https://github.com/malagebidi/Focus-Filter",
        "! License: https://github.com/malagebidi/Focus-Filter/blob/main/LICENSE",
        "!"
    ]

    # 2. 读取所有规则并收集到一个集合中 (Set)
    rules = set()
    
    if os.path.exists(SOURCE_DIR):
        for filename in os.listdir(SOURCE_DIR):
            if filename.endswith(".txt"):
                filepath = os.path.join(SOURCE_DIR, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        # 核心逻辑：
                        # 1. 跳过空行
                        # 2. 跳过以 ! 开头的注释行 (彻底删除源文件里的注释)
                        if line and not line.startswith('!'):
                            rules.add(line)

    # 3. 排序 (关键！为了 Git Diff 稳定，必须排序)
    sorted_rules = sorted(list(rules))

    # 4. 写入文件
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        # 先写头部
        f.write('\n'.join(header) + '\n')
        # 再写规则
        f.write('\n'.join(sorted_rules))
        f.write('\n') # 文件末尾留一个空行是好习惯

    print(f"Build complete: {len(sorted_rules)} rules merged.")

if __name__ == "__main__":
    main()
