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

#print("Title:", title)
#print("Thumbnail:", thumbnail)
#print("Date:", date)

set_output("Title:", title)
set_output("Thumbnail:", thumbnail)
set_output("Date:", date)
import uuid

def set_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'{name}={value}', file=fh)


def set_multiline_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        delimiter = uuid.uuid1()
        print(f'{name}<<{delimiter}', file=fh)
        print(value, file=fh)
        print(delimiter, file=fh)
