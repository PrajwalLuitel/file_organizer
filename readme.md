This project arranges the files present into different folders according to the file extensions. Initially, it is used to arrange the files in an organized manner once it is downloaded into your device. (The download folder)


How to run:

In the file location.py:
dir_location = "location of the downloads folder" 
(replace the dir_location with the location of directory you wish to arrange)

project_location = "Location of the project folder"
i.e. location of the main.py file in your system


To run the project in background, open command prompt and type:
    pythonw main.py




To automatically arrange the files in downloads folder everytime, create a .bat file with the following line:
        pythonw C:/Users/user/Projects/main.py

And paste it inside the following folder:
    C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Startup/
