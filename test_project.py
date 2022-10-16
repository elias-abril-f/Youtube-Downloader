from project import combine, userIn, youtube, extract_max, main
from pytube import YouTube
    
    
def test_combine():
    
    assert combine("John Mayer - Ain't no Sunshine", "webm", "mp4") == "Cool beans"
    
def test_userIn():
    assert userIn("https://www.youtube.com/watch?v=CwAnLe4R4F0&t=1022s&ab_channel=Goosee9") == "CwAnLe4R4F0"
    
def test_youtube():
    assert youtube("CwAnLe4R4F0") == "David Ryan Harris feat. John Mayer and Friends - YSD Jam Session - Hotel Café - 2/4/2020 4K Video"; "mp4"; "webm"
    
def test_extract_max():
    yt = YouTube("CwAnLe4R4F0")
    video = f"{yt.streams.filter(only_video=True)}".split(", ")
    audio = f"{yt.streams.filter(only_audio=True)}".split(", ")
    assert extract_max(video) == "401"; "webm"
    assert extract_max(audio) == "251"; "mp4"