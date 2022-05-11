import uuid

from ffmpy import FFmpeg
from moviepy.editor import *
# def a(video_input_path,video_output_path):
#     def blur_video(video_path: str, output_dir: str, level=10):
#         ext = os.path.basename(video_path).strip().split('.')[-1]
#         if ext not in ['mp4', 'avi', 'flv']:
#             raise Exception('format error')
#         ff = FFmpeg(
#             inputs={
#                 '{}'.format(video_path): None}, outputs={
#                 os.path.join(
#                     output_dir, '{}.{}'.format(
#                         uuid.uuid4(), ext)): '-filter_complex "boxblur={}:1:cr=0:ar=0"'.format(level)})
#         print(ff.cmd)
#         ff.run()
#         return os.path.join(output_dir, '{}.{}'.format(uuid.uuid4(), ext))

def excute(video1,video3,out):
    # 读取待转换的视频
    clip1 = VideoFileClip(video1)
    clip3 = VideoFileClip(video3)
    # 将视频放大并加蒙版遮罩
    #tempClip2 = VideoFileClip(video_input_path, audio=False, has_mask="True").resize(4)
    #clip2 = tempClip2.fl_image(1)
    # 将小的视频叠在大视频的居中位置
    temp = CompositeVideoClip([clip3, clip1.set_pos("center")])
    # 对叠好的视频进行剪切
    final = temp.crop(x1=0, y1=0, x2=1920, y2=1080)
    # 输出编辑完成的视频
    final.resize(height=clip1.h).write_videofile(out, codec="libx264")

if __name__ == '__main__':
    video1 = "C:/Users/Administrator/Videos/1.mp4"
    video2 = "C:/Users/Administrator/Videos/2.mp4"
    video3 = "C:/Users/Administrator/Videos/3.mp4"
    out = "C:/Users/Administrator/Videos/4.mp4"
    excute(video1,video3,out)

