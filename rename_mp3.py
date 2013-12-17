import os
path = r'F:\music'
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        if file.find('.')<0:
            newname=file+'.mp3'
            os.rename(os.path.join(path,file),os.path.join(path,newname))
            print file,'ok'
