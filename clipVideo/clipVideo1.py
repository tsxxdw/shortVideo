#裁剪视频，将视频中的所有内容按照10秒为分割符，然后去除前30秒和最后30多秒的时间，按照10秒一份保存到一个文件夹内
# 多个视频的裁剪内容就保存到多个文件夹内



# 使用系统自带画图功能选择截取的坐标点
from moviepy.editor import *

from Utils.fileUtil import createFloder, getFileNameNotSuffix

fileFloderPath = "D:/duan/file/shortVideo/video/"
oldVideo1 = "oldVideo1"
newVideo1 = "newVideo1"
x1, y1, x2, y2 = 0, 0, 1920, 960
resize_x, resize_y = 1920, 1080
time_space = 15


def getTimeArray(totalTime:int):
    array = []
    if totalTime> 190:
        time1 =  0
        time2 = totalTime - totalTime % 10 - 30
        tempStartTime = time1
        while tempStartTime < time2:
            array.append(tempStartTime)
            tempStartTime = tempStartTime + time_space
    return  array






def cut_out_video(sourceVideo:str,newFloderPath:str):

    start_time = 10  # 这里根据影片开头的时间设置
    end_time = 60
    video_base = VideoFileClip(sourceVideo)  # 手动测试片头从对应时间切分
    total_time = video_base.duration
    # 如果视频长度超过180秒，则进行下一步的分片
    timeArray = getTimeArray(total_time)
    fileName_number = 1
    if len(timeArray) >0 :
        # 手动测试片头从对应时间切分
        video_base = VideoFileClip(sourceVideo)
        n = 1
        for tempStartTime in timeArray:
            print(tempStartTime)
            video_base = VideoFileClip(sourceVideo)  # 手动测试片头从对应时间切分
            video_base = video_base.subclip(tempStartTime, tempStartTime+10)
            # 剔除视频无用部分
            video_base = (video_base.fx(vfx.crop, x1, y1, x2, y2)).resize((resize_x, resize_y))
            video_base.write_videofile(newFloderPath +"/"+ str(n) +".mp4")
            tempStartTime = tempStartTime +time_space
            n = n+1



def  cutAllVideo():
    # 得到所以的视频名称
    fileList = os.listdir(fileFloderPath+oldVideo1)
    createFloder(fileFloderPath+newVideo1)
    n = 1
    for i in fileList:
        if n > 999:
            break
        oldname = fileFloderPath + oldVideo1 + os.sep + fileList[n - 1]  # os.sep添加系统分隔符
        fileNameNotSuffix = getFileNameNotSuffix(fileList[n - 1])
        newFloderPath = fileFloderPath + newVideo1 + os.sep + fileNameNotSuffix  # os.sep添加系统分隔符

        createFloder(fileFloderPath +newVideo1 + "/" + fileNameNotSuffix)
        cut_out_video(oldname,newFloderPath)
        n= n+1






if __name__ == '__main__':
  # cutAllVideo()
   print("代码执行完毕")
