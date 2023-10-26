# 移除文件名前缀

import os
import argparse

# 创建ArgumentParser对象
parser = argparse.ArgumentParser(description='Description of your script.')

# 添加命令行参数
parser.add_argument('arg1', type=str, help='prefix string')

# 解析命令行参数
args = parser.parse_args()

# 设置目录和前缀
prefix = args.arg1#"stu_gameUI_"
directory = "./"


def remove_prefix(file_path, prefix):
    # 获取文件名和扩展名，这个函数获取的文件名会带路径
    _filename, file_extension = os.path.splitext(file_path)
    # 使用os.path.basename获取文件名
    filename = os.path.basename(file_path)
    # print('file_path : ', file_path, filename,filename.startswith(prefix))
    # 检查文件名是否以指定前缀开头
    if filename.startswith(prefix):
        # 构建新的文件名
        new_filename = filename[len(prefix):] #+ file_extension

        # 构建新的完整路径
        new_path = os.path.join(os.path.dirname(file_path), new_filename)

        # 重命名文件
        os.rename(file_path, new_path)
        print(f"重命名文件: {file_path} ---------------> {new_path}")

def batch_remove_prefix(directory, prefix):
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # 检查是否为文件而不是子目录
        if os.path.isfile(file_path):
            remove_prefix(file_path, prefix)

# 执行批量重命名
batch_remove_prefix(directory, prefix)
