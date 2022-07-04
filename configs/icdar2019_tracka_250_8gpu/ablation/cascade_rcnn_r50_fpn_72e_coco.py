_base_ = './cascade_rcnn_r50_fpn_1x_coco.py'
# learning policy
lr_config = dict(step=[66, 69])
runner = dict(type='EpochBasedRunner', max_epochs=72)
