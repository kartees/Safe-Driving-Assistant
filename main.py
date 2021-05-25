# import section
import tkinter as tk 
from PIL import Image, ImageTk
from pygame import mixer
import time
import cv2
import cv2 as cv

import os
from keras.preprocessing import image
import matplotlib.pyplot as plt 
import numpy as np
from keras.utils.np_utils import to_categorical
import random,shutil
from keras.models import Sequential
from keras.layers import Dropout,Conv2D,Flatten,Dense, MaxPooling2D, BatchNormalization
from keras.models import load_model
from pygame import mixer
#--------------- import section finish ---------------



#---------- home page -----------------

home=tk.Tk() 
  
# setting the windows size 
home.geometry("900x600") 

home.title("Safe Driving Assistant")
tit = tk.Label(home, text = 'Safe Driving Assistant', font=('calibre',  30, 'bold'),)
tit.place(x=250,y=130) 

subtit = tk.Label(home, text = 'Keep you Safe :)' ,font=('calibre',  15, 'bold'),fg='grey',)
subtit.place(x=380,y=190) 

log = tk.Label(home, text = 'Login' ,font=('calibre',  14, 'bold'),fg='green',)
log.place(x=430,y=260) 

# declaring string variable 
# for storing name and password 
name_var=tk.StringVar() 
passw_var=tk.StringVar() 
  
   
# defining a function that will 
# get the name and password and  
# print them on the screen 
def submit(): 
  
    name= name_entry.get() 
    password= passw_var.get() 

    if name=="driver" and password=="root":
        home.destroy() 
        mainfunc()     
  
    else:
        fail = tk.Label(home, text = 'Login Failed. Try Again !!!', font=('calibre',  12, 'bold'),fg='red')
        fail.place(x=360,y=450)

   
      
      
# creating a label for  
# name using widget Label 
name_label = tk.Label(home, text = 'Username', font=('calibre',  10, 'bold')) 
name_label.place(x= 310,y= 320)   
# creating a entry for input 
# name using widget Entry 
name_entry = tk.Entry(home,  textvariable = name_var,font=('calibre',10,'normal')) 
name_entry.place(x= 400,y= 320)    
# creating a label for password 
passw_label = tk.Label(home, text = 'Password', font = ('calibre',10,'bold')) 
passw_label.place(x= 310,y= 350)   
# creating a entry for password 
passw_entry=tk.Entry(home,  textvariable = passw_var,   font = ('calibre',10,'normal'),  show = '*') 
passw_entry.place(x= 400,y= 350)   
# creating a button using the widget  
# Button that will call the submit function  
sub_btn=tk.Button(home,text = 'Submit',bg='black',fg='white', 
                  command = submit) 
sub_btn.place(x= 440,y= 400)  


 

3
#-------------- home page finish --------------------


#      main page function 

def mainfunc():
    main=tk.Tk()  
    main.geometry("900x600") 
    main.title("Home Page")
    maintit = tk.Label(main, text = 'Safe Driving Assistant', font=('calibre',  20, 'bold'),)
    maintit.place(x=280,y=30)

    drowsy_label = tk.Label(main, text = 'Drowsiness Detection', font=('calibre',  15, 'bold'),fg="grey")
    drowsy_label.place(x=100,y=120) 
    
    drowsy_para = tk.Label(main, text = 'Makes you attentive and preventing from drowsy ', font=('calibre',  12, 'bold'),)
    drowsy_para.place(x=30,y=150) 
 
    drowsy1_btn=tk.Button(main,text = 'Normal Detection  ',bg='black',fg='white', command = drowsy2) 
    drowsy1_btn.place(x= 130,y= 190)
    drowsy2_btn=tk.Button(main,text = 'Advanced Detection',bg='black',fg='white', command = drowsy1) 
    drowsy2_btn.place(x= 130,y= 230)
    

    road_label = tk.Label(main, text = 'Road Lane-line Detection', font=('calibre',  15, 'bold'),fg="grey")
    road_label.place(x=100,y=330) 
    road_para = tk.Label(main, text = 'Visualize lanes to make your route safe ', font=('calibre',  12, 'bold'),)
    road_para.place(x=50,y=360) 
    road_btn=tk.Button(main,text = 'Lane-line Detection  ',bg='black',fg='white', command = lane) 
    road_btn.place(x= 130,y= 400)

    optic_label = tk.Label(main, text = 'Moving object Detector', font=('calibre',  15, 'bold'),fg="grey")
    optic_label.place(x=580,y=120) 
    optic_para = tk.Label(main, text = 'Detect any moving objects ', font=('calibre',  12, 'bold'),)
    optic_para.place(x=565,y=150) 
    optic_btn=tk.Button(main,text = 'Object Detection ',bg='black',fg='white', command = optical) 
    optic_btn.place(x= 630,y= 190)
    
    dense_label = tk.Label(main, text = 'Dense Detection', font=('calibre',  15, 'bold'),fg="grey")
    dense_label.place(x=580,y=240) 
    dense_para = tk.Label(main, text = 'Helps to detect objects in night ', font=('calibre',  12, 'bold'),)
    dense_para.place(x=550,y=270) 
    dense_btn=tk.Button(main,text = 'Dense Detection ',bg='black',fg='white', command = dense) 
    dense_btn.place(x= 630,y= 300)

    main.mainloop()
#---------  finish main page function  ----------


#   drowsy 1 function
def alert():
   mixer.init()
   alert=mixer.Sound('Drowsy/beep-07.wav')
   alert.play()
   time.sleep(0.1)
   alert.play()


def drowsy1():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('Drowsy/lbpcascade_frontalface.xml')
   eye_cascade = cv2.CascadeClassifier('Drowsy/haarcascade_eye.xml')
   blink_cascade = cv2.CascadeClassifier('Drowsy/CustomBlinkCascade.xml')

   while True:
      ret, frame = capture.read()
      gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      faces = face_cascade.detectMultiScale(gray)

      for (x,y,w,h) in faces:
         font = cv2.FONT_HERSHEY_COMPLEX
         cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = frame[y:y+h, x:x+w]

         eyes = eye_cascade.detectMultiScale(roi_gray)
         for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

         blink = blink_cascade.detectMultiScale(roi_gray)
         for(eyx,eyy,eyw,eyh) in blink:
            cv2.rectangle(roi_color,(eyx,eyy),(eyx+eyw,eyy+eyh),(255,255,0),2)
            alert()
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
          break
         
  
   capture.release()
   cv2.destroyAllWindows()


# ----------- drowsy1 function finish -----------------

#           drowsy 2 function ( first model of drowsy)
def drowsy2():
   os.system('python drow.py')
# -------------  drowsy2 function finish ----------------

#     road lane line detection 

def lane():
    os.system('python lanes.py')
    

#    optical flow function 

def optical():
    os.system('python optical.py')

#--------- optical flow function finish --------------

#   dense flow function 

def dense():
    os.system('python dense.py')

#--------- dense flow function finish -------------




















home.mainloop()