# optimizer
optimizer = dict(type='SGD', lr=0.02, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)
# learning policy
lr_config = dict(
    policy='OneCycle', max_lr=0.1,)
runner = dict(type='EpochBasedRunner', max_epochs=12)
