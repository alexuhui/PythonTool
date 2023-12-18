# git 工具，忽略某路径本地修改

import os
import argparse

# 创建ArgumentParser对象
parser = argparse.ArgumentParser(description='git tool，ignore local modify')

# 添加命令行参数
parser.add_argument('pathname', type=str, help='path/filename to ignore')
parser.add_argument('-i', dest='ignore', action='store_true', help='ignore')
parser.add_argument('-u', dest='recheck', action='store_true', help='recheck')
parser.add_argument('-s', dest='search', action='store_true', help='search skip files')

# 解析命令行参数
args = parser.parse_args()

# 设置目录
directory = "./"
pathname = args.pathname
ignore = args.ignore
recheck = args.recheck
search = args.search

getpath = False
def ignoreFile(directory):
    if search:
        os.system(f"git ls-files -v | grep -i ^S")
    else:
        # 遍历目录中的所有文件
        for filename in os.listdir(directory):
            # file_path = os.path.join(directory, filename)
            # print(f'file_path : {file_path}   filename : {filename}   pathname : {pathname}' )
            # if file_path == pathname :
            if filename == os.path.basename(pathname) :
                global getpath
                getpath = True
                if ignore :
                    os.system(f'git update-index --skip-worktree {pathname}')
                else: 
                    if recheck:
                        os.system(f'git update-index --no-skip-worktree {pathname}')
                    else:
                        print(f"please input operation args")

        if not getpath :
            print(f"can not find dir or file : {pathname}")

ignoreFile(directory)
