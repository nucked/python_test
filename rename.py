import os

def walk_dir(dir,topdown=True):
    for root,dirs,files in os.walk(dir,topdown):
        for name in files:
            newname=name.replace('.mp3','')
            os.rename(os.path.join(root,name),os.path.join(root,newname))
            print name,'OK'

path = r'c:\assets'
walk_dir(path)

    
