# -*- coding: cp936 -*-

def findIndex(recovery_head,fname):    
    f = open(fname,"r+b")
    head = open ( r"C:\联想\a788t\A788t_S12852_140515\recovery_head","w+b")
    i = 0
    #end = open ( "C:\联想\a788t\A788t_S12852_140515\recovery_end","w+b")

    byte = f.read(1)
    while byte != "":
        f.seek(i)
        byte = f.read(11)
        if byte == recovery_head :                
            print hex(i)
            rec_head = i
            break                            
        i = i+1        
    f.seek(0)
    c = f.read(rec_head)
    head.write(c)
    head.flush()
    head.close()
    f.close()

def patchRecovery(recovery_in,recovery_out):
    f_in = open(recovery_in,"r+b")
    head = open ( r"C:\联想\a788t\A788t_S12852_140515\recovery_head","r+b")
    f_out = open(recovery_out,"w+b")
    f_out.write(head.read())
    f_out.write(f_in.read())
    f_out.flush()
    f_out.close()
    head.close()
    f_in.close()

if __name__ == "__main__":
    recovery_head = b"\x41\x4e\x44\x52\x4f\x49\x44\x21\x88\x0b\x40"
    fname = r"C:\联想\a788t\A788t_S12852_140515\recovery.img"
    recovery_in = r"C:\联想\a788t\A788t_S12852_140515\a788t.img"
    recovery_out = r"C:\联想\a788t\A788t_S12852_140515\a788t_out.img"
    a = raw_input("input your choice. 1 mean extra, 2 mean patch:")
    while not a.isdigit():
        a = raw_input("input your choice. 1 mean extra, 2 mean patch:")
    if a == 1:
        findIndex(recovery_head,fname)
    else:
        patchRecovery(recovery_in,recovery_out)
    
    print "done"
