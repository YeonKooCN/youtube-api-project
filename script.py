import os
import re
from googleapiclient.discovery import build

api_key = 'AIzaSyA7IFb7wGwfqFFTUxYYyNroNPcJIj_wQb0'

youtube = build('youtube', 'v3', developerKey=api_key)

pl_request = youtube.playlistItems().list(
		part='contentDetails',
		playlistId='PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS'
	)

pl_response = pl_request.execute()

vid_ids = []
for item in pl_response['items']:
	vid_ids.append(item['contentDetails']['videoId'])

vid_request = youtube.videos().list(
		part="contentDetails",
		id=','.join(vid_ids)
	)

vid_response = vid_request.execute()

hours_pattern = re.compile(r'(\d+)H')
minutes_pattern = re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')

for item in vid_response['items']:
	duration = item['contentDetails']['duration']

	hours = hours_pattern.search(duration)
	minutes = minutes_pattern.search(duration)
	seconds = seconds_pattern.search(duration)

	print(hours, minutes, seconds)
	print()