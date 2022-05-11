#暂不使用
#裁剪视频，将视频中的所有内容按照10秒为分割符，然后去除前30秒和最后30多秒的时间，按照10秒一份保存到一个文件夹内
# 多个视频的裁剪内容就保存到多个文件夹内


import os
import uuid
from ffmpy import FFmpeg


# 视频裁剪
def cut_out_video(video_path: str, output_dir: str, start_pix: tuple, size: tuple):
    ext = os.path.basename(video_path).strip().split('.')[-1]
    if ext not in ['mp4', 'avi', 'flv']:
        raise Exception('format error')
    result = os.path.join(output_dir, '{}.{}'.format(uuid.uuid1().hex, ext))
    ff = FFmpeg(inputs={video_path: None},
                outputs={
                    result: '-vf crop={}:{}:{}:{} -y -threads 5 -preset ultrafast -strict -2'.format(size[0], size[1],
                                                                                                     start_pix[0],
                                                                                                     start_pix[1])})
    print(ff.cmd)
    ff.run()
    return result


sourceVideo = r'D:\duan\file\temp\20220430\source\1.mp4'

newPath = r'D:\duan\file\temp\20220430\new'

if __name__ == '__main__':
    cut_out_video(sourceVideo, newPath, (0, 0), (1920, 1080))


