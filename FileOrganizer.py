import os
import shutil

# Path
currentDir = os.getcwd()

# Extensions
Images_ext = ('tif, tiff, bmp', 'jpg', 'jpeg',
              'gif', 'png', 'eps', '.raw', 'psd')
Videos_ext = ('mp4', 'mkv')
Acrobats_ext = ('pdf', 'ps', 'eps')
Spreedsheets_ext = ('csv', 'xlsx', 'xlsb', 'xlsm', 'xltx')
Worlddocuments_ext = ('docm', 'dot', 'docx', 'dotx')
Powerpoints_ext = ('pptx', 'pptm', 'ppt',)
Softwares_ext = ('.exe', '.msi')
App_ext = ('apk', 'obb')
Archive_ext = ('zip', 'rar', 'tar', 'iso', '7z')


FileFormates = [Images_ext, Videos_ext, Acrobats_ext,
                Spreedsheets_ext, Worlddocuments_ext, Powerpoints_ext, Softwares_ext, App_ext, Archive_ext]
FolderNames = ["Images", "Videos", "PDF", "Excel", "Word",
               "Powerpoint", "Software Packages", "Apps", "Archives"]


class FileOrganizer:

    def clear_screen():
        os.system("cls")

    def FileChecker(file_ext):
        for key, extension in enumerate(FileFormates):
            #print(key, extension, file_ext)
            if file_ext in (extension):
                Path = f'{currentDir}\\{FolderNames[key]}'
                return Path
            else:
                pass

    def Organizer(file, file_ext):
        Path = FileOrganizer.FileChecker(file_ext)
        if os.path.exists(Path):
            print("path exists")
            shutil.move(file, Path)
            print("file moved")
        else:
            os.mkdir(Path)
            print("Folder Created")
            shutil.move(file, Path)
            print("file moved")


FileOrganizer.clear_screen()

try:
    for (path, dirs, files) in os.walk(currentDir):
        for file in files:
            filename, file_ext = file.split('.')
            thisFile = f'{filename}.{file_ext}'
            if thisFile == 'FileOrganizer.py':
                continue
            else:
                print(f'{filename}.{file_ext}')
                FileOrganizer.Organizer(file, file_ext)
except OSError as error:
    print(error)
