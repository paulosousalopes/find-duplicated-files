#! /usr/bin/python3

import getopt
import os
import sys
import glob
import filecmp
import os.path

def compare(file1, file2):
    return filecmp.cmp(file1, file2)

def getFileNameFromPath(path):
    return path.rsplit('/', 1)[-1]

def moveDuplicatedFile(filename, filepath):
    newfile = "/home/paulo/Duplicated/" + filename
    extra = ''
    count = 0
    while os.path.isfile(newfile + extra):
        count += 1
        extra = " (" + str(count) + ")"
    os.rename(filepath, newfile + extra)

    print('File')
    print(filepath)
    print('was moved to')
    print(newfile + extra)
    print('-------------------\n')

def findDuplicatedFiles(root_dir):
    files = {}

    for filepath in glob.iglob(root_dir + '/**/*', recursive=True):
        if os.path.isfile(filepath):
            filename = getFileNameFromPath(filepath)
            for key in files.keys():
                #if filename == getFileNameFromPath(key):
                if os.path.isfile(key) and os.path.isfile(filepath):
                    if compare(key, filepath):
                        print('-------------------')
                        print('The following files are duplicated:');
                        print(filepath)
                        print(key + '\n')

                        moveDuplicatedFile(filename, filepath)


            files[filepath] = filename

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:v", ["file="])
    except getopt.GetoptError as err:
        # print help information and exit:
        # print str(err)
        sys.exit(2)

    root_dir = None
    ignore_name = False

    for o, a in opts:
        if o in ("-f", "--file"):
            root_dir = a

    findDuplicatedFiles(root_dir, ignore_name)

if __name__ == "__main__":
    main()
