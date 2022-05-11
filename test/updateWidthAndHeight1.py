import os
import uuid

from ffmpy import FFmpeg
#背景模糊

def blur_image(image_path: str, output_dir: str, level=10):
    ext = os.path.basename(image_path).strip().split('.')[-1]
    if ext not in ['png', 'jpg']:
        raise Exception('format error')
    ff = FFmpeg(
        inputs={
            '{}'.format(image_path): None}, outputs={
            os.path.join(
                output_dir, '{}.{}'.format(
                    uuid.uuid4(), ext)): '-filter_complex "boxblur={}:1:cr=0:ar=0"'.format(level)})
    print(ff.cmd)
    ff.run()
    return os.path.join(output_dir, '{}.{}'.format(uuid.uuid4(), ext))


def blur_video(video_path: str, output_dir: str, level=30):
    ext = os.path.basename(video_path).strip().split('.')[-1]
    if ext not in ['mp4', 'avi', 'flv']:
        raise Exception('format error')
    ff = FFmpeg(
        inputs={
            '{}'.format(video_path): None}, outputs={
            os.path.join(
                output_dir, '{}.{}'.format(
                    uuid.uuid4(), ext)): '-filter_complex "boxblur={}:1:cr=0:ar=0"'.format(level)})

    print(ff.cmd)
    ff.run()
    return os.path.join(output_dir, '{}.{}'.format(uuid.uuid4(), ext))



if __name__ == '__main__':
    oldFile = "C:/Users/Administrator/Videos/2.mp4"
    newFile ="C:/Users/Administrator/Videos"
    blur_video(oldFile,newFile)