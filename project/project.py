from pytube import YouTube
import os
import ffmpeg
import re


def main():
    #url = f"https://youtu.be/{userIn()}"
    yt = youtube("https://www.youtube.com/watch?v=eQ_8F4nzyiw&ab_channel=LinusTechTips")
    

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
    video = f"{yt.streams.filter(only_video=True)}".split(", ")
    audio = f"{yt.streams.filter(only_audio=True)}".split(", ")
    vid = extract_video(video)
    print(vid)
    aud = extract_audio(audio)
    
    
    
def extract_video(video):
    streams = {}
    for i in video:
        vid = re.search(r'^\[?<Stream: itag="(.{3})" mime_type="video/(?:webm|mp4)" res="(1080|1440|2160)p" fps="30fps" vcodec="(?:vp9|avc1.(?:4d401f|640028))" progressive="False" type="video">\]?$', i, re.IGNORECASE)
        try:
            if vid[2]:
                streams[vid[1]] = vid[2]
        except:
            continue
        
    return max(streams)
    
def extract_audio(audio):
    streams = {}
    for i in audio:
        print(i)
        aud = re.search = r'^\[?<Stream: itag="(.{3})" mime_type="audio/(?:mp4|webm)" abr="(128|160)kbps" acodec="(?:opus|mp4a.40.(?:2|5))" progressive="False" type="audio">\]?$' 
        print(aud)
        
    return max(streams)
if __name__ == "__main__":
    main()
    
    

    