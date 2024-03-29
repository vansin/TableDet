'''
RLE: Run-Length Encode
'''
#!--*-- coding: utf- --*--
from __future__ import annotations
from itertools import groupby
import pycocotools.mask
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2

import mmcv

'''
RLE: Run-Length Encode
'''
def binary_mask_to_rle(binary_mask):
    rle = {'counts': [], 'size': list(binary_mask.shape)}
    counts = rle.get('counts')
    for i, (value, elements) in enumerate(groupby(binary_mask.ravel(order='F'))):
        if i == 0 and value == 1:
            counts.append(0)
        counts.append(len(list(elements)))
    return rle


# before = np.random.rand(400, 400) > 0.5

in_json = 'data/icdar2019_tracka_modern/train.json'
out_json = 'data/icdar2019_tracka_modern/train1.json'

# in_json = 'data/icdar2019_tracka_modern/test.json'
# out_json = 'data/icdar2019_tracka_modern/test_m.json'

# in_json = 'data/table/annotations/both_train.json'
# out_json = 'data/table/annotations/both_train_m.json'

# in_json = 'data/table/annotations/latex_train.json'
# out_json = 'data/table/annotations/latex_train_m.json'

# in_json = 'data/table/annotations/word_train.json'
# out_json = 'data/table/annotations/word_train_m.json'






data = mmcv.load(in_json)
annotations = data['annotations']
# app = binary_mask_rle()


i = 0

ratio = 0.05

for anno in annotations:



    image_id = anno['image_id']
    print(id)
    height = data['images'][image_id]['height']
    width = data['images'][image_id]['width']

    print(height, width)

    before = np.zeros([height, width], np.uint8)

    x,y,w,h = anno['bbox']

    x0 = x
    y0 = y

    x1 = int(x+w*ratio)
    y1 = int(y+h*ratio)

    before[y0:y0+h, x0:x0+w] = 255
    before[y1:y1+int(h*(1-2*ratio)), x1:x1+int(w*(1-2*ratio))] = 0



    # cv2.imshow("iamge", before)
    # cv2.waitKey(0)




    before[before <= 127] = 0
    before[before > 127] = 1


    # foo = pycocotools.mask.encode(np.asarray(before, order="F"))
    # after = pycocotools.mask.decode(foo)
    # anno['segmentation'] = foo

    anno['segmentation'] = binary_mask_to_rle(before)
    
    
    # print(anno)

    pass


mmcv.dump(data, out_json)
print(annotations)


# import numpy as np
 
# def create_image():
#     img = np.zeros([400, 400], np.uint8)

#     img[10:100, 10:50] = 255
#     img[20:30, 20:30] = 0

# create_image()