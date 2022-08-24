import os
from tkinter import Frame
from turtle import width
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)
frame = cv2.imread(images[0])
Height,width,channel = frame.shape
size=(Height,width)
print(size)

uwu = cv2.VideoWriter("QuandaleDingle.mp4",cv2.VideoWriter_fourcc(*'DIVX'),9,size)
for i in range(0,count-1):
    frame = cv2.imread(images[i])
    uwu.write(frame)
uwu.release()
print("don")