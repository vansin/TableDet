from mmdet.apis import init_detector, inference_detector
import json
config_file = '/project/train/models/faster_rcnn_r50_fpn_1x_coco.py'
checkpoint_file = '/project/train/models/epoch_12.pth'


model = init_detector(config_file, checkpoint_file)

img = '/home/data/599/fire_8556.jpg'  # or img = mmcv.imread(img), which will only load it once
result = inference_detector(model, img)
objects = []
fires = result[0]
for fire in fires:
    obj = dict(
        xmin=fire[0].item(),
        ymin=fire[1].item(),
        xmax=fire[2].item(),
        ymax=fire[3].item(),
        confidence=fire[4].item(),
        name="fire"
    )

    if obj['confidence']>0.5:
        objects.append(obj)

# model.show_result(img, result)
# model.show_result(img, result, out_file='result.jpg', score_thr = 0.3)

r_json = dict()
r_json['algorithm_data'] = dict(target_info=objects, is_alert=False, target_count=0)
r_json['model_data'] = dict(objects=objects)

if objects.__len__()>0:
    r_json['algorithm_data']['is_alert'] = True
    r_json['algorithm_data']['target_count'] = objects.__len__()


a = json.dumps(r_json, indent=4)

print(a)

