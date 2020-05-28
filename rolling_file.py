import os

'''
文件夹结构为
.
├── 1
│   ├── 1-1.txt
│   ├── 1-2.txt
│   └── 1-3.txt
├── 2
│   ├── 2-1.txt
│   ├── 2-2.txt
│   └── 2-3.txt
└── 5
    ├── 5-1.txt
    ├── 5-2.txt
    └── 5-3.txt
    
从5文件夹中依次获取5个文件
从2文件夹中依次获取2个文件
从1文件夹中依次获取1个文件
'''
root_dir = '/home/dugj/Desktop/temp/'
child_dir_list = os.listdir(root_dir)
child_dir_list.sort(reverse=True)


def get_file_path(last_file: str):
    valid = False
    for child_dir in child_dir_list:
        count = int(child_dir)
        child_index = 0
        final_file_list = []

        child_file_list = os.listdir(os.path.join(root_dir, child_dir))
        child_file_list.sort()

        if len(last_file) > 0:
            for child_file in child_file_list:
                this_file = os.path.join(root_dir, child_dir, child_file)
                if this_file == last_file:
                    child_index += 1
                    valid = True
                    continue
                if valid:
                    final_file_list.append(this_file)
                    if (len(final_file_list) == count) or ((child_index + 1) == len(child_file_list)):
                        return final_file_list
                child_index += 1
        else:
            for child_file in child_file_list:
                this_file = os.path.join(root_dir, child_dir, child_file)
                final_file_list.append(this_file)
                if (len(final_file_list) == count) or ((child_index + 1) == len(child_file_list)):
                    return final_file_list
                child_index += 1


print(get_file_path(""))
