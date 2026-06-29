import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

from ultralytics import YOLO

model = YOLO('yolov8x')

result = model.track('input_video/input_video.mp4',conf=0.5 ,save=True)
#print(result)
#print("boxes:")
#for box in result[0]:
#    print(box) 


