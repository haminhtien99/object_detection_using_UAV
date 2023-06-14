# object_detection_using_UAV
НИР-Цитис
***
Review of the problem
***
***Related works***
* [Detail of dataset VisDrone](https://github.com/VisDrone/VisDrone-Dataset)
* [Training with Faster RCNN](https://github.com/sovit-123/fasterrcnn-pytorch-training-pipeline)
* [Training with Yolov4](https://www.researchgate.net/publication/359391361_Analysis_and_Adaptation_of_YOLOv4_for_Object_Detection_in_Aerial_Images)
***
***Experiments***
1. Models used:
* Yolov7
* Yolov7x
* Faster R-CNN with ResNet-50 FPN backbone
* Faster R-CNN with ResNet-50 FPN backbone (version 2) 
2. Main experiments:
* input size of 640*640 with default hyperparameters
* input size of 1280*1280 with default hyperparameters
3. Other experiments: lr = 0.1, 0.01, 0.001
***Results***
***
Source codes:
* Convert .xml to .txt https://gist.github.com/Amir22010/a99f18ca19112bc7db0872a36a03a1ec
