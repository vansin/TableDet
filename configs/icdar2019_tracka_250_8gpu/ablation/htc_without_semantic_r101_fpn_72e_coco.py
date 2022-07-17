_base_ = './htc_without_semantic_r50_fpn_1x_coco.py'
# learning policy

model = dict(
    backbone=dict(
        depth=101,
        init_cfg=dict(type='Pretrained',
                      checkpoint='torchvision://resnet101')))

lr_config = dict(warmup_iters=50, step=[47, 63])
runner = dict(max_epochs=72)
