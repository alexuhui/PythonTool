# 当前目录下所有文夹下新建文件夹

import os
import argparse
import shutil
import re

# 创建ArgumentParser对象
parser = argparse.ArgumentParser(description='Description of your script.')

# 添加命令行参数，统一的文件名
parser.add_argument('pattern', type=str, help='pattern to search file')
parser.add_argument('newFolderName', type=str, help='new folder name for all directory')
parser.add_argument('-r', dest='useRe', action='store_true', help='use regular expression, default is false')
parser.add_argument('-y', dest='yes', action='store_true', help='Real execution operation, default is false means preview changes.')

# 解析命令行参数
args = parser.parse_args()
print ("args:",args)
pattern = args.pattern
newFolderName = args.newFolderName
useRe = args.useRe
execution = args.yes

def organize_files():
    # 获取当前工作目录
    current_directory = os.getcwd()

    # 遍历当前目录下的所有文件
    for filename in os.listdir(current_directory):
        if not os.path.isfile(filename):
            # 检查文件名匹配
            if useRe: 
                match = re.compile(pattern).match(filename)
            else:
                match = pattern in filename

            if match:
                # 构建新的文件夹名
                if useRe: 
                    folder_name = re.sub(pattern, newFolderName, filename)
                else:
                    folder_name = newFolderName

                # 创建同名文件夹
                newFolderPath = os.path.join(filename, folder_name)
                if execution:
                    os.makedirs(newFolderPath, exist_ok=True)
                
                if execution:
                    print("new directory execution:", newFolderPath)
                else:
                    print("new directory preview:", newFolderPath)

if __name__ == "__main__":
    organize_files()
