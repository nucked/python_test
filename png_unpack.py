import os
import struct

file_name = r'c:/game.droid'
fp = open(file_name,'rb')
png_h = '\x89\x50\x4E\x47'
png_e = '\xAE\x42\x60\x82'
data = 1
offset = 0x0
while data:   
    fp.seek(offset)
    data = fp.read(4)
    offset= offset+1    
    if data == png_h:
        i = 0
        data_e = 1
        wp = open(r'c:/'+hex(offset)+'.png','wb')
        wp.write(png_h)
        while data_e and i<0xd0cd64 and data_e != png_e:            
            data_e = fp.read(4)
            wp.write(data_e)
            i = i+1               
            
        print 'offset is '+hex(offset)+' '+data
    
    
    
        

