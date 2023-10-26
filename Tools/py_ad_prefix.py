# 文件名添加前缀

import os
import argparse

# 创建ArgumentParser对象
parser = argparse.ArgumentParser(description='Description of your script.')

# 添加命令行参数
parser.add_argument('arg1', type=str, help='prefix string')
parser.add_argument('arg2', type=str, help='[all] add prefix to all file, even if the file already has the prefix')

# 解析命令行参数
args = parser.parse_args()

# 设置目录和前缀
prefix = args.arg1
directory = "./"
isAll = args.arg2.casefold() == "all" 

def add_prefix(file_path):
    # 获取文件名和扩展名，这个函数获取的文件名会带路径
    _filename, file_extension = os.path.splitext(file_path)
    # 使用os.path.basename获取文件名包含扩展名
    filename = os.path.basename(file_path)

    # 检查文件名是否以指定前缀开头
    if isAll or not filename.startswith(prefix):
        # 构建新的文件名
        new_filename = prefix + filename
        # 构建新的完整路径
        new_path = os.path.join(os.path.dirname(file_path), new_filename)

        # 重命名文件
        os.rename(file_path, new_path)
        print(f"重命名文件: {file_path} ---------------> {new_path}")

def batch_add_prefix(directory):
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # 检查是否为文件而不是子目录
        if os.path.isfile(file_path):
            add_prefix(file_path)

# 执行批量重命名
batch_add_prefix(directory)
