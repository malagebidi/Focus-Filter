import os
import datetime
import pytz

SOURCE_DIR = 'filters'
OUTPUT_FILE = 'filter.txt'

HEADER_TEMPLATE = """! Title: Focus Filter
! Description: A Focus Filter for AdGuard that remove recommended feeds, distracting elements, and "doom-scrolling" traps from various websites.
! Homepage: https://github.com/malagebidi/Focus-Filter
! License: https://github.com/malagebidi/Focus-Filter/blob/main/LICENSE
! Last modified: {timestamp}
! Expires: 24 hours (update frequency)
!
"""

def main():
    rules = set()
    
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
                    if line and not line.startswith('!'):
                        rules.add(line)

    sorted_rules = sorted(list(rules))

    tz = pytz.timezone('Asia/Shanghai')
    current_time = datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S %Z')

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(HEADER_TEMPLATE.format(timestamp=current_time))
        for rule in sorted_rules:
            f.write(rule + '\n')
            
    print(f"Success! Merged {len(sorted_rules)} rules into {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
