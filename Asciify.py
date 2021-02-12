# Asciify : a program to convert jpg to ascii art
# Author : Shekhar Dwivedi
# Date : 11/02/2021

import cv2
import numpy as np

def rescale(mapped_arr,rescale_factor):
    min , max , res_min , res_max = 0 , 255 , 0 , rescale_factor
    for i in range(len(mapped_arr)):
        mapped_arr[i] = (int) ( (res_max - res_min) * (mapped_arr[i] - min) / (max - min) + res_min )
    return mapped_arr

def asciify(arr,type):
    ascii_map = []
    if (type == 0):
        for i in range(len(arr)):
            ascii_map.append(long_set[arr[i]])
        return ascii_map
    else:
        for i in range(len(arr)):
            ascii_map.append(mini_set[arr[i]])
        return ascii_map

def displayAscii(ascii_arr):
    contr = 0
    for i in range(len(ascii_arr)):
        print(ascii_arr[i],end="")
        contr += 1
        if (contr == max_horz):
            print()
            contr = 0


#vars
max_horz = 100 # change to limit the width of ascii art
long_set = ".'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
mini_set = " .:-=+*#%@"
type = 1 # set 0 for long set and 1 for mini set

# Input the file from user
file_path = input("Enter file path")

# read the image
image = cv2.imread(file_path)

# convert to grayscale
grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# extract height width and channel
h,w,c = image.shape

# resize to fit max width of 100 (default)
if(w>max_horz):
    #resize image
    fac = 1 - (w-100)/w
    new_h = (int)(h * fac)
    resized = cv2.resize(grayimg, (100,new_h))

#flatten the image to a array
mapp = []
for i in range(0,new_h):
    for j in range(0,100):
        mapp.append(resized[i,j])

if (type==0):
    rescale_factor = len(long_set)
else:
    rescale_factor = len(mini_set)

#rescale according to gray levels set
f_arr = rescale(mapp,rescale_factor)

#subsitute ascii chars for all values in array
ascii_arr = asciify(f_arr,type)

#print ascii art
displayAscii(ascii_arr)
