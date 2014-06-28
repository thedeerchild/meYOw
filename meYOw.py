import serial
import sys

sys.path.append('./src')
import yo
import tumblr

SERIAL_ADDRESS = '/dev/tty.usbmodemfd121'
BAUD_RATE = 9600
MEASUREMENT_RATE = 0.1 # Number of seconds between readings sent by the Arduino
TRIGGER_THRESHOLD = 2 # Number of seconds target must be in range before triggering
TRIGGER_TIMEOUT = 10 # Number of seconds before program can be triggered again
DISTANCE_THRESHOLD = 30 # cm

def main_loop():
  ser = serial.Serial(SERIAL_ADDRESS, BAUD_RATE)
  counter = 0
  active = True

  while True:
    val = ser.readline().strip().replace("\n","")
    print val
    
    try:
      dist = int(float(val))
    except:
      continue

    if dist < DISTANCE_THRESHOLD and active:
      counter += 1
    else:
      counter = 0

    if counter > (TRIGGER_THRESHOLD / MEASUREMENT_RATE):
      counter = -(TRIGGER_TIMEOUT / MEASUREMENT_RATE)
      print 'CAT!'
      yo.send_yo()
      tumblr.send_tumblr()



if __name__ == "__main__":
  main_loop()