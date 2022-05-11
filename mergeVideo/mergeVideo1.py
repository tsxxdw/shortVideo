#  2022最好看的6个韩国片段

from moviepy.video.fx import crop

from Utils.DateUtil import getDateStr1
from Utils.NumberCombination import getFloderCombination
from Utils.fileUtil import getFileNameNotSuffix, getFileName, createFloder
from Utils.videoUtil import get_video_fps, removeFile, getMinfps

from moviepy.editor import *

#处理片头的分辨率
from contant.PathContant import normalFragmentPath1, specialFragmentIntroductPath, tempPath, AfterProcessePath


def specialFragmentFBL(oldFile,newFile):
    video_base = VideoFileClip(oldFile)  # 手动测试片头从对应时间切分
    # 剔除视频无用部分
    video_base = (video_base.fx(vfx.crop)).resize((1920, 1080))
    video_base.write_videofile(newFile)



# 片头文件路径 + 储存的文件路径
def video_merge1(startVideo:str,outFilePath:str):
    array =[]
    sourceFiles = getFloderCombination(startVideo,normalFragmentPath1)
    min_fps = getMinfps(sourceFiles)
    number = 1
    for file in sourceFiles:
        if specialFragmentIntroductPath in file:
            video_base = VideoFileClip(file)  # 手动测试片头从对应时间切分
            # 剔除视频无用部分
            video = (video_base.fx(vfx.crop)).resize((1920, 1080))
        else:
            video = crop.crop(VideoFileClip(file), x1=0, y1=0, x2=1920, y2=1080)
        # 裁剪视频存为mp4格式文件(也可忽略此步骤，直接使用原始视频)
        tmp_output_file_path = os.path.join(tempPath, str(number) + '_temp.mp4')
        video.write_videofile(tmp_output_file_path, fps=min_fps, remove_temp=False)
        # 再次载入处理后的mp4视频
        video = VideoFileClip(tmp_output_file_path)
        array.append(video)
        number = number +1

    # 拼接视频
    final_clip = concatenate_videoclips(array)
    # 生成目标视频文件
    final_clip.write_videofile(outFilePath, fps=min_fps, remove_temp=True)
    # 清理视频
    removeFile(tempPath)


def getStartVideos():
    startVideoArray = []
    startVideos = os.listdir(specialFragmentIntroductPath)
    for fileName in startVideos:
         startVideoPath = specialFragmentIntroductPath + "/"+fileName+"/"+fileName +".mp4"
         startVideoArray.append(startVideoPath)

    return startVideoArray


if __name__ == '__main__':
    startVideoArray = getStartVideos()
    dateStr1 = getDateStr1()
    for startVideo in startVideoArray:
        fileName = getFileName(startVideo)
        todayFloder = AfterProcessePath +"/"+dateStr1
        createFloder(todayFloder)
        video_merge1(startVideo,todayFloder+"/"+fileName)


    print("执行完毕")