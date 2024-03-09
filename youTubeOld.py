import pytube
from pytube import YouTube

def get_video_info(url):
    yt = YouTube(url)
    title = yt.title
    thumbnail = yt.thumbnail_url
    date = yt.publish_date
    return title, thumbnail, date

# Example usage
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
title, thumbnail, date = get_video_info(url)

with open('output.txt', 'w') as f:
    f.write("Title: {}\n".format(title))
    f.write("Thumbnail: {}\n".format(thumbnail))
    f.write("Date: {}\n".format(date))
