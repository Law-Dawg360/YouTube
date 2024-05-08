from googleapiclient.discovery import build
from datetime import datetime, timedelta

# Your API key
API_KEY = "AIzaSyDhLuQ_Fv16fh_cqyP6Lo1G5GjlGCTOuus"

# IDs of the YouTubers whose videos you want to fetch
CHANNEL_IDS = ["UC7Ucs42FZy3uYzjrqzOIHsw", "UCR6LasBpceuYUhuLToKBzvQ"]  # Add more channel IDs as needed

# Function to fetch latest videos
def fetch_latest_videos():
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    for channel_id in CHANNEL_IDS:
        # Get the uploads playlist ID for the channel
        channel_info = youtube.channels().list(part='contentDetails', id=channel_id).execute()
        uploads_playlist_id = channel_info['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        # Get the latest videos from the uploads playlist
        playlist_items = youtube.playlistItems().list(
            part='snippet',
            playlistId=uploads_playlist_id,
            maxResults=10  # Adjust this number as needed
        ).execute()

        # Process each video in the playlist
        for item in playlist_items['items']:
            video_id = item['snippet']['resourceId']['videoId']
            video_title = item['snippet']['title']
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            video_thumbnail = item['snippet']['thumbnails']['default']['url']
            video_published_at = item['snippet']['publishedAt']
            video_duration = get_video_duration(youtube, video_id)

            # Print or store the information as needed
            print("Uploader:", channel_info['items'][0]['snippet']['title'])
            print("Video URL:", video_url)
            print("Title:", video_title)
            print("Thumbnail:", video_thumbnail)
            print("Published At:", video_published_at)
            print("Duration:", video_duration)
            print("\n")

# Function to get video duration
def get_video_duration(youtube, video_id):
    video_info = youtube.videos().list(
        part='contentDetails',
        id=video_id
    ).execute()

    duration = video_info['items'][0]['contentDetails']['duration']
    return parse_duration(duration)

# Function to parse duration in ISO 8601 format to seconds
def parse_duration(duration):
    duration = duration[2:]  # Remove the leading 'PT'
    seconds = 0

    # Parse days, hours, minutes, seconds
    if 'D' in duration:
        days, duration = duration.split('D')
        seconds += int(days) * 86400
    if 'H' in duration:
        hours, duration = duration.split('H')
        seconds += int(hours) * 3600
    if 'M' in duration:
        minutes, duration = duration.split('M')
        seconds += int(minutes) * 60
    if 'S' in duration:
        seconds += int(duration.split('S')[0])

    return seconds

# Call the function to fetch latest videos
fetch_latest_videos()
