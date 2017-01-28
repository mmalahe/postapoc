import os
import subprocess
import shutil

paths = os.listdir(".")
for path in paths:
    if path.endswith(".ogg"):
        newpath = path[:-4]+"_newrate.ogg"
        subprocess.call(["ffmpeg","-i",path,"-ar","44100",newpath])
        os.remove(path)
        shutil.move(newpath,path)
