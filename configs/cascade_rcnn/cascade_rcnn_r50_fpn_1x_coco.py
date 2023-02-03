_base_ = [
    '../_base_/models/cascade_rcnn_r50_fpn.py',
    #'../_base_/datasets/coco_detection.py',
    #'../_base_/datasets/wider_challenge_detection.py',
    '../_base_/datasets/cityperson_detection.py',
    #'../_base_/datasets/crowdhuman_detection.py',
    #'../_base_/datasets/wider_crowdhuman_detection.py',
    #'../_base_/datasets/wider_crowdhuman_ecp_detection.py',
    #'../_base_/datasets/eurocity_detection.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]