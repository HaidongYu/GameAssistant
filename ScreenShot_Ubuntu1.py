import pyautogui
import cv2
import numpy as np
img = pyautogui.screenshot(region=[0,0,1920,1080]) # x,y,w,h #
img.save('/home/haidong/Desktop/screenshot.jpg')
#img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)
