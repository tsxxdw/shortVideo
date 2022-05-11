# 竖版视频转横版，在原有视频不变的情况下，将视频两边用白色背景替换
import ffmpeg


def excute(video_input_path,video_output_path):
    input1 = ffmpeg.input(video_input_path)
    w = 1920-609
    output = ffmpeg.output(input1, video_output_path, vcodec='libx264', vf='pad=w=iw+'+str(w)+':h=ih:x='+str(w/2)+':y=0:color=white')
    output.run()

if __name__ == '__main__':
    video_input_path = "C:/Users/Administrator/Videos/1.mp4"
    video_output_path = "C:/Users/Administrator/Videos/8.mp4"
    excute(video_input_path,video_output_path)