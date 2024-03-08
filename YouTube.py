# prompt: make me code that takes the title, thumbnail, and date of a YouTube video

#import os
#name = 'my_name'
#value = 'my_value'
#with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
    #print(f'{name}={value}', file=fh)


#import os
#name = 'my_name'
#value = 'my_value'
#with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
    #print(f'{name}={value}', file=fh)

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
set_multiline_output("Title: ", title)
set_multiline_output("Thumbnail: ", thumbnail)
set_multiline_output("Date: ", date)
def set_multiline_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        delimiter = uuid.uuid1()
        print(f'{name}<<{delimiter}', file=fh)
        print(value, file=fh)
        print(delimiter, file=fh)
#with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
  #print("Title:", title)
  #print("Thumbnail:", thumbnail)
  #print("Date:", date)
  #print(f'{name}<<{delimiter}', file=fh)
  #print(value, file=fh)
  #print(delimiter, file=fh)
  #print(f'{name}={value}', file=fh)
