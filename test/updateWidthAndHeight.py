from moviepy.editor import *
from moviepy.video.fx import crop

from Utils.fileUtil import createFloder, getFileNameNotSuffix
#竖版视频变大
def excute(oldFile,newFile):
    video_base = VideoFileClip(oldFile)  # 手动测试片头从对应时间切分
    # 剔除视频无用部分
    video = (video_base.fx(vfx.crop)).resize((1920, 1080))
    video.write_videofile(newFile, fps=24, remove_temp=False)


if __name__ == '__main__':
    oldFile = "C:/Users/Administrator/Videos/1.mp4"
    newFile ="C:/Users/Administrator/Videos/2.mp4"
    excute(oldFile,newFile)