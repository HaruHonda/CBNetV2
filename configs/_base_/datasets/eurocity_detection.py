dataset_type = 'CocoDataset'
classes = ('pedestrain',) #ecp
#classes = ('pedestrian',) #ecp
#classes = ('person',) crowdhuman and widerperson
#data_root_coco = 'datasets/pedestrian_datasets/COCOPersons/'
#data_root_crowdhuman = '/home/honda/datasets/CrowdHuman/'
#data_root_cityperson = '/home/honda/datasets/CityPersons/'
#data_root_wider = '/home/honda/datasets/Wider_challenge/'
data_root_ecp = '/home/honda/datasets/EuroCity/'
#data_root_caltech = 'datasets/pedestrian_datasets/Caltech/'
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    #original
    #dict(type='Resize', img_scale=(2048, 1024), keep_ratio=True),
    #ours
    dict(type='Resize', img_scale=[(2048, 800), (2048, 1024)], keep_ratio=True),
    #dict(type='Resize', img_scale=[(1216, 608), (2048, 1024)], keep_ratio=True),
    #HRNet
    #dict(type='Resize', img_scale=(1333, 800), keep_ratio=True),
    #dict(type='Resize', img_scale=[(1600, 400), (1600, 1400)], keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    #dict(type='Pad', size_divisor=32),
    dict(type='Pad', size_divisor=64),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]
"""
extra_aug = dict(
    photo_metric_distortion=dict(
        brightness_delta=180,
        contrast_range=(0.5, 1.5),
        saturation_range=(0.5, 1.5),
        hue_delta=18,
    ),
    random_crop=dict(
        min_ious=(0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9),
        min_crop_size=0.1,
    ),
),
"""
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(2048, 1024),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            #dict(type='Pad', size_divisor=32),
            dict(type='Pad', size_divisor=64),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    samples_per_gpu=1,
    workers_per_gpu=6,
    train=dict(
        type=dataset_type,
        ann_file=data_root_ecp + 'day_train_all.json',
        img_prefix=data_root_ecp,
        classes = classes,
        #classes = ['person',],
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        ann_file=data_root_ecp + 'day_val.json',
        img_prefix=data_root_ecp,
        classes=classes,
        pipeline=test_pipeline),
    test=dict(
        type=data_root_ecp,
        ann_file=data_root_ecp + 'day_val.json',
        img_prefix=data_root_ecp,
        classes=classes,
        pipeline=test_pipeline))
evaluation = dict(interval=750, metric='bbox')
