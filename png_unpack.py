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
    if data == png_h:
        i = 0
        data_e = 1
        wp = open(r'c:/build/'+hex(offset)+'.png','wb')
        while data_e and data_e != png_e:
            fp.seek(offset+i)
            data_e = fp.read(4)
            i = i+1
            
        i = i+3
        fp.seek(offset)
        wp.write(fp.read(i))
        print 'offset is '+hex(offset)+' file size is '+hex(i) + ' file end is '+hex(offset + i)
        
        wp.flush()
        wp.close()
            
        
    
    offset= offset+1  
    
    
    
        

