#!/usr/bin/env python

"""

Interrogate the size of all files (presumably images) in a directory tree (see below)
and move any that are smaller than 640 pixels (in the largest dimension) to a pre-determined
directory.

"""

import os
from os.path import isfile, join
from PIL import Image

def main():
    rootdir = '/Volumes/files/STORAGE/_IMAGES'
    count = 0

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            try:
                filepath = subdir + "/" + file
                # print("Processing file " + filepath + ".")
                im = Image.open(filepath)
            except:
                print(">>>>>> Unable to open file " + filepath + ".")
            else:
                width, height = im.size
                dimension = max(width, height)
                if (dimension < 641):
                    new_path = "/Volumes/files/Trash/Small/" + file
                    print("!!!!!!!!!!!!!!! " + filepath + " moving to " + new_path + "!")
                    os.rename(filepath, new_path)
                    count += 1

    print("Found " + str(count) + " files to be removed.")

if __name__ == '__main__':
    main()
