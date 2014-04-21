import re
import string

ins = open( r"D:\Users\wind\dumchar_info", "rb" )
outs = open( r"D:\Users\wind\scatter.txt", "wb" )
for line in ins:
    linesp = re.split('\W+', line)
    name = linesp[0].upper()
    start = int(linesp[2],16)
    block = linesp[5]
    if block != 'misc':
        start = start + 0x600000
    outs.write(name + " " + string.replace(hex(start), "L", "") + "\n{\n}\n")
ins.close()
outs.close()
