# 以所有文件的文件名新建文件夹，并把文件移动到同名文件夹下。然后，重命名文件

import os
import argparse
import shutil

# 创建ArgumentParser对象
parser = argparse.ArgumentParser(description='Description of your script.')

# 添加命令行参数，统一的文件名
parser.add_argument('pattern', type=str, help='pattern to search file')
parser.add_argument('newFileName', type=str, help='new file name for all file')
parser.add_argument('-r', dest='useRe', action='store_true', help='use regular expression, default is false')
parser.add_argument('-y', dest='yes', action='store_true', help='Real execution operation, default is false means preview changes.')

# 解析命令行参数
args = parser.parse_args()
print ("args:",args)
pattern = args.pattern
newFileName = args.newFileName
useRe = args.useRe
execution = args.yes

def organize_files():
    # 获取当前工作目录
    current_directory = os.getcwd()

    # 遍历当前目录下的所有文件
    for filename in os.listdir(current_directory):
        if os.path.isfile(filename):
            # 检查文件名匹配
            if useRe: 
                match = re.compile(pattern).match(filename)
            else:
                match = pattern in filename

            if match:
                # 获取文件名和扩展名，这个函数获取的文件名会带路径
                _filename, file_extension = os.path.splitext(filename)

                folder_name = os.path.splitext(filename)[0]
                # 创建同名文件夹
                if execution:
                    os.makedirs(folder_name, exist_ok=True)

                # 移动文件到同名文件夹
                if execution:
                    shutil.move(filename, os.path.join(folder_name, filename))

                new_filename = newFileName
                if new_filename == None or new_filename == "":
                    new_filename = f"{folder_name}_{filename}"

                if not (file_extension in new_filename):
                    new_filename += file_extension

                newFilePath = os.path.join(folder_name, new_filename)
                # 重命名文件
                if execution:
                    os.rename(os.path.join(folder_name, filename), newFilePath)
                
                if execution:
                    print("execution:", filename, "------> ", newFilePath)
                else:
                    print("preview:", filename, "------> ", newFilePath)

if __name__ == "__main__":
    organize_files()
