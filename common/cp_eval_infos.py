import os, shutil
import mmcv

algorithm_list = []
for root, dirs, files in os.walk('work_dirs'):
    print("root", root)  # 当前目录路径
    # print("dirs", dirs)  # 当前路径下所有子目录
    print("files", files)  # 当前路径下所有非目录子文件

    if files.__len__() > 0:

        algorithm_list.append([root, files])  

for i, element in enumerate(algorithm_list):

    root, work_dir_files = element
    dist_root = root.replace('work_dirs', 'work_dirs_no_pth')

    if not os.path.exists(dist_root):
        os.makedirs(dist_root)

    pth_files = []
    config_file = None
    for file_name in work_dir_files:

        file_name = root + '/' + file_name

        if not file_name.endswith('.pth'):
            print(file_name)
            dst_file = file_name.replace('work_dirs', 'work_dirs_no_pth')
            shutil.copy(file_name, dst_file)
    # for j, pth_file in enumerate(pth_files):
    #     print('===========', i, algorithm_list.__len__(),
    #             j, pth_files.__len__(), '=============')
