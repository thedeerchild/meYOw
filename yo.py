from time import sleep
import json
import requests
import serial
import cv

# ser = serial.Serial('/dev/tty/thing', 9600)

# while True:
#   print ser.readline()
#   sleep(1)

environ = json.load(open("secrets.json"))

cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
camera_index = 0

def send_yo():
  params = {"api_token": environ["yo_key"]}
  r = requests.post("http://www.justyo.co/yoall/", params=params)
  print(r.text)

def take_photo():
  capture = cv.CaptureFromCAM(camera_index)
  frame = cv.QueryFrame(capture)
  cv.SaveImage("pic.jpg", frame)

# def upload_photo():
send_yo()