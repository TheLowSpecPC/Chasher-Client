import serial
import time

def run(com):
    # open a serial connection
    s = serial.Serial(com, 115200)

    print(s)

    while True:
        re = s.read_all().decode("utf-8")
        if re != "":
            print(re)
            return re
        time.sleep(1)

run("COM1")