import sys
import io
import subprocess
import pytube


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


f = open("D:/temp/filelist.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    line = line.strip()

    yt = pytube.YouTube(line) 
    vids= yt.streams.all()

    parent_dir = "D:\download"
    vids[0].download(parent_dir)

f.close()