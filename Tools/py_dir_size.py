import os

def get_folder_sizes(folder_path):
    folder_sizes = {}
    # 遍历当前目录下的所有文件夹
    for folder in os.listdir(folder_path):
        folder_full_path = os.path.join(folder_path, folder)
        if os.path.isdir(folder_full_path):
            folder_size = get_total_folder_size(folder_full_path)
            folder_sizes[folder] = folder_size
    return folder_sizes

def get_total_folder_size(folder_path):
    total_size = 0
    # 遍历文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                total_size += os.path.getsize(file_path)
            except Exception as e:
                print('error ', filename)
            else:
                pass
            finally:
                pass
            
    return total_size

def main():
    current_dir = os.getcwd()  # 获取当前目录
    folder_sizes = get_folder_sizes(current_dir)
    sorted_folders = sorted(folder_sizes.items(), key=lambda x: x[1], reverse=True)
    for folder, size in sorted_folders:
        print(f"{folder}: {size / (1024*1024):.2f} MB")

if __name__ == "__main__":
    main()
