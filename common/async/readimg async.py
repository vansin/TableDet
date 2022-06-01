

import asyncio



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


async def nested(img_path):
    print(img_path)
    img = mmcv.imread(prefix+img_path)
    img_list.append(img)


async def main():

    tasks = [asyncio.create_task(nested(img_path))
             for img_path in img_path_list]

    for task in tasks:

        await task


start_time = time.perf_counter()

asyncio.run(main())

end_time = time.perf_counter()
print('multiprocessing Calculation takes {} seconds'.format(
    end_time - start_time))