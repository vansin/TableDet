_base_ = './faster_rcnn_r50_fpn_300e_coco.py'
model = dict(train_cfg=dict(rcnn=dict(sampler=dict(type='OHEMSampler'))))
