from auth import secrets
import requests

environ = secrets()

def send_yo():
  params = {"api_token": environ["yo_key"]}
  r = requests.post("http://www.justyo.co/yoall/", data=params)

if __name__ == "__main__":
  send_yo()