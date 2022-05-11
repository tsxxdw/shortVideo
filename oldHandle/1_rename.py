# 对旧的文件进行重命名处理
import os
import uuid

from Utils.fileUtil import getFileSuffix

if __name__ == '__main__':
    path = "D:/duan/file/shortVideo/video/oldVideo2"
    # 获取该目录下所有文件，存入列表中
    fileList1 = os.listdir(path)
    for oldFileName1 in fileList1:
         uid1 = uuid.uuid1()
         oldFilePath1 = path + os.sep + oldFileName1  # os.sep添加系统分隔符
         if os.path.isfile(oldFilePath1):
             fileSuffix1 = getFileSuffix(oldFilePath1)
             newname1 = path + os.sep + str(uid1) + "." + fileSuffix1
             os.rename(oldFilePath1, newname1)  # 用os模块中的rename方法对文件改名
         else: print("有文件夹存在："+oldFileName1)
    fileList2 = os.listdir(path)
    n2 = 1
    for oldFileName2 in fileList2:
        uid2 = uuid.uuid1()
        oldFilePath2 = path + os.sep + oldFileName2 # os.sep添加系统分隔符
        if os.path.isfile(oldFilePath2):
            fileSuffix2 = getFileSuffix(oldFilePath2)
            newname2 = path + os.sep + str(n2) + "." + fileSuffix2
            os.rename(oldFilePath2, newname2)  # 用os模块中的rename方法对文件改名
            n2 = n2 + 1
        else:
            print("有文件夹存在：" + oldFileName2)



