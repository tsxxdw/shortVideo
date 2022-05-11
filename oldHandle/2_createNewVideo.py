# 根据旧的视频生成新的视频


# 获取所有的文件路径
import os
import shutil

from Utils.videoUtil import getTypeByFilePath
from contant.PathContant import basePath


def getAllFileByOldVideo(path):
    filePathArrays = []
    fileList = os.listdir(path)
    for f in fileList:
        if os.path.isfile(path+"/"+f):
            filePathArrays.append(path+"/"+f)
    return filePathArrays



# 竖屏转横屏
def toHorizontalFromVertical():
    print()
    #blurVideoObj = blurVideo()
    #blurVideoObj.blurVideo1()


def excute(oldVideoFloderPath,newVideoFloderPath):
    arrays = getAllFileByOldVideo(oldVideoFloderPath)
    for filePath in arrays:
        if getTypeByFilePath(filePath)=="h" or getTypeByFilePath(filePath)=="v":
            shutil.copy(filePath,newVideoFloderPath)
            print("文件复制成功："+filePath)






if __name__ == '__main__':
    fileFloderPath = basePath + "/video"
    oldVideo = fileFloderPath + "/oldVideo2"
    newVideo = fileFloderPath + "/newVideo2"
    excute(oldVideo,newVideo)
