
import mmdet.datasets.pipelines.auto_augment

from mmdet.datasets.pipelines import AutoAugment

import numpy as np

replace = (104, 116, 124)
policies = [
    [
        dict(type='Sharpness', prob=0.0, level=8),
        dict(
            type='Shear',
            prob=0.4,
            level=0,
            replace=replace,
            axis='x')
    ],
    [
        dict(
            type='Rotate',
            prob=0.6,
            level=10,
            replace=replace),
        dict(type='Color', prob=1.0, level=6)
    ]
]
augmentation = AutoAugment(policies)
img = np.ones(100, 100, 3)
gt_bboxes = np.ones(10, 4)
results = dict(img=img, gt_bboxes=gt_bboxes)
results = augmentation(results)