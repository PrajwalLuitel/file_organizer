import shutil
import os
from os import listdir
from os.path import isfile, join
from location import dir_location
import time

# The path of the directory which is to be organized
location = dir_location

def classify(filename, foldername):
    f = os.listdir(location)
    if foldername[:-1] not in f:
        os.mkdir(location+foldername)
    
    # To check if the same named file already exists in the destination folder
    i=0
    while filename in os.listdir(location+foldername):
        s = filename.split(".")
        if i==0:
            s[-2]+= str(i)
        else:
            s[-2] = s[-2][:-1]+ str(i)
     
        filename2 = ".".join(s)
        os.rename(location+filename, location+filename2)
        filename = filename2
        i += 1
    
    shutil.move(location+filename, location+foldername)


def organize_files(location):
    files = [f for f in listdir(location) if isfile(join(location,f))]
    if len(files) != 0:
        for file in files:
            extension = file.split(".")[-1]

            if extension in ["tmp", "crdownload"]:
                pass
        
            elif extension == "pdf":
                classify(file, "PDF Files/")

            elif extension in ["pptx", "ppt", "pptm", "potx", "potm", "ppsx", "ppsm"]:
                classify(file, "Presentations/")

            elif extension in ["docx", "dox", "doc"]:
                classify(file, "Documents/")

            elif extension in ["jpg", "png", "jpeg", "raw", "psd", "gif"]:
                classify(file, "Photos and GIF/")

            elif extension in ["c", "py", "java", "cpp"]:
                classify(file, "Programming/")
                if extension == "c":
                    classify("Programming/"+file, "Programming/C_files/")
                elif extension == "py":
                    classify("Programming/"+file, "Programming/Python_files/")
                elif extension == "java":
                    classify("Programming/"+file, "Programming/Java_files/")
                elif extension == "cpp":
                    classify("Programming/"+file, "Programming/CPP_files/")

            elif extension in ["mp4", "mpg", "mp2", "mpeg", "mpe", "mpv", "m4p", "m4v", "avi", "wmv", "mov", "qt", "flv", "swf"]:
                classify(file, "Videos/")

            elif extension in ["mp3", "aac", "flac", "alac", "wav", "aiff", "dsd", "pcm", "mid"]:
                classify(file, "Audios/")

            elif extension in ["xls", "xlr", "xlsx", "xlsb", "xml", "csv"]:
                classify(file, "Spreadsheets/")

            elif extension in ["txt"]:
                classify(file, "Text Files/")

            elif extension in ["html", "css", "js", "php"]:
                classify(file, "Web Files/")

            elif extension in ["gz", "rar", "7z", "rpm", "zip", "zipx"]:
                classify(file, "Compressed Files/")

            elif extension in ["vcd", "iso", "mdf", "bin"]:
                classify(file, "Disk Image Files/")
            
            else:
                classify(file, "Unknown Format Files/")


if __name__ == "__main__":
    try:
        while(True):
            organize_files(location)
            time.sleep(2)

    except Exception as e:
        # print("Error: " + str(e))
        os.system(f'cmd /c "echo {e}"')