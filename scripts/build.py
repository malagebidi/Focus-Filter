import os
import datetime
import pytz

SOURCE_DIR = 'filters'
OUTPUT_FILE = 'filter.txt'

def main():
    # 1. 准备头部
    tz = pytz.timezone('Asia/Shanghai')
    time_str = datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    
    content = []
    content.append(f"! Title: Focus Filter")
    content.append(f"! Version: {time_str}") # 使用时间作为版本号最简单
    content.append(f"! Last modified: {time_str}")
    content.append(f"! Expires: 24 hours")
    content.append(f"! Homepage: https://github.com/malagebidi/Focus-Filter")
    content.append(f"!")
    content.append(f"")

    # 2. 获取所有文件并排序 (A-Z)
    files = sorted([f for f in os.listdir(SOURCE_DIR) if f.endswith('.txt')])

    # 3. 遍历写入
    for filename in files:
        filepath = os.path.join(SOURCE_DIR, filename)
        
        # 使用文件名作为标题 (去掉 .txt)
        domain_name = filename.replace('.txt', '')
        
        # 写入分隔注释，让最终文件可读性变强
        content.append(f"! -------------------------------------------------")
        content.append(f"! {domain_name}") 
        content.append(f"! -------------------------------------------------")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # 忽略原来的日期注释和标题注释，只留规则
                if line and not line.startswith('! '): 
                    content.append(line)
        
        content.append("") # 每个网站之间空一行

    # 4. 写入结果
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(content))

if __name__ == "__main__":
    main()
