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

# M1:
class general_rle(object):
    '''
    ref.: https://www.kaggle.com/stainsby/fast-tested-rle
    '''

    def __init__(self):
        pass

    def rle_encode(self, binary_mask):
        pixels = binary_mask.flatten()
        # We avoid issues with '1' at the start or end (at the corners of
        # the original image) by setting those pixels to '0' explicitly.
        # We do not expect these to be non-zero for an accurate mask,
        # so this should not harm the score.
        pixels[0] = 0
        pixels[-1] = 0
        runs = np.where(pixels[1:] != pixels[:-1])[0] + 2
        runs[1::2] = runs[1::2] - runs[:-1:2]
        return runs

    def rle_to_string(self, runs):
        return ' '.join(str(x) for x in runs)

    def check(self):
        test_mask = np.asarray([[0, 0, 0, 0],
                                [0, 0, 1, 1],
                                [0, 0, 1, 1],
                                [0, 0, 0, 0]])
        assert rle_to_string(rle_encode(test_mask)) == '7 2 11 2'


# M2:
class binary_mask_rle(object):
    '''
    ref.: https://www.kaggle.com/paulorzp/run-length-encode-and-decode
    '''

    def __init__(self):
        pass

    def rle_encode(self, binary_mask):
        '''
        binary_mask: numpy array, 1 - mask, 0 - background
        Returns run length as string formated
        '''
        pixels = binary_mask.flatten()
        pixels = np.concatenate([[0], pixels, [0]])
        runs = np.where(pixels[1:] != pixels[:-1])[0] + 1
        runs[1::2] -= runs[::2]
        return ' '.join(str(x) for x in runs)

    def rle_decode(self, mask_rle, shape):
        '''
        mask_rle: run-length as string formated (start length)
        shape: (height,width) of array to return
        Returns numpy array, 1 - mask, 0 - background
        '''
        s = mask_rle.split()
        starts, lengths = [np.asarray(x, dtype=int)
                           for x in (s[0:][::2], s[1:][::2])]
        starts -= 1
        ends = starts + lengths
        binary_mask = np.zeros(shape[0] * shape[1], dtype=np.uint8)
        for lo, hi in zip(starts, ends):
            binary_mask[lo:hi] = 1
        return binary_mask.reshape(shape)

    def check(self):
        # maskfile = '/home/PJLAB/huwenxing/Pictures/mmlab.png'

        # mask = np.array(Image.open(maskfile))

        mask = np.zeros([400, 400], np.uint8)

        mask[10:100, 10:50] = 255
        mask[20:30, 20:30] = 0



        binary_mask = mask.copy()
        binary_mask[binary_mask <= 127] = 0
        binary_mask[binary_mask > 127] = 1

        # encode
        rle_mask = self.rle_encode(binary_mask)

        # decode
        binary_mask2 = self.rle_decode(rle_mask, binary_mask.shape[:2])

        # cv2.imshow("iamge", binary_mask2)
        # cv2.waitKey(0)

        #
        assert binary_mask2.shape == binary_mask.shape

        return rle_mask

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


data = mmcv.load('data/icdar2019_tracka_modern/train.json')
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

    x0 = int(x-0.5*ratio*w)
    y0 = int(y-0.5*ratio*h)

    x1 = int(x+w*ratio*0.5)
    y1 = int(y+h*ratio*0.5)

    before[y0:y0+int(h*(1+ratio)), x0:x0+int(w*(1+ratio))] = 255
    before[y1:y1+int(h*(1-ratio)), x1:x1+int(w*(1-ratio))] = 0



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


mmcv.dump(data,
    'data/icdar2019_tracka_modern/train_m.json')
print(annotations)


# import numpy as np
 
# def create_image():
#     img = np.zeros([400, 400], np.uint8)

#     img[10:100, 10:50] = 255
#     img[20:30, 20:30] = 0

# create_image()