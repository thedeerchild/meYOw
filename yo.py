from time import sleep
import json
import requests
import urlparse
from tumblpy import Tumblpy
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
  r = requests.post("http://www.justyo.co/yoall/", data=params)

def take_photo():
  capture = cv.CaptureFromCAM(camera_index)
  frame = cv.QueryFrame(capture)
  cv.SaveImage("pic.jpg", frame)

def post_to_tumblr():
  # Initialize
  t = Tumblpy(environ['tumblr_oauth'], environ['tumblr_secret'])

  # Ask for tokens
  auth_props = t.get_authentication_tokens(callback_url='http://meyow.herokuapp.com')
  auth_url = auth_props['auth_url']

  # Parse the OAuth token from the response
  url = auth_url
  parsed = urlparse.urlparse(url)
  token = urlparse.parse_qs(parsed.query)['oauth_token'][0]

  # Collect them all
  CONSUMER_KEY = environ['tumblr_oauth']
  CONSUMER_SECRET = environ['tumblr_secret']
  OAUTH_TOKEN = token
  OAUTH_TOKEN_SECRET = auth_props['oauth_token_secret']

  print CONSUMER_KEY
  print CONSUMER_SECRET
  print OAUTH_TOKEN
  print OAUTH_TOKEN_SECRET

  # Authenticate dat
  t = Tumblpy(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

  # Get the blog URL we're looking for
  blog_url = t.post('user/info')
  # blog_url = blog_url['user']['blogs'][0]['url']

  # blog_url = 'http://meyow-me.tumblr.com';

  # Load the photo and post to Tumblr
  photo = open('pic.jpg', 'rb')
  post = t.post('post', blog_url=blog_url, params={'type':'photo', 'caption': 'Test Caption', 'data': photo})

send_yo()
# post_to_tumblr()