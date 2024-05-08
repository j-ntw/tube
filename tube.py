import os
from pytube import YouTube
from pytube.cli import on_progress

def download_video(video_url):
    try:
        yt = YouTube(video_url, on_progress_callback=on_progress)
        stream = yt.streams.get_highest_resolution()
        print("Downloading:", yt.title)
        save_path = os.path.join(os.path.expanduser("~"), "Downloads")
        stream.download(save_path)
        print("Download completed! Video saved in Downloads folder.")

    except Exception as e:
        print("Error:", str(e))

def main():
    video_url = input("Enter the video URL: ")
    download_video(video_url)

if __name__ == "__main__":
    main()
    
else:
    video_url = "https://youtu.be/qgF2ZksUbBE?si=9NYZ07CSEdWMEVpG"
    download_video(video_url)