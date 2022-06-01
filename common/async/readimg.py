import re
import mmcv
import os
import time

def is_jpg(x):
    return 'jpg' in x
    
prefix = 'data/icdar2019/test/TRACKA/'
img_path_list = os.listdir(prefix)
img_path_list = list(filter(is_jpg, img_path_list))
img_list = []

start_time = time.perf_counter()

for i, img_path in enumerate(img_path_list):
    print(i)
    img = mmcv.imread(prefix+img_path)
    img_list.append(img)

end_time = time.perf_counter()
print('multiprocessing Calculation takes {} seconds'.format(
    end_time - start_time))

