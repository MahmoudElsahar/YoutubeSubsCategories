# YoutubeSubsCategories
App that takes urls of any video from certain channels and returns the most recently uploaded video from the channel. The
program uses the google api, which requires an api key, but does not require oAuth2.0. V1.1 is straight foreward and simple,
but V2 is a more object-oriented approach which can hopefully scale better and allow for more flexibility in features.

1. copy channel video url and paste it into text file, followed by \n. save file with py file
2. running the code will generate a list of channels based on the text file and also include urls for their most recent videos.

For example, you can have a text file named news.txt where you paste video urls for the CNBC, Fox, BBC, Aljazeera, CNN, etc.. 
channels. Then call the text file with the application to recieve urls for the most recent videos from each of these channels.
You can go to the urls to catch up on your favourites.
