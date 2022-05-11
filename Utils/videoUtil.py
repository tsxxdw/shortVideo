import subprocess
import random

import cv2
from ffmpy import FFmpeg
from imageio.plugins import ffmpeg
from moviepy.editor import *

from Utils.fileUtil import getFileNameNotSuffix, getFileDirPath, createFloder


def getMinfps(video_list: list):
    old_fps = 30
    for x in video_list:
        new_fps = get_video_fps(x)
        if new_fps<old_fps:
            old_fps = new_fps
    return old_fps


def get_video_fps(video_path: str):
    ext = os.path.splitext(video_path)[-1]
    if ext != '.mp4' and ext != '.mkv' and ext != '.avi' and ext != '.flv':
        raise Exception('format not support')
    ffprobe_cmd = 'ffprobe -v error -select_streams v -of default=noprint_wrappers=1:nokey=1 -show_entries stream=r_frame_rate {}'
    p = subprocess.Popen(
        ffprobe_cmd.format(video_path),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True)
    out, err = p.communicate()
    #print("subprocess 执行结果：out:{} err:{}".format(out, err))
    fps_info = str(out, 'utf-8').strip()
    if fps_info:
        if fps_info.find("/") > 0:
            video_fps_str = fps_info.split('/', 1)
            fps_result = int(int(video_fps_str[0]) / int(video_fps_str[1]))
        else:
            fps_result = int(fps_info)
    else:
        raise Exception('get fps error')
    return fps_result


# 判断该文件是否是竖屏视频
def getTypeByFilePath(filePath):
    capture = cv2.VideoCapture(filePath)
    frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    if frame_width == 1080 and frame_height == 1920:
        return "v"
    elif frame_height == 1920 and frame_width == 1080:
        return "h"
    else:
        return "o"

#移除文件夹中所有的文件
def removeFile(output_dir):
    for root, dirs, files in os.walk(output_dir):
        for file in files:
            if os.path.splitext(file)[-1] == '.mp4':
                if os.path.splitext(file)[0][-4:] == 'temp':
                    os.remove(os.path.join(root, file))



#重置大小
def resetSize(oldFilePath,newFilePath,x_size,y_size):
    video_base = VideoFileClip(oldFilePath)
    video_base = (video_base.fx(vfx.crop)).resize((x_size, y_size))
    video_base.write_videofile(newFilePath,remove_temp=False)



# 裁剪视频
def cutVideo(oldFilePath,newFilePath,start_time,cutTime,min_fps):
    createFloder(getFileDirPath(newFilePath))
    video_base = VideoFileClip(oldFilePath)
    total_time = int(video_base.duration)
    if cutTime >= total_time:
        cutTime = total_time
        start_time = 0
    if start_time >= total_time:
        sjs = random.randint(0, int(total_time / cutTime)) * cutTime
        start_time = sjs
    if total_time <= 30:
        start_time = 0
    elif total_time - start_time < cutTime:
         start_time = total_time - cutTime - 1
    video_base = video_base.subclip(start_time, start_time + cutTime)
    video_base.write_videofile(newFilePath,fps=min_fps, remove_temp=True)
    #video_base.write_videofile(newFilePath, fps=min_fps, remove_temp=False)
    #file_handle.write("fileName:" + getFileNameNotSuffix(oldFilePath)+",start_time:"+str(start_time)+"total_time:"+str(total_time)+",cutTime:"+str(cutTime) + ' \n')

def blur_video(oldVideoPath: str, newVideoPath: str, level=100):
    ext = os.path.basename(oldVideoPath).strip().split('.')[-1]
    if ext not in ['mp4', 'avi', 'flv','mkv']:
        raise Exception('format error')
    ff = FFmpeg(
        inputs={
            '{}'.format(oldVideoPath): None}, outputs={
            newVideoPath: '-filter_complex "boxblur={}:1:cr=0:ar=0"'.format(level)})

    print(ff.cmd)
    ff.run()


def video_manyVideoBlur(oldVideoPath1,oldVideoPath2,newVideoPath):
    # 读取待转换的视频
    clip1 = VideoFileClip(oldVideoPath1)
    clip3 = VideoFileClip(oldVideoPath2)
    # 将视频放大并加蒙版遮罩
    #tempClip2 = VideoFileClip(video_input_path, audio=False, has_mask="True").resize(4)
    #clip2 = tempClip2.fl_image(1)
    # 将小的视频叠在大视频的居中位置
    video_base = CompositeVideoClip([clip3, clip1.set_pos("center")])
    # 对叠好的视频进行剪切
    # final = temp.crop(x1=0, y1=0, x2=1920, y2=1080)
    # 输出编辑完成的视频
    video_base = (video_base.fx(vfx.crop)).resize((1920, 1080))
    video_base.write_videofile(newVideoPath, codec="libx264")



# 视频添加音频
def video_add_audio(video_path: str, audio_path: str, output_dir: str):
    _ext_video = os.path.basename(video_path).strip().split('.')[-1]
    _ext_audio = os.path.basename(audio_path).strip().split('.')[-1]
    if _ext_audio not in ['mp3', 'wav']:
        raise Exception('audio format not support')
    _codec = 'copy'
    if _ext_audio == 'wav':
        _codec = 'aac'

    ff = FFmpeg(
        inputs={video_path: None, audio_path: None},
        outputs={output_dir: '-map 0:v -map 1:a -c:v copy -c:a {} -shortest'.format(_codec)})
    print(ff.cmd)
    ff.run()
