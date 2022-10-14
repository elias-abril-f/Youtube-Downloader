from pytube import YouTube
import os
import ffmpeg
import re
import sys

def main():
    url = f"https://youtu.be/{userIn()}"
    yt = youtube(url)
    

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
    vid = extract_max(video)
    print(vid)
    aud = extract_max(audio)
    print(aud)
    
    vidStream = yt.streams.get_by_itag(vid)
    vidStream.download("")
    audStream = yt.streams.get_by_itag(aud)
    audStream.download("")
    
    
    
    
def extract_max(inp):
    streams = {}
    for i in inp:
        print(i)
        if not "kbps" in i:
            temp = re.search(r'^\[?<Stream: itag="(.{3})" mime_type="video/(?:webm|mp4)" res="(1080|1440|2160)p" fps=".?..fps" vcodec=".+" progressive="False" type="video">\]?$', i, re.IGNORECASE)
        else:    
            temp = re.search(r'^\[?<Stream: itag="(.{3})" mime_type="audio/(?:mp4|webm)" abr="(128|160)kbps" acodec=".+" progressive="False" type="audio">\]?$', i, re.IGNORECASE) 
        try:
            if temp[2]:
                streams[temp[1]] = temp[2]
        except:
            continue
    try:
        print(streams)    
        return max(streams)
    except:
        sys.exit("Not enough quality")
        

if __name__ == "__main__":
    main()
    
    

    