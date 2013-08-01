import binascii
import struct
import os

keys = [0x1,0x2]



try:
    fr = file(r'c:/2.dat','rb')
    fw = file(r'c:/3.dat','wb')
    i = 0
    while True:
        chunk = fr.read(2)
        if not chunk:
            break
        for i in range(0, len(chunk)):
            chunk_out = ord(chunk[i])^keys[i]
            
            fw.write(chr(chunk_out))
    fw.flush()
    fw.close()


except IOError:
    print("----------------------------------------")
    print("Progress error")
finally:
    print("----------------------------------------")
    print("done successfully")
    fr.close()
    fw.close()
