import serial

SERIAL_ADDRESS = '/dev/tty.usbmodemfd121'
BAUD_RATE = 9600

def main_loop():
  ser = serial.Serial(SERIAL_ADDRESS, BAUD_RATE)
  while True:
    print ser.readline()[:-1]


if __name__ == "__main__":
  main_loop()