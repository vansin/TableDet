_base_ = './htc_without_semantic_r50_fpn_1x_coco.py'
# learning policy

lr_config = dict(warmup_iters=50, step=[47, 63])
runner = dict(max_epochs=72)
