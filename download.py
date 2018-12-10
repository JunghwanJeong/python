import os
import sys
import io
import subprocess

import pytube


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


yt = pytube.YouTube("https://youtu.be/lLMMYh2TLfU?list=PLKXssUt-F-E4V5tW9ueZLhHS_DDj9TXeM") 

vids= yt.streams.all()

for i in range(len(vids)):
    print(i,'. ',vids[i])

print(vids)

parent_dir = "D:\download"
vids[0].download(parent_dir)

new_filename = 'filename.mp3'

default_filename = vids[0].default_filename 
subprocess.call(['ffmpeg', '-i',                 
    os.path.join(parent_dir, default_filename),
    os.path.join(parent_dir, new_filename)
])


