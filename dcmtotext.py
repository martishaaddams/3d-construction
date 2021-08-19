# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 19:28:39 2021

@author: Marisha
"""
#C:\Users\Marisha\Desktop\36614
import sys
import glob
#import pydicom
import pydicom
from pydicom.pixel_data_handlers.util import apply_modality_lut
import numpy as np
# load the DICOM files
files = []
count=0
"""
import glob
for name in glob.glob(’C:/Users/Maria/Documents/Курсовая/модельки/Новая папка/images 1/4876/*’):
print (name)
"""
for fname in glob.glob("C:/Users/Marisha/Desktop/36614/*"):
    print("loading: {}".format(fname))
    files.append(pydicom.dcmread(fname))
    count=count+1
print("All: {} ".format(count))
slices = []
skipcount = 0
for f in files:
    if hasattr(f, "ImagePositionPatient"):
        slices.append(f)
        print(f[0x020,0x032])
    else:
            skipcount = skipcount + 1
print("Skipped: {}".format(skipcount))
count=0

for f in files:
    count=count+1
    print("saving: {}".format(count))
    arr=f.pixel_array
    hu = apply_modality_lut(arr, f)
    width=hu.shape[0]
    height=hu.shape[1]
    xs=f.PixelSpacing[0] #space between pixels in x
    ys=f.PixelSpacing[1] # space beteen pixels in y
    elem=f[0x020,0x032]#image position patient
    zCoord=elem.value[2]#z coordinate of the slice
    evx1=np.zeros(3,dtype=hu.dtype)
    #j is pixel height coordinat
    #i is pixel width coordinat
    countsize=0 #how many pieces there are
    evx=np.zeros(3,dtype=hu.dtype)
    begin=np.zeros(3,dtype=hu.dtype)#begining of the brick
    end=np.zeros(3,dtype=hu.dtype)#ending of the brick 
    exists_now=0#if tthe brick exists now it is ’1’ else it is ’0’
    if(np.any(hu>=2000)):
       print("there are")
       count_brick=0#bricks in the current file
       for j in range (0,height):
           for i in range (0,width):
               if (hu[i,j]>=2000):
                   countsize=countsize+1
                   evx[0]= i*xs#x
                   evx[1]= j*ys#y
                   evx[2]=zCoord#z
                   if (exists_now==0):
                       count_brick=count_brick+1
                       begin=evx
                       exists_now=1
                       evx1=np.vstack([evx1,begin])#creating new brick
                   
            else:
                    if(exists_now==1):
                        end[0]= i*xs#x
                        end[1]= j*ys#y
                        end[2]=zCoord#z
                        exists_now=0
                        evx1=np.vstack([evx1,end]) #ending brick
        if(exists_now==1):
            end[0]= (i+1)*xs#x
            end[1]= j*ys#y
            end[2]=zCoord#z
            exists_now=0
            evx1=np.vstack([evx1,end])#ending brick in the end of the line
    print("almost saved")
    evx1=np.delete(evx1,0,0)
    print("bricks in the file: {}" .format(count_brick))
    #fpath="C:/Users/Maria/Documents/Курсовая/модельки/Новая папка/images 1/4876txt/4876_"+str(count)+".txt"
    fpath='C:/Users/Marisha/Desktop/36614_TEXT/36614_'+str(count)+".txt"
    np.savetxt(fpath,evx1,fmt=’%4.2f’)

