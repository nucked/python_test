# -*- coding: cp936 -*-
import os
import sys
import struct

def unpack_app(app,head):
    app_file = open(app,"r+b")
    app_read = app_file.read()
    app_file.close()
    locate = 0
    fname_list = app.split("\\")
    fname = ""
    for i in range(0,len(fname_list)-1):
        fname = fname + fname_list[i]+"\\"
    while True:
        index = app_read.find(head,locate)
        if index == -1:
            break
        packet_addr = app_read[index+4:index+8]
        data_addr = app_read[index+24:index+28]
        img_name = app_read[index+60:index+70]
        (packet_size,) = struct.unpack("I",packet_addr)
        (data_size,) = struct.unpack("I",data_addr)
        print packet_size,data_size
        print img_name.strip('\x00')
        start = index + packet_size
        end = start + data_size
        temp = app_read[start:end]
        locate = index+packet_size+data_size
        output_name = fname + str(img_name.strip('\x00')) + r".img" 
        output = open(output_name,"w+b")
        output.write(temp)
        output.close()
    

if __name__ == "__main__":
    head = b"\x55\xaa\x5a\xa5"
    app = r"F:\rom\华为\G520\华为G520固件(G520-5000,Android 4.1,V100R001CHNC01B216,中国移动)\dload\UPDATE.APP"
    unpack_app(app,head)
