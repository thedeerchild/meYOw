from auth import secrets

import requests
import urlparse
from tumblpy import Tumblpy
import cv

environ = secrets()
cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
camera_index = 0

def take_photo():
  capture = cv.CaptureFromCAM(camera_index)
  frame = cv.QueryFrame(capture)
  cv.SaveImage("pic.jpg", frame)

def post_to_tumblr():
  # Collect them all
  CONSUMER_KEY = environ['tumblr_consumer_key']
  CONSUMER_SECRET = environ['tumblr_consumer_secret']
  OAUTH_TOKEN = environ['tumblr_auth_token']
  OAUTH_TOKEN_SECRET = environ['tumblr_auth_token_secret']

  # Authenticate dat
  t = Tumblpy(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

  # Load the photo and post to Tumblr
  photo = open('pic.jpg', 'rb')
  post = t.post('post', blog_url='http://meyow-me.tumblr.com', params={'type':'photo', 'caption': 'Test Caption', 'data': photo})


def send_tumblr():
  take_photo()
  post_to_tumblr()
  
if __name__ == "__main__":
  send_tumblr()