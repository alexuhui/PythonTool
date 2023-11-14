# 修改文件名， 移除文件名前缀

import os
import argparse

# 创建ArgumentParser对象
parser = argparse.ArgumentParser(description='Description of your script.')

# 添加命令行参数
parser.add_argument('arg1', type=str, help='prefix string of file name to delete')
parser.add_argument('-y', dest='yes', action='store_true', help='Real execution operation, default is false means preview changes.')

# 解析命令行参数
args = parser.parse_args()
execution = args.yes

# 设置目录和前缀
prefix = args.arg1
directory = "./"


def remove_file(file_path, prefix):
    # 获取文件名和扩展名，这个函数获取的文件名会带路径
    _filename, file_extension = os.path.splitext(file_path)
    # 使用os.path.basename获取文件名
    filename = os.path.basename(file_path)
    # print('file_path : ', file_path, filename,filename.startswith(prefix))
    # 检查文件名是否以指定前缀开头
    if filename.startswith(prefix):
        # 刪除文件
        if execution:
            os.remove(file_path)

        if execution:
            print(f"delete execution: --------->  {file_path} ")
        else:
            print(f"delete preview: ----------> {file_path}")

def batch_remove_file(directory, prefix):
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # 检查是否为文件而不是子目录
        if os.path.isfile(file_path):
            remove_file(file_path, prefix)
        else:
            batch_remove_file(file_path, prefix)

# 执行批量重命名
batch_remove_file(directory, prefix)
