# 批量重命名

import os
import argparse
import re

# 创建ArgumentParser对象
parser = argparse.ArgumentParser(description='Description of your script.')

# 添加命令行参数
parser.add_argument('pattern', type=str, help='pattern to be replaced')
parser.add_argument('replace', type=str, help='[pattern] replace pattern, defalut is empty which means remove the string match the pattern')
parser.add_argument('-r', dest='useRe', action='store_true', help='use regular expression, default is false')

# 解析命令行参数
args = parser.parse_args()
print ("args:",args)

# 设置目录和前缀
directory = "./"
pattern = args.pattern
useRe = args.useRe
replace = args.replace


oriList = []
newList = []

def tryrename(file_path):
    # 获取文件名和扩展名，这个函数获取的文件名会带路径
    _filename, file_extension = os.path.splitext(file_path)
    # 使用os.path.basename获取文件名包含扩展名
    filename = os.path.basename(file_path)

    # 检查文件名匹配
    if useRe: 
        match = re.compile(pattern).match(filename)
    else:
        match = pattern in filename
        
    # print("file:", filename, "pattern:", pattern, "match:", match)
    
    if match:
        # 构建新的文件名
        if useRe: 
            new_filename = re.sub(pattern, replace, filename)
        else:
            new_filename = filename.replace(pattern, replace)

        # 构建新的完整路径
        new_path = os.path.join(os.path.dirname(file_path), new_filename)
        print(f"{file_path} ---------------> {new_path}")
        oriList.append(file_path)
        newList.append(new_path)



def rename(oriList, newList):
    # 重命名文件
    for i in range(len(oriList)):
        try :
            os.rename(oriList[i], newList[i])
            print(f"rename: {oriList[i]} ---> {newList[i]}")
        except:
            print(f"Error!!!!! The new path is invalid : {newList[i]}")

def batch_rename(directory):
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # 检查是否为文件而不是子目录
        if os.path.isfile(file_path):
            tryrename(file_path)

    if len(oriList) > 0 :
        # 询问用户的输入
        user_input = input("Are you sure you want to make the change? y[es]/n[o] : ")
        if user_input == "y" or user_input == "yes" :
            rename(oriList, newList) 
        else:
            print("user cancel~~~")
    else:
        print(f"No files match the renaming rule.")

# 执行批量重命名
batch_rename(directory)
