from project import combine, userIn, youtube, extract_max


def test_combine():
    
    assert combine("John Mayer - Ain't no Sunshine", "webm", "mp4") == "Cool beans"
    
def test_userIn():
    assert userIn("https://www.youtube.com/watch?v=CwAnLe4R4F0&t=1022s&ab_channel=Goosee9") == "CwAnLe4R4F0"
    
def test_youtube():
    assert youtube("CwAnLe4R4F0") == "David Ryan Harris feat. John Mayer and Friends - YSD Jam Session - Hotel Café - 2/4/2020 4K Video", "", 