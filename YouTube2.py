# prompt: make me code that takes the title, thumbnail, and date of a YouTube video

import pytube
import re
from pytube import YouTube

import subprocess

# Install the pytube package
subprocess.call(['pip', 'install', 'pytube'])
# !pip install pytube

def get_video_info(url):
  yt = YouTube(url)
  title = yt.title
  thumbnail = yt.thumbnail_url
  date = yt.publish_date
  return title, thumbnail, date

def main():
  # Get the YouTube video URL from the user.
  url = input("Enter the YouTube video URL: ")

  # Get the video information.
  title, thumbnail, date = get_video_info(url)

  # Print the video information.
  print("Title:", title)
  print("Thumbnail:", thumbnail)
  print("Date:", date)

if __name__ == "__main__":
  main()
