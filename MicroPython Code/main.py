from library import mfrc522
from time import sleep
from os import uname

def RUN():
    rdr = mfrc522.MFRC522(sck=2, miso=4, mosi=3, cs=1, rst=0)

    try:
        while True:

            (stat, tag_type) = rdr.request(rdr.REQIDL)

            if stat == rdr.OK:

                (stat, raw_uid) = rdr.anticoll()

                if stat == rdr.OK:
                    print("0x%02x%02x%02x%02x" %
                        (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
                    sleep(1)

    except KeyboardInterrupt:
        pass

if __name__=="__main__":
    RUN()
