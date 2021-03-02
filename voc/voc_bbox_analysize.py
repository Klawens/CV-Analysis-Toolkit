import argparse
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
import os
import cv2
from xml.etree import ElementTree as ET

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--annos',help="input Annotations file")
    parser.add_argument('--jpgs',help="input JPEGImages file")
    parser.add_argument('--imgSets',help="input imageSets txtFile")
    return parser.parse_args()
# python voc_bbox_analysize.py --annos "RTTS/Annotations" --jpgs "RTTS/JPEGImages" --imgSets "RTTS/ImageSets/Main/test.txt" 

# statistic the trainval/test image width&heigh
def img_statistic(annoFile, jpgFile, imgSets):
    f = open(imgSets, "r")
    context = f.readlines()
    n = len(context)
    width = np.zeros((n,), dtype=np.int)
    heigth = np.zeros((n,), dtype=np.int)
    for i in range(n):
        line = context[i]
        name = line[:-1]
        im = cv2.imread(jpgFile+'/'+name+'.jpg')
        width[i] = im.shape[0]
        heigth[i] = im.shape[1]
    plt.plot(width, heigth, 'o')
    plt.show()
    # plt.subplot(121)
    # pl.hist(width)
    # pl.xlabel('width')
    # pl.subplot(122)
    # pl.hist(heigth)
    # pl.xlabel('heigth')
    # pl.show()

def bbox_ratio(annoFile, jpgFile, imgSets, reszie_width=None, reszie_hight=None):
    ratio = []
    with open(imgSets, 'r') as f:
        for line in f:
            name = line[:-1]
            tree = ET.parse(annoFile+'/'+name+'.xml')
            root = tree.getroot()

            for size in root.iter(tag="size"):
                width = int(size[0].text)
                hight = int(size[1].text)

            for bndbox in root.iter(tag="bndbox"):
                xmin = int(bndbox[0].text)
                ymin = int(bndbox[1].text)
                xmax = int(bndbox[2].text)
                ymax = int(bndbox[3].text)
                w_bbox = xmax-xmin+1
                h_bbox = ymax-ymin+1

                if reszie_width:
                    w_bbox = w_bbox * (reszie_width / float(width))
                    h_bbox = h_bbox * (reszie_hight / float(hight))

                r = h_bbox/float(w_bbox)
                ratio.append(r)

    if reszie_width:
        plt.title("shoulder_bbox_ratio_resize") 
    else:
        plt.title("shoulder_bbox_ratio") 
    plt.hist(ratio, 80, range=(0, 5), edgecolor='black')
    plt.show()
ratio = []
def bbox_statistic(annoFile, jpgFile, imgSets, reszie_width=None, reszie_hight=None):
    w = []
    h = []
    with open(imgSets, 'r') as f:
        for line in f:
            name = line[:-1]
            tree = ET.parse(annoFile+'/'+name+'.xml')
            root = tree.getroot()

            for size in root.iter(tag="size"):
                width = int(size[0].text)
                hight = int(size[1].text)

            for bndbox in root.iter(tag="bndbox"):
                xmin = int(bndbox[0].text)
                ymin = int(bndbox[1].text)
                xmax = int(bndbox[2].text)
                ymax = int(bndbox[3].text)
                ratio.append((xmax-xmin)/(ymax-ymin))
                w_bbox = xmax-xmin+1
                h_bbox = ymax-ymin+1

                if reszie_width:
                    w_bbox = w_bbox * (reszie_width / float(width))
                    h_bbox = h_bbox * (reszie_hight / float(hight))

                w.append(w_bbox) 
                h.append(h_bbox)
                

    if reszie_width:                
        plt.title("shoulder_bbox_resize_w_statistic") 
    else:
        plt.title("shoulder_bbox_w_statistic") 
    plt.hist(ratio, 20, range=(0, 8), edgecolor='black')
    plt.show()


if __name__ == '__main__':
    args = parse_args()
    bbox_statistic(args.annos, args.jpgs, args.imgSets)
