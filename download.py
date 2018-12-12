import sys
import io
import os
import subprocess
import pytube


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

argc = len(sys.argv)

if argc == 1:

    f = open("D:/temp/filelist.txt", 'r')
    parent_dir = "D:\download"

    i = 0
    while True:

        line = f.readline()

        if not line: break

        line = line.strip()

        yt = pytube.YouTube(line) 

        vids= yt.streams.all()

        default_filename = vids[0].default_filename
        default_filename, default_filename_ext = os.path.splitext(default_filename)
        new_filename = '{}_{}'.format(i, default_filename)
       
        vids[0].download(parent_dir, new_filename)

        print(i, " : ", line, " , ", new_filename)
        sys.stdout.flush()

        i = i + 1

    f.close()

else:

    print(argc)

    for i in range(1, argc):

        print(sys.argv[i])

        f = open(sys.argv[i], 'r')

        while True:

            line = f.readline()

            if not line: break

            line = line.strip()

            yt = pytube.YouTube(line) 

            vids= yt.streams.all()

            parent_dir = "D:\download"

            default_filename = vids[0].default_filename
            default_filename, default_filename_ext = os.path.splitext(default_filename)
            new_filename = '{}_{}'.format(i, default_filename)

            vids[0].download(parent_dir, new_filename)
            
            print(i, " : ", line, " , ", new_filename)
            sys.stdout.flush()

        f.close()
