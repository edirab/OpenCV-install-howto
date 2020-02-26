import os


def absoluteFilePaths(directory, mask):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           # yield os.path.abspath(os.path.join(dirpath, f))
            #print(os.path.abspath(os.path.join(dirpath, f)))
           if mask in f:
                print(f)


def truncate_filename(directory, mask):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            # yield os.path.abspath(os.path.join(dirpath, f))
            # print(os.path.abspath(os.path.join(dirpath, f)))
            if mask in f:
                print(f)
                os.rename(f, f[:30] + ".pdf")


# dir = "C:/Program Files/opencv-4-1-1/build/bin/Release"
dir = ""
boost_dir = r'C:\Program Files\boost-1-71\stage\lib'
boost_mask = ".pdf"

libs = []

#absoluteFilePaths(dir, boost_mask)
truncate_filename(dir, boost_mask)
