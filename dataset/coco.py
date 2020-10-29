from yacs.config import CfgNode as CN

cn = CN(new_allowed=True)

cn.DATASET = CN(new_allowed=True)
cn.DATASET.NAME = 'COCO'
cn.DATASET.TFRECORDS = '/media/wmcnally/data/coco/TF2-SimpleHumanPose/tfrecords'
cn.DATASET.ANNOT = '/media/wmcnally/data/coco/annotations/person_keypoints_val2017.json'
cn.DATASET.TRAIN_SAMPLES = 149813
cn.DATASET.VAL_SAMPLES = 11004
cn.DATASET.KP_FLIP = [0, 2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15]
cn.DATASET.BGR = False
cn.DATASET.NORM = True
cn.DATASET.MEANS = [0.485, 0.456, 0.406]  # imagenet means RGB
cn.DATASET.STDS = [0.229, 0.224, 0.225]
cn.DATASET.INPUT_SHAPE = [256, 192, 3]
cn.DATASET.OUTPUT_SHAPE = [64, 48, 17]
cn.DATASET.SIGMA = 2 * cn.DATASET.OUTPUT_SHAPE[0] / 64
cn.DATASET.FLIP_PROB = 0.5
cn.DATASET.SCALE_FACTOR = 0.3
cn.DATASET.ROT_PROB = 0.6
cn.DATASET.ROT_FACTOR = 40
cn.DATASET.CACHE = False
cn.DATASET.BFLOAT16 = False

cn.TRAIN = CN(new_allowed=True)
cn.TRAIN.BATCH_SIZE = 64
cn.TRAIN.BASE_LR = 0.00025
cn.TRAIN.LR_SCHEDULE = 'WARMUP_PIECEWISE'
cn.TRAIN.EPOCHS = 210
cn.TRAIN.DECAY_FACTOR = 0.1
cn.TRAIN.DECAY_EPOCHS = [170, 200]
cn.TRAIN.WARMUP_EPOCHS = 0
cn.TRAIN.WARMUP_FACTOR = 32 / cn.TRAIN.BATCH_SIZE
cn.TRAIN.DISP = True
cn.TRAIN.SEED = 0
cn.TRAIN.WD = 1e-5
cn.TRAIN.SAVE_META = True
cn.TRAIN.SAVE_EPOCHS = 0

cn.VAL = CN(new_allowed=True)
cn.VAL.BATCH_SIZE = 64
cn.VAL.FLIP = True

cn.MODEL = CN(new_allowed=True)
cn.MODEL.TYPE = 'evopose'
cn.MODEL.BACKBONE = None
cn.MODEL.HEAD_KERNEL = 3
cn.MODEL.HEAD_CHANNELS = 128
cn.MODEL.HEAD_ACTIVATION = 'swish'
cn.MODEL.GENOTYPE = None
cn.MODEL.WIDTH_COEFFICIENT = 1.
cn.MODEL.DEPTH_COEFFICIENT = 1.

cn.SEARCH = CN(new_allowed=True)


