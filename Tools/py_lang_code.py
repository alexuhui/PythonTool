# -------------
# 查询国家/语言简码
# 需要安装 label 库，  pip install babel
# -------------

import os
import argparse
from babel import Locale

# 创建ArgumentParser对象
parser = argparse.ArgumentParser(description='查询国家/语言简码工具')

# 添加命令行参数
parser.add_argument('-f', dest='find', help='input keyword to find, otherwise out all language code')
parser.add_argument('-p', dest='perfect', action='store_true', help='perfect match')

# 解析命令行参数
args = parser.parse_args()
print ("==============================================")
print ("args:",args)
find = args.find
perfect = args.perfect

# 设置语言为中文
chinese_locale = Locale('zh')


def find_code():
    # 获取所有国家/地区代码和名称
    all_territories = chinese_locale.territories
    # 获取所有语言代码和名称
    all_languages = chinese_locale.languages

    print ("==============================================")
    for code, name in all_territories.items():
        if not find or (not perfect and (code.find(find) != -1 or name.find(find) != -1)) or (code == find or name == find):
            print(f"^^^^ 国家/地区 : {name}, Code: {code}")

    for code, name in all_languages.items():
        if not find or (not perfect and (code.find(find) != -1 or name.find(find) != -1)) or (code == find or name == find):
            print(f"语言: {name}, Code: {code}")
        

find_code()


