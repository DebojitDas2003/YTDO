from pytube import YouTube

x = input("Submit your YouTube link here: ")

link = YouTube(x)

video = link.streams.get_highest_resolution()
audio = link.streams.get_audio_only()

y = int(input("Press 1 for Video | Press 2 for Music: "))

# Get the video title
video_title = link.title

if y == 1:
    video.download(output_path="C:\\Users\\deboj\\Downloads", filename=f"{video_title}.mp4")
elif y == 2:
    audio.download(output_path="C:\\Users\\deboj\\Downloads", filename=f"{video_title}.mp3")
