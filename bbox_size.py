import json
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (8.0, 8.0)

j = open('instances_train2017.json', 'r')
f = json.load(j)
size = []
n = 0
m = 0
min_scales = 4
min_strides = 4
max_scales = 20
max_strides = 64
thr_min = (min_scales * min_strides)**2
thr_max = (max_scales * max_strides)**2
for i in f['annotations']:
    size.append(i['bbox'][2] * i['bbox'][3])
    if i['bbox'][2] * i['bbox'][3] >= thr_max:
        m += 1
    if i['bbox'][2] * i['bbox'][3] <= thr_min:
        n += 1
print('Min bbox size: {}\nMax bbox size: {}\n{} bboxes smaller than threshold {} x {}\n{} bboxes bigger than threshold {} x {}'.format(min(size), max(size), n, min_scales, min_strides, m, max_scales, max_strides))
# plt.plot(size)
# plt.show()
