from moviepy import editor #需要moviepy库
#mp4提取音频，需要 pip install moviepy
video = editor.VideoFileClip(r"D:\Downloads\2023-11-23_14-13-55.MP4")
audio = video.audio
#mp3转wav，扩展名小写
audio.write_audiofile(r"D:\Downloads\2023-11-23_14-13-55.wav")


