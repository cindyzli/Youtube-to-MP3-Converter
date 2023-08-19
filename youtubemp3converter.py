from pytube import YouTube
import moviepy.editor as mp
import os
import time

# This is where you put in the Youtube URL
video_url = 'URL'


yt = YouTube(video_url)
audio_stream = yt.streams.filter(only_audio=True).first()
downloaded_file_path = audio_stream.download(output_path='./', filename='temp_audio')
time.sleep(5)  

# Check if the file exists
if os.path.exists(downloaded_file_path):
    print(f"File '{downloaded_file_path}' exists.")

# Convert the downloaded audio to MP3
mp3_output_path = 'output_audio.mp3'
video_clip = mp.AudioFileClip(downloaded_file_path)
video_clip.write_audiofile(mp3_output_path)

# Clean up temporary files
video_clip.close()

# Print information about the working directory and files
print("Current working directory:", os.getcwd())
print("Files in the directory:", os.listdir())
