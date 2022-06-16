# optimizer
optimizer = dict(type='SGD', lr=0.02, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)
# learning policy
import os
lr_config = dict(
    policy='Notion',
    by_epoch=False,
    page_id='b7e143d6ae3940beb5c8bff1de7e1846',
    notion_token= os.getenv("NOTION_TOKEN", "")
    )
runner = dict(type='EpochBasedRunner', max_epochs=12)
