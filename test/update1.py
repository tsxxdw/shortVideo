from moviepy.editor import *

if __name__ == '__main__':
    video_input_path = "D:/duan/file/shortVideo/video/specialVideo/handled/start_1.mp4"
    video_output_path = "D:/duan/file/shortVideo/video/specialVideo/handled/start_11.mp4"
    clip = VideoFileClip(video_input_path)
    clip.write_videofile(video_output_path, fps=23.98)
    clip.reader.close()
