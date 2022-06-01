import sys
sys.path.append('/project/mmlab_template/mmdeploy/build/lib/')
import mmdeploy_python

import cv2



import json

from mmdet_custom.datasets import FireDataset

detector = mmdeploy_python.Detector('/project/train/models', 'cuda', 0)

img = cv2.imread('/home/data/599/fire_8556.jpg')

result = detector([img])
objects = []
v1, v2, v3 = result[0][0], result[0][1], result[0][2]
target_count = 0

for i,j,k in zip(v1, v2, v3):

    print(i,j,k)
    obj = dict(
        xmin=i[0].item(),
        ymin=i[1].item(),
        xmax=i[2].item(),
        ymax=i[3].item(),
        confidence=i[4].item(),
        name=FireDataset.CLASSES[j.item()]
    )
    if obj['confidence']>0.5:
        objects.append(obj)
        if obj['name']==FireDataset.CLASSES[0]:
            target_count+=1

r_json = dict()
r_json['algorithm_data'] = dict(target_info=objects, is_alert=False, target_count=0)
r_json['model_data'] = dict(objects=objects)

    
if target_count>0:
    r_json['algorithm_data']['is_alert'] = True
    r_json['algorithm_data']['target_count'] = target_count

a = json.dumps(r_json, indent=4)


print(result)



