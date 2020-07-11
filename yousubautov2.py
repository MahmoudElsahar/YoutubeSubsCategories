import re
from googleapiclient.discovery import build

api_key = 'AIzaSyC_FTjp2r4TA3bzqQaMtcVVY--lfIQ_Hv0'
youtube = build('youtube', 'v3', developerKey=api_key)

def get_uploadId(channelId):
    request = youtube.channels().list(
        part = 'contentDetails',
        id= channelId
    )
    response = request.execute()
    uploadId = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    return uploadId

def get_channel(videoId):

    request1 = youtube.videos().list(
        part="snippet",
        id=videoId
    )
    response1 = request1.execute()
    channelId = response1['items'][0]['snippet']['channelId']
    channelTitle = response1['items'][0]['snippet']['channelTitle']
    return [channelId, channelTitle]

def get_videos(uploadId):
    request2 = youtube.playlistItems().list(
        part = 'contentDetails',
        playlistId = uploadId
    ) 
    response2 = request2.execute()
    videos = vidurl_0 + response2['items'][0]['contentDetails']['videoId']+'\n'
    return videos

class Subchannel:
    def __init__(self,videoId):
        self.channelId = get_channel()[1]
        self.channelTitle = get_channel()[0]
        self.uploadId = get_uploadId()
        self.videos = get_videos()

txt = ''
with open('subvidurls.txt','r') as file:
    txtin = file.readlines()
txt = txt.join(txtin)
videoIds = re.findall(r"=(.*)",txt)

for videoId in videoIds:
    videoOut = Subchannel()
    print(videoOut.channelTitle + ':\n' + videoOut.videos)


