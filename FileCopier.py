import shutil
import os
from os import listdir
import time

sourcePath = ""
destinationPath = ""

#Currently set to 24 hours ago. This can be used later to accept a user defined time for validating if a file should be archived or not.
archiveTime = time.time() - 86400

#checks the source and destination paths given to ensure they are valid and not equal to each other
def validatePath(path):
    if (sourcePath == destinationPath):
        print("Source and destination are the same. Exiting")
        exit()
    else:
        if (os.path.exists(path)):
            return ("Valid path:  ")
        else:
            return ("invalid path. Exiting")
            exit()

#prompt for source path
sourcePath = raw_input("Enter the path of the source folder: ")
validatePath(sourcePath)
print(validatePath(sourcePath) + sourcePath)

#prompt for destination path
destinationPath = raw_input("Enter the path of the destination folder: ")
validatePath(destinationPath)
print(validatePath(destinationPath) + destinationPath)

#prompt for create or modified date as the criteria for coping the file
criteria = ""
while criteria != ("c" or "m"):
    criteria = raw_input("\nWould you like to copy files that have been CREATED in the last 24 hours?\nOr would you like to copy files that have been MODIFIED in the last 24 hours?\nEnter 'c' or 'm'.")
    
filesInFolder = listdir(sourcePath)

def fileCopier(filesInFolder,criteria):
    filesCopied = []
    filesNotCopied = []
    if (criteria == "m"):
        for i in filesInFolder:
            fileCreateTime = os.path.getmtime(sourcePath + "\\" + i)
            if (fileCreateTime > archiveTime):
                shutil.copyfile((sourcePath + "\\" + i), (destinationPath + "\\" + i))
                filesCopied.append(i)
            else:
                filesNotCopied.append(i)
    elif (criteria == "c"):
        for i in filesInFolder:
            fileCreateTime = os.path.getctime(sourcePath + "\\" + i)
            if (fileCreateTime > archiveTime):
                shutil.copyfile((sourcePath + "\\" + i), (destinationPath + "\\" + i))
                filesCopied.append(i)
            else:
                filesNotCopied.append(i)
    else:
            print ("Error in criteria. Exiting")
            exit
    print ("Files that have been copied: ")
    print (filesCopied)
    print ("\nFiles that have not been copied: ")
    print (filesNotCopied)

fileCopier(filesInFolder,criteria)

