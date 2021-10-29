import shutil
import os
from os import listdir
from os.path import isfile, join
from location import dir_location, project_location
import time

# The path of the directory which is to be organized
location = dir_location

def classify(filename, foldername):
    f = os.listdir(location)
    if foldername[:-1] not in f:
        os.mkdir(location+foldername)

    shutil.move(location+filename, location+foldername)


def organize_files(location):
    files = [f for f in listdir(location) if isfile(join(location,f))]
    if len(files) != 0:
        for file in files:
            extension = file.split(".")[-1]

            if extension == "pdf":
                classify(file, "pdf_files/")

            elif extension in ["pptx", "ppt", "pptm", "potx", "potm", "ppsx", "ppsm"]:
                classify(file, "presentation_files/")

            elif extension in ["docx", "dox", "doc"]:
                classify(file, "word_files/")

            elif extension in ["jpg", "png", "jpeg", "raw", "psd", "gif"]:
                classify(file, "images_and_gifs/")

            elif extension in ["c", "py", "java", "cpp"]:
                classify(file, "developer_files/")
                if extension == "c":
                    classify("developer_files/"+file, "developer_files/C_files/")
                elif extension == "py":
                    classify("developer_files/"+file, "developer_files/Python_files/")
                elif extension == "java":
                    classify("developer_files/"+file, "developer_files/Java_files/")
                elif extension == "cpp":
                    classify("developer_files/"+file, "developer_files/CPP_files/")

            elif extension in ["mp4", "mpg", "mp2", "mpeg", "mpe", "mpv", "m4p", "m4v", "avi", "wmv", "mov", "qt", "flv", "swf"]:
                classify(file, "videos_and_movies/")

            elif extension in ["mp3", "aac", "flac", "alac", "wav", "aiff", "dsd", "pcm", "mid"]:
                classify(file, "audios_and_songs/")

            elif extension in ["xls", "xlr", "xlsx", "xlsb", "xml", "csv"]:
                classify(file, "spreadsheet_files/")

            elif extension in ["txt"]:
                classify(file, "text_files/")

            elif extension in ["html", "css", "js", "php"]:
                classify(file, "web_files/")

            elif extension in ["gz", "rar", "7z", "rpm", "zip", "zipx"]:
                classify(file, "compressed_files/")

            elif extension in ["vcd", "iso", "mdf", "bin"]:
                classify(file, "disk_image_files/")


if __name__ == "__main__":
    try:
        while(True):
            organize_files(location)
            time.sleep(2)

    except Exception as e:
        os.system(f'cmd /k "pythonw {project_location}main.py"') #The project_location is the location of the file main.py