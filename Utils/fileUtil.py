import os


def createFloder(path):
    if not os.path.exists(path) :
       os.makedirs(path)




def getFileNameNotSuffix(fileName):
    file_name = getFileName(fileName).split('.')[0]
    return file_name

def getFileSuffix(fileName):
    file_name = getFileName(fileName).split('.')[1]
    return file_name

def getFileName(fileName):
    file_Name = fileName.split("/")[-1]
    return file_Name

def getFileDirPath(filePath):
    return os.path.dirname(filePath)

if __name__ == '__main__':
    getFileNameNotSuffix("1.mp4")
