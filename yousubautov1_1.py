import re
from googleapiclient.discovery import build
api_key = 'AIzaSyC_FTjp2r4TA3bzqQaMtcVVY--lfIQ_Hv0'
youtube = build('youtube', 'v3', developerKey=api_key)

vidurl = "https://www.youtube.com/watch?v="
txt = ''
with open('subvidurls.txt','r') as file:
    txtin = file.readlines()
txt = txt.join(txtin)
videoIds = re.findall(r"=(.*)",txt)

for videoId in videoIds:
    request1 = youtube.videos().list(
        part="snippet",
        id=videoId
    )
    response1 = request1.execute()

    channelId = response1['items'][0]['snippet']['channelId']
    channelTitle = response1['items'][0]['snippet']['channelTitle']

    request = youtube.channels().list(
        part = 'contentDetails',
        id= channelId
    )
    response = request.execute()

    uploadId = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    request2 = youtube.playlistItems().list(
        part = 'contentDetails',
        playlistId = uploadId
    ) 
    response2 = request2.execute()
    videoIds = response2['items'][0]['contentDetails']['videoId']
    print(channelTitle)
    for videoId in videoIds.splitlines():
        print(vidurl+videoId)
  