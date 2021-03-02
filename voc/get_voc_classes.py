import os
import numpy as np

xml_path = 'RTTS/Annotations/'
xmls = os.listdir(xml_path)
class_list = []
for file in xmls:
    f = open('./RTTS/Annotations/' + file, 'r')
    for i in f:
        if '<name>' in i:
            class_list.append(i)
print(np.unique(class_list))
# bicycle, bus, car, motorbike, person
