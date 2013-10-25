# -*- coding: cp936 -*-
import os
import argparse

def injectFile(hex_find,poke,fname):
    f = open(fname,"r+b")
    b = f.read()
    f.seek(0)
    k = 1
    i = 0
    while k:        
        f.seek(i)
        k = f.read(8)
        if k == hex_find :
            print hex(i)
            break                
        i = i+1
    f.close()

    f = open(fname,"w+b")
    f.write(b)
    f.seek(i-4,0)
    f.write(poke)
    f.close()
    

if __name__ == "__main__":
    hex_find = b"\x75\x22\x5f\x5e\x5d\x33\xc0\x5b"
    fname = r".\PXTOOLS _xxxxxxxxxxxxxxxx.fex"
    poke = b"\x3b\xff\x3b\xff"
    injectFile(hex_find,poke,fname)
    print "done"
    
