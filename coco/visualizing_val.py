import cv2
import os
import json

img_path = '/home/lsc/Kaggle/xray_gt/gt/'
with open('/home/lsc/Kaggle/result.json', 'r') as f:
    json_f = json.load(f)
img_list = os.listdir(img_path)

for fname in img_list:
    img = cv2.imread(img_path + fname)
    print(img_path + fname)
    for ann in json_f:
        if ann['name'] == fname:
            x1, y1 = ann['bbox'][0], ann['bbox'][1]
            x2, y2 = ann['bbox'][2], ann['bbox'][3]
            # Draw bboxes
            cv2.rectangle(img, (x1,y1), (x2,y2), (0, 0, 255), 3)
            # Add texts
            text = str(ann['category'])
            cv2.putText(img, text, (x1, y1 - 2), 2, 2, (0, 0, 255), 1)
            cv2.imwrite('/home/lsc/Kaggle/xray_gt/inference/%s.jpg' % ann['name'], img)