import os

from multiprocessing import Pool
from multiprocessing import Manager


# 文件拷贝
def copy_file(file_name,old_folder_name,new_folder_name,queue):
    with open('{0}/{1}'.format(old_folder_name,file_name), 'r') as fr:
        with open('{0}/{1}'.format(new_folder_name,file_name), 'w') as fw:
            fw.write(fr.read())
            queue.put(file_name)


def main():
    pool = Pool(3)
    queue = Manager().Queue()
    old_folder_name = input('请输入文件夹名字\n')

    new_folder_name = old_folder_name+'-复件'
    os.mkdir(new_folder_name)
    file_names = os.listdir(old_folder_name)
    file_number = len(file_names)
    for file_name in file_names:
        pool.apply(copy_file, args=(file_name,old_folder_name,new_folder_name,queue))

    pool.close()
    pool.join()
    print(queue.qsize())
    if file_number == queue.qsize():
        print('完成')
    else:
        print('缺少文件')
if __name__ == '__main__':
    main()