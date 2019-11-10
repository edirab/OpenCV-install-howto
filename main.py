import os


def absoluteFilePaths(directory):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           # yield os.path.abspath(os.path.join(dirpath, f))
            #print(os.path.abspath(os.path.join(dirpath, f)))
           if "d.lib" in f:
                print(f)


# dir = "C:/Program Files/opencv-4-1-1/build/bin/Release"
dir = "C:/Program Files/opencv-4-1-1/build/install/x64/vc16/lib"
dir = r'F:\Университет\Работа\ЭнергоАвангард\Chiller\pipes'

libs = []

absoluteFilePaths(dir)
