import os
from datetime import datetime

def get_file_list(folder_path):
    # 获取给定文件夹路径下所有文件的路径并存储在列表中（不包括目录）
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if not file_name.startswith('.'):  # 排除隐藏文件
                file_list.append(os.path.join(root, file_name))
                
    return file_list

def add_text_to_files(file_list, new_text):
    for file_path in file_list:
        with open(file_path, 'r+', encoding='utf-8') as f:
            old_content = f.read()
            f.seek(0)

            filename, _ = os.path.splitext(os.path.basename(file_path)) 
            now = datetime.now()
            time_str = now.strftime("%Y-%m-%d %H:%M:%S")
            time_str = "2021-05-06 17:27:48"

            formatted = new_text.format(filename, time_str)

            
            print(filename, formatted)
            
            # 在文件头部添加新的文本
            f.write(formatted + '\n' + old_content)
            f.truncate()

if __name__ == '__main__':
    target_folder = 'C:\\Users\\hudejie\\Desktop\\articles\\高性能服务器框架设计'
    new_text_to_add = """---
title: 【转载】{}
date: {}
tags: 
    - 高性能服务器框架设计
    - c++
categories:
    - 转载
---
"""

    # 获取需要处理的文件列表
    files_to_modify = get_file_list(target_folder)

    # 对文件进行修改，插入新文本
    add_text_to_files(files_to_modify, new_text_to_add)
