from pytube import YouTube

x = input("Submit your YouTube link here: ")

link = YouTube(x)

audio = link.streams.get_audio_only()


# Get the video title
video_title = link.title


audio.download(output_path="C:\\Users\\deboj\\Downloads", filename=f"{video_title}.mp3")
