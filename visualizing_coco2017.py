import cv2
import os
import json

'''
    Draw bboxes & save.
'''
# cv2.rectangle()
# parameter: image, top-left coordinate, bottom-right coordinate, BGR array, Thickness
# cv2.rectangle(img, (x,y), (x+w,y+h), (B,G,R), Thickness)
 
# cv2.putText()
# parameter: image, text, coordinate, font, size, BGR array, Thickness
# cv2.putText(img, text, (x,y), Font, Size, (B,G,R), Thickness)

img_path = '/home/lsc/Kaggle/xray_gt/'
with open('/home/lsc/Kaggle/xray/annotations/instances_train2017.json', 'r') as f:
    json_f = json.load(f)
img_list = os.listdir(img_path)

for fname in img_list:
    img = cv2.imread(img_path + fname)
    print(img_path + fname)
    for ann in json_f['annotations']:
        if ann['image_id'] == os.path.splitext(fname)[0]:
            x1, y1 = ann['bbox'][0], ann['bbox'][1]
            x2, y2 = ann['bbox'][0] + ann['bbox'][2], ann['bbox'][1] + ann['bbox'][3]
            # Draw bboxes
            cv2.rectangle(img, (x1,y1), (x2,y2), (0, 255, 0), 4)
            # Add texts
            text = str(ann['category_id'])
            cv2.putText(img, text, (x1, y1 - 1), 2, 2, (0, 255, 0), 1)
            cv2.imwrite('/home/lsc/Kaggle/xray_gt/%s.jpg' % ann['image_id'], img)
