from library import mfrc522
from time import sleep

def RUN():
    rdr = mfrc522.MFRC522(sck=2, miso=4, mosi=3, cs=1, rst=0)

    try:
        while True:
            a = 0
            inp = input()
            
            if inp == "0":
                while a==0:
                    (stat, tag_type) = rdr.request(rdr.REQIDL)

                    if stat == rdr.OK:

                        (stat, raw_uid) = rdr.anticoll()

                        if stat == rdr.OK:
                            
                            if rdr.select_tag(raw_uid) == rdr.OK:

                                key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

                                if rdr.auth(rdr.AUTHENT1A, 8, key, raw_uid) == rdr.OK:
                                    data = rdr.read(8)
                                    datastr = ""
                                    hexstr = []
                                    for i in data:
                                        datastr = datastr + (chr(i))
                                        hexstr.append(hex(i))
                                    print(str(datastr))
                                    a+=1
                                    rdr.stop_crypto1()
                                    
            elif inp == "1":
                num = input()
                while a==0:
                    (stat, tag_type) = rdr.request(rdr.REQIDL)

                    if stat == rdr.OK:

                        (stat, raw_uid) = rdr.anticoll()

                        if stat == rdr.OK:
                            
                            if rdr.select_tag(raw_uid) == rdr.OK:

                                key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

                                if rdr.auth(rdr.AUTHENT1A, 8, key, raw_uid) == rdr.OK:
                                    base = "0000000000000000"
                                    ba = base[:len(base)-len(num)]
                                    byt= str(ba+num).encode()
                                    stat = rdr.write(8, byt)
                                    a+=1
                                    rdr.stop_crypto1()
                                    if stat == rdr.OK:
                                        print(byt.decode())

    except KeyboardInterrupt:
        pass

if __name__=="__main__":
    RUN()
