# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 17:17:03 2020
@author: mimel
"""
import re
from googleapiclient.discovery import build
api_key = 'AIzaSyC_FTjp2r4TA3bzqQaMtcVVY--lfIQ_Hv0'
youtube = build('youtube', 'v3', developerKey=api_key)

# Reads youtube video urls from text files and extracts video ids
txt = ''
with open('subvidurls.txt','r') as file:
    txtin = file.readlines()
txt = txt.join(txtin)
videoIds = re.findall(r"=(.*)",txt)


# Takes the video id, which is part of the video url and retrieves the uploader's channel id,
# appends to subs list
subs = []
for videoId in videoIds:
    request1 = youtube.videos().list(
        part="snippet",
        id=videoId
    )
    response1 = request1.execute()
    channelId = response1['items'][0]['snippet']['channelId']
    subs.append(channelId)

# gets the information from a chosen youtube channel with the channel ID and returns the upload id, 
# which contains the playlist info for the channel
for sub in subs:
    request = youtube.channels().list(
        part = 'contentDetails',
        id= channelId
    )
    response = request.execute()
    uploadId = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # retrieves videos from the upload playlist(currently set at 5 most recent)
    request2 = youtube.playlistItems().list(
        part = 'contentDetails',
        playlistId = uploadId
    ) 
    response2 = request2.execute()
    channelTitle = response1['items'][subs.index(sub)]['snippet']['channelTitle']
    print(channelTitle)

    # go through the list of video items and collects the video id, then prints the standard
    # starting url concatenated with the video id. urls are ready to go.
    vidurl_0 = "https://www.youtube.com/watch?v="
    for i in range(len(response2['items'])):
        print(vidurl_0 + response2['items'][i]['contentDetails']['videoId'])