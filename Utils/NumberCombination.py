# 得到组合
import os
import random
import warnings

from Utils.DateUtil import getDateStr1, getDateStr2, getDateStr3
from Utils.fileUtil import createFloder
from Utils.videoUtil import getTypeByFilePath
from contant.PathContant import specialFragmentIntroductPath_1, specialFragmentPath, number_max, AfterProcessePath


# 获取文件夹下随即的几个视频文件
def getFileListCombination(dir_path,video_number,type):
    fileNameList = os.listdir(dir_path)
    tempArray = []
    for fileName in fileNameList:
        tempFilePath = dir_path +"/"+ fileName
        if getTypeByFilePath(tempFilePath) == type:
            tempArray.append(tempFilePath)

    resultArray = random.sample(tempArray, video_number)
    print("一共获取了文件数量是{}，文件路径为{}",video_number,str(resultArray))
    return resultArray


#得到文件夹组合
def getFloderCombination(specialFragmentIntroductPath_one,normalFragmentPath1):
    fileList = os.listdir(normalFragmentPath1)
    fileList = [n for n in fileList if int(n) <= number_max]
    resultArray = random.sample(fileList, 6)
    return getFileByFloder(specialFragmentIntroductPath_one,normalFragmentPath1,resultArray)


#从文件夹中随意获取一个文件
def getFileByFloder(specialFragmentIntroductPath_one,normalFragmentPathTemp,resultArray):
    warnings.warn("从文件夹中随意获取一个文件 因为掺杂非工具类的方法所以不在建议使用", DeprecationWarning)
    dateStr1 = getDateStr1()
    todayFloder = AfterProcessePath + "/" + dateStr1
    createFloder(todayFloder)
    result = []
    result.append(specialFragmentIntroductPath_one)
    number = 6
    file_handle = open(todayFloder + "/filePath"+getDateStr3()+".txt", mode='w')
    for i in resultArray:
        filePath = normalFragmentPathTemp+"/"+i
        fileList = os.listdir(filePath)
        array1 = random.sample(fileList, 1)
        file_handle.write(i+ "-"+array1[0]+' \n')
        result.append(specialFragmentPath + "/number/"+str(number)+".mp4")
        result.append(filePath+"/"+array1[0])
        number = number - 1
    file_handle.close()
    return result









