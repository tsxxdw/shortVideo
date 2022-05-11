#竖版的视频2个在一起，外加
import os
import uuid

from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.video.io.VideoFileClip import VideoFileClip

from Utils.DateUtil import getDateStr1, getDateStr3
from Utils.NumberCombination import getFileListCombination
from Utils.fileUtil import createFloder
from Utils.videoUtil import getMinfps, removeFile, cutVideo, blur_video, video_manyVideoBlur, resetSize
from clipVideo.clipVideo1 import fileFloderPath
from contant.PathContant import tempPath, AfterProcessePath, specialFragmentIntroductPath


def add(tempNumber, filePathArray, min_fps, array,startTime, cutTime, file_handle, type):
    tempNumber1 = tempNumber
    for file in filePathArray:
        file_handle.write("文件路径："+file+ ",cutTime："+str(cutTime)+' \n')
        uuidStr1 = uuid.uuid1()
        uuidStr2 = uuid.uuid1()
        uuidStr3 = uuid.uuid1()

        tmp_output_file_path = os.path.join(tempPath, str(tempNumber1) + '_temp.mp4')
        if type == 'v':
            tmp_uuidStr_file_path1 = os.path.join(tempPath,  str(uuidStr1)+'v1_temp.mp4')
            tmp_uuidStr_file_path2 = os.path.join(tempPath,  str(uuidStr2)+'v2_temp.mp4')
            tmp_uuidStr_file_path3 = os.path.join(tempPath,  str(uuidStr3)+'v3_temp.mp4')
            cutVideo(file, tmp_uuidStr_file_path1, startTime, cutTime, min_fps)
            resetSize(tmp_uuidStr_file_path1,tmp_uuidStr_file_path2,1920*16/9,1920)
            blur_video(tmp_uuidStr_file_path2, tmp_uuidStr_file_path3)
            video_manyVideoBlur(tmp_uuidStr_file_path1,tmp_uuidStr_file_path3,tmp_output_file_path)
        else:
            tmp_uuidStr_file_path1 = os.path.join(tempPath, str(uuidStr1)+'v1_temp.mp4')
            cutVideo(file, tmp_uuidStr_file_path1, startTime,cutTime, min_fps)
            resetSize(tmp_uuidStr_file_path1, tmp_output_file_path, 1920, 1080)
        # 再次载入处理后的mp4视频
        video = VideoFileClip(tmp_output_file_path)
        array.append(video)
        tempNumber1 = tempNumber1 + 1

def excute3():
    temp_number = 1 #临时文件序号（从1开始累加）
    todayFloder = AfterProcessePath + "/" + getDateStr1()
    createFloder(todayFloder)
    dateStr = getDateStr3()
    fileName = dateStr + ".mp4"
    video_number, video_duration, type, outFilePath = 1, 30, 'v', todayFloder + "/" + fileName
    filePathArray = []
    filePathArray1 = [specialFragmentIntroductPath+"/7/7.mp4"]
    filePathArray2 = getFileListCombination(fileFloderPath + "/newVideo2", video_number, type)
    #filePathArray3 = [specialFragmentIntroductPath + "/8/8.mp4"]
    filePathArray4 = getFileListCombination(fileFloderPath + "/newVideo2", video_number, type)
    #filePathArray5 = [specialFragmentIntroductPath + "/9/9.mp4"]
    filePathArray.append(filePathArray1[0])
    filePathArray.append(filePathArray2[0])
    #filePathArray.append(filePathArray3[0])
    filePathArray.append(filePathArray4[0])
    #filePathArray.append(filePathArray5[0])
    file_handle = open(todayFloder + "/" + dateStr + ".txt", mode='w')
    min_fps = getMinfps(filePathArray)
    resultArray = []
    add(temp_number, filePathArray1, min_fps, resultArray,0, 10000, file_handle, "")
    temp_number = temp_number + 1
    add(temp_number, filePathArray2, min_fps, resultArray,10000, video_duration, file_handle, type)
    temp_number = temp_number + 1
    # add(temp_number, filePathArray3, min_fps, resultArray, video_duration, file_handle, "")
    # temp_number = temp_number + 1
    add(temp_number, filePathArray4, min_fps, resultArray,10000, video_duration, file_handle, type)
    temp_number = temp_number + 1
    # add(temp_number, filePathArray5, min_fps, resultArray, video_duration, file_handle, "")
    # temp_number = temp_number + 1
    #拼接视频
    final_clip = concatenate_videoclips(resultArray)
    # 生成目标视频文件
    final_clip.write_videofile(outFilePath, fps=min_fps, remove_temp=True)
    file_handle.close()
    # 清理视频
    removeFile(tempPath)


if __name__ == '__main__':

    for i in [1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,17,18,19,20,1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,17,18,19,20]:
        excute3()


    print("执行完毕")
