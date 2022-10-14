from pytube import YouTube
import os
import ffmpeg
import re


def main():
    #url = f"https://youtu.be/{userIn()}"
    yt = youtube("https://www.youtube.com/watch?v=V2KU5HracvI&ab_channel=LoopDaddyFanPage")
    


def userIn():
    while True:
        try:
            i = input("Link: ")
            url = re.search(r"^(?:https?://)?(?:www\.)youtube\.com/watch\?v=(\w{11})", i, re.IGNORECASE)[1]
            if not url:
                continue
            return url
        except:
            continue
            
            
def youtube(url):
    yt = YouTube(url)
    video = []
    audio = []
    video = f"{yt.streams.filter(only_video=True)}".split(", ")
    #audio = f"{yt.streams.filter(only_audio=True)}".split(", ")
    
    for i in video:
        print(f'ORIGINAL STREAM \n{i} \n')
        # <Stream: itag="134" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.4d401e" progressive="False" type="video">
        vid = re.search(r'^\[?<Stream: itag="(.{3})" mime_type="video/(?:webm|mp4)" res="(1080p|1440p|2160p)" fps="30fps" vcodec="(?:vp9|avc1.(?:4d401f|640028))" progressive="False" type="video">\]?$', i, re.IGNORECASE)
        try:
            if vid[2]:
                                print(f'CAPTURES \n{vid[1]} {vid[2]}')
        except:
            continue
if __name__ == "__main__":
    main()
    
    

    