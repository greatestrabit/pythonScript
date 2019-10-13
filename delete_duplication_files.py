import os
import hashlib

file_list = ['/home/dugj/icloud', '/home/dugj/icloud2']


def get_file_id(file):
    md5obj = hashlib.md5()
    maxbuf = 8192
    f = open(file, 'rb')
    while True:
        buf = f.read(maxbuf)
        if not buf:
            break
        md5obj.update(buf)
    f.close()
    hash = md5obj.hexdigest()
    return str(hash).upper()


def delete_dup_file(source_file_id, source_dir):
    for root, dirs, files in os.walk(source_dir):
        for name in files:
            absolutePath = os.path.join(root, name)
            print(absolutePath)
            file_id = get_file_id(absolutePath)
            if file_id in source_file_id:
                print('删除文件:' + absolutePath)
                os.remove(absolutePath)
            else:
                source_file_id.add(file_id)


source_file_id = set()
for file in file_list:
    delete_dup_file(source_file_id, file)

