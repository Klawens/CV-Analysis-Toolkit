import cv2
import os
import json

img_path = 'p_v/'
with open('xxx.bbox.json', 'r') as f:
    json_f = json.load(f)
img_list = os.listdir(img_path)

for fname in img_list:
    img = cv2.imread(img_path + fname)
    print(img_path + fname)
    for ann in json_f:
        if ann['image_id'] + '.jpg' == fname and ann['score'] > 0.2:
            x1, y1 = ann['bbox'][0], ann['bbox'][1]
            x2, y2 = ann['bbox'][2], ann['bbox'][3]
            # Draw bboxes
            cv2.rectangle(img, (int(x1),int(y1),int(x2),int(y2)), (0, 0, 255), 2)
            # Add texts
            # text = str(ann['category'])
            # cv2.putText(img, text, (int(x1), int(y1 - 1)), 2, 2, (0, 0, 255), 1)
            cv2.imwrite('p_r/%s.jpg' % ann['image_id'], img)
