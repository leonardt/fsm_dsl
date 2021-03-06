import serial
import time
import sys
from uart import BAUD_RATE, message

# argument should be something like
# /dev/tty.usbserial-142B
# /dev/ttyUSB1
with serial.Serial(sys.argv[1], BAUD_RATE, timeout=1) as ser:
    while True:
        try:
            print(ser.read(len(message) * 5).decode(), end="")
        except UnicodeDecodeError as e:
            print("Experienced {}".format(str(e)))
            print("Possible framing issue, continueing")
