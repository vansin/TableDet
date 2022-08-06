import mmcv

both_train = mmcv.load('data/table/annotations/both_train.json')['images']
latex_train = mmcv.load('data/table/annotations/latex_train.json')['images']
word_train = mmcv.load('data/table/annotations/word_train.json')['images']
both_test = mmcv.load('data/table/annotations/both_test.json')['images']
latex_test = mmcv.load('data/table/annotations/latex_test.json')['images']
word_test = mmcv.load('data/table/annotations/word_test.json')['images']

both_train.extend(latex_train)
both_train.extend(word_train)
both_train.extend(both_test)
both_train.extend(latex_test)
both_train.extend(word_test)

train_imgs = set()

def path_remake(path):
    return path.replace(' ', '\ ').replace('(','\(').replace(')','\)').replace('&','\&').replace("'","\'")


import shutil

import os

for img in both_train:


    train_imgs.add(img['file_name'])

    # print(both_train)

for img_name in train_imgs:
    path1 = f'/project/TableDet/data/table/images/{img_name}'
    path2 = f'/project/TableDet/data/table/images_small/{img_name}'

    shutil.copyfile(path1, path2)


    # path1 = path_remake(path1)

    # path2 = path_remake(path2)

    # cp_cmd = f'cp {path1} {path2}'
    # os.system(cp_cmd)
    # print(cp_cmd)

