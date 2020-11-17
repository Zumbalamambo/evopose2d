# EvoPose2D
Source code for EvoPose2D: Pushing the Boundaries of 2D Human Pose Estimation using Neuroevolution.
Implemented using Python 3.7 and TensorFlow 2.3.

## Getting Started
1. If you haven't already, [install Anaconda or Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
2. Create a new conda environment with Python 3.7: ```$ conda create -n evopose2d python==3.7```
3. Install the dependencies using ```$ pip install -r requirements.txt```
4. Clone this repo: ```$ git clone https://github.com/wmcnally/evopose2d.git```

## Validation / Testing
1. Download a pretrained model: [[bfloat16](https://drive.google.com/drive/folders/1lPXkml5icmKLOGr3o2FQsHEPPe7Du_cH?usp=sharing), float32 (coming soon)] and place it in a new ```models``` directory. The bfloat16 models run best on TPU, and might be slow on older GPUs. 
2. Download the COCO 2017 [validation](http://images.cocodataset.org/zips/val2017.zip) / [test](http://images.cocodataset.org/zips/test2017.zip) images.
3. Download the [validation](http://images.cocodataset.org/annotations/annotations_trainval2017.zip) / [test](http://images.cocodataset.org/annotations/image_info_test2017.zip) annotations.
4. Download the [person detections](https://drive.google.com/drive/folders/1fRUDNUDxe9fjqcRZ2bnF_TKMlO0nB_dk?usp=sharing) (from HRNet repo). 
5. Use [write_tfrecords.py](./write_tfrecords.py) and the detection json to generate the validation / test TFRecords. If using Google Cloud, upload the TFRecords to a Storage Bucket. 
6. Modify the corresponding ```.yaml``` file in [configs](./configs) to point to the directory containing the TFRecords, as well as the validation annotation json. Modify the validation batch size as per your hardware constraints. If you are not using TPU, set the bfloat16 attribute to 'false'.  


## Training
Coming soon

## Neuroevolution
Coming soon

## Acknowledgements

Hardware: 
- NVIDIA GPU Grant
- [TensorFlow Research Cloud (TFRC) program](https://www.tensorflow.org/tfrc)

GitHub Repositories:
- [https://github.com/mks0601/TF-SimpleHumanPose](https://github.com/mks0601/TF-SimpleHumanPose)
- [https://github.com/microsoft/human-pose-estimation.pytorch](https://github.com/microsoft/human-pose-estimation.pytorch)
- [https://github.com/HRNet/HRNet-Human-Pose-Estimation](https://github.com/HRNet/HRNet-Human-Pose-Estimation)
- [https://github.com/megvii-detection/MSPN](https://github.com/megvii-detection/MSPN)
- [https://github.com/mks0601/PoseFix_RELEASE](https://github.com/mks0601/PoseFix_RELEASE)