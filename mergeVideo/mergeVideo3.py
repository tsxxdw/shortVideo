import os
import uuid

from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.video.io.VideoFileClip import VideoFileClip

from Utils.DateUtil import getDateStr1, getDateStr3
from Utils.NumberCombination import getFileListCombination
from Utils.fileUtil import createFloder, getFileNameNotSuffix
from Utils.videoUtil import getMinfps, removeFile, cutVideo, blur_video, video_manyVideoBlur, resetSize, video_add_audio
from clipVideo.clipVideo1 import fileFloderPath
from contant.PathContant import tempPath, AfterProcessePath, specialFragmentIntroductPath, audioPath


def handleVideo(filePath, min_fps, startTime, cutTime, file_handle, type):
    file_handle.write("文件路径：" + filePath + ",cutTime：" + str(cutTime) + ' \n')
    tmp_output_file_path = os.path.join(tempPath, getFileNameNotSuffix(filePath), getFileNameNotSuffix(filePath) + '_temp.mp4')
    if not os.path.exists(tmp_output_file_path):
        if type == 'v':
            tmp_file_path1 = os.path.join(tempPath, getFileNameNotSuffix(filePath), 'v1_temp.mp4')
            tmp_file_path2 = os.path.join(tempPath, getFileNameNotSuffix(filePath), 'v2_temp.mp4')
            tmp_file_path3 = os.path.join(tempPath, getFileNameNotSuffix(filePath), 'v3_temp.mp4')
            cutVideo(filePath, tmp_file_path1, startTime, cutTime, min_fps)
            resetSize(tmp_file_path1, tmp_file_path2, 1920 * 16 / 9, 1920)
            blur_video(tmp_file_path2, tmp_file_path3)
            video_manyVideoBlur(tmp_file_path1, tmp_file_path3, tmp_output_file_path)
        else:
            tmp_file_path1 = os.path.join(tempPath, getFileNameNotSuffix(filePath), 'v1_temp.mp4')
            cutVideo(filePath, tmp_file_path1, startTime, cutTime, min_fps)
            resetSize(tmp_file_path1, tmp_output_file_path, 1920, 1080)
    return tmp_output_file_path





def excute3():
    todayFloder = AfterProcessePath + "/" + getDateStr1()
    createFloder(todayFloder)
    dateStr = getDateStr3()
    fileName = dateStr + ".mp4"
    video_number, video_duration, type,temp_outFilePath , outFilePath ,file_handle= 2, 30, 'v', tempPath + "/" + fileName,todayFloder + "/" + fileName,open(todayFloder + "/" + dateStr + ".txt", mode='w')
    videoPathArray = getFileListCombination(fileFloderPath + "/newVideo2", video_number, type)
    min_fps = getMinfps([specialFragmentIntroductPath+"/7/7_start.mp4", videoPathArray[0], videoPathArray[1]])
    videoPath0_start = handleVideo(specialFragmentIntroductPath+"/7/7_start.mp4", min_fps, 0, 10000, file_handle, "")
    videoPath1 = handleVideo(videoPathArray[0], min_fps, 10000, video_duration, file_handle, type)
    videoPath2 = handleVideo(videoPathArray[1], min_fps, 10000, video_duration, file_handle, type)
    videoPath3_not_audio = os.path.join(tempPath, "videoPath3", "videoPath3" + '_temp.mp4')
    videoPath4_has_audio = os.path.join(tempPath, "videoPath4", "videoPath4" + '_temp.mp4')
    createFloder(os.path.join(tempPath, "videoPath3"))
    createFloder(os.path.join(tempPath, "videoPath4"))
    concatenate_videoclips([VideoFileClip(videoPath1),VideoFileClip(videoPath2)]).write_videofile(videoPath3_not_audio, fps=min_fps, remove_temp=True)
    video_add_audio(videoPath3_not_audio, audioPath + "/1.wav", videoPath4_has_audio)# 生成目标视频文件
    concatenate_videoclips([VideoFileClip(videoPath0_start), VideoFileClip(videoPath4_has_audio)]).write_videofile(outFilePath, fps=min_fps, remove_temp=True)
    file_handle.close()
    # 清理视频
    removeFile(tempPath)



if __name__ == '__main__':
    n,max = 1,1
    while n <= max:
        excute3()
        n = n+1
    print("执行完毕")
