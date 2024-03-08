# prompt: make me code that takes the title, thumbnail, and date of a YouTube video

!pip install pytube
import pytube
import re
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

print("Title:", title)
print("Thumbnail:", thumbnail)
print("Date:", date)
