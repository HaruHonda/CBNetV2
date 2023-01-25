checkpoint_config = dict(interval=1)
# yapf:disable
log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook'),
        dict(type='TensorboardLoggerHook')
    ])
# yapf:enable
custom_hooks = [dict(type='NumClassCheckHook')]

dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
#load_from = '/home/honda/work_dirs/wp_cb_x101_fpn_00025_gpu2/epoch_21.pth'
#load_from = './pretrained_models/cascade_mask_rcnn_swin_base_patch4_window7.pth'
#load_from = './work_dirs/crowdhuman_pre_ecp_ft/epoch_23.pth'
#load_from = './work_dirs/ecp_base_3x_coco_pre/epoch_31.pth'
#load_from = './work_dirs/wp_only/epoch_15.pth'
#load_from = './work_dirs/cp_ft_wp_pre_ecp_ft/epoch_1.pth'
resume_from = None
#resume_from = '/home/honda/work_dirs/wp_crowd_cb_x101_fpn_00025_gpu2/epoch_7.pth'
#resume_from = '/home/honda/work_dirs/crowd_cb_x101_fpn_0005_gpu4/epoch_3.pth'
workflow = [('train', 1)]
#work_dir = './work_dirs/cp_dummy_train'
#work_dir = '/home/honda/work_dirs/wp_crowd_cb_x101_fpn_00025_gpu2'
#work_dir = '/home/honda/work_dirs/crowd_cb_x101_fpn_0005_gpu4'
#work_dir = '/home/honda/work_dirs/cp_cb_x101_fpn_0005_gpu4'
#work_dir = '/home/honda/work_dirs/ecp_cb_x101_fpn_0005_gpu4'
#work_dir = '/home/honda/work_dirs/ecp_cb_x101_fpn_000125_gpu1'
#work_dir = '/home/honda/work_dirs/wp_cb_x101_fpn_00025_gpu2_2'
work_dir = '/home/honda/work_dirs/wp_cb_x101_fpn_00025_gpu2_3_person'
#work_dir = '/home/honda/work_dirs/wp_cb_x101_fpn_0005_gpu4'
#work_dir = '/home/honda/work_dirs/cp_cb_x101_fpn_0005_gpu4'
#work_dir = '/home/honda/work_dirs/wp_crowd_cb_x101_fpn_00025_gpu2'
#work_dir = '/home/honda/work_dirs/wp_crowd_cb_x101_fpn_0005_gpu4'
#work_dir = '/home/honda/work_dirs/wp_cb_x101_fpn_0005_gpu4_finetune_ecp'
#work_dir = '/home/honda/work_dirs/wp_cb_swin_base_fpn_0005_gpu4'
#work_dir = '/home/honda/work_dirs/wp_crowd_cb_swin_base_fpn_0.000025_gpu2'