#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 23:15:18 2022

@author: payammohammadi
"""

from time import sleep
from cvzone.SerialModule import SerialObject
import cv2

arduino = SerialObject("/dev/tty.usbserial-1410")

on_img =cv2.imread('./image/on.jpg')
off_img =cv2.imread('./image/off.jpg')

while True:
    arduino.sendData([1])
    #sleep(3);
    cv2.imshow('Led ON',on_img)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()    
    arduino.sendData([0])
    cv2.imshow('Led OFF',off_img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    #sleep(1);
    
    