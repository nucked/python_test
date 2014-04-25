# -*- coding: cp936 -*-


def poke(apk,channel):
    poke_to_write = channel+ b"\x00\x00\x00\x00\x00"
    fi = open(apk,"rb")
    file_dir = apk.split("\\")
    k = len(file_dir)
    channel_dir = file_dir[0]
    for i in range (1,k-1):
        channel_dir = channel_dir + "/" + file_dir[i]
    channel_dir_to_write = channel_dir+"/"+channel+".apk"
    fo = open(channel_dir_to_write,"wb")
    fi_read = fi.read()
    fo.write(fi_read)
    fo.write(poke_to_write)
    fi.close()
    fo.close()
    print channel+"已经写入到文件"


if __name__ == "__main__":
    channel = raw_input( "input the Channel number:")
    while not channel.isdigit():
        channel =  raw_input( "input the Channel number:")
    apk = r"F:\rom\10364\(原版).apk"
    poke (apk,channel)
    
    
