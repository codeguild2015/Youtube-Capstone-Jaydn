import httplib2
import os
import sys

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow



def get_upload_list():
  #Specifies location of secrets file
  CLIENT_SECRETS_FILE = "client_secrets.json"

  #Message if secrets file is missing or missing information
  MISSING_CLIENT_SECRETS_MESSAGE = """
  WARNING: Please configure OAuth 2.0
  To make this sample run you will need to populate the client_secrets.json file
  found at:
     %s
  with information from the {{ Cloud Console }}
  For more information about the client_secrets.json file format, please visit:
  https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
  """ % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     CLIENT_SECRETS_FILE))

  # This OAuth 2.0 access scope allows for access to the authenticated
  # user's account, can be changed to read-only or other scope
  YOUTUBE_SCOPE = "https://www.googleapis.com/auth/youtube"
  YOUTUBE_API_SERVICE_NAME = "youtube"
  YOUTUBE_API_VERSION = "v3"
  video_list = [] # list to store they video_id 

  #googles authentication flow, way over my head, using their software to speed up Oauth process
  flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
    message=MISSING_CLIENT_SECRETS_MESSAGE,
    scope=YOUTUBE_SCOPE)
  
  #checks for authentication at the secrets path
  storage = Storage("%s-oauth2.json" % sys.argv[0])
  credentials = storage.get() #

  argparser.add_argument('runserver') #argparser will now run with the runserver command
  if credentials is None or credentials.invalid: # if credentials are invalid, output MISSING_CLIENT_SECRETS_MESSAGE
    flags = argparser.parse_args()
    credentials = run_flow(flow, storage,flags) #youtubes(googles) credentials flow

  #builds the youtube object and authenticates service.
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    http=credentials.authorize(httplib2.Http()))

  # Retrieve the contentDetails part of the channel resource for the
  # authenticated user's channel.
  channels_response = youtube.channels().list(
    mine=True, #Only return authenticated user channel list
    part="contentDetails"
  ).execute()

  for channel in channels_response["items"]:
    # From the response, extract the playlist ID that identifies the list
    # of videos uploaded to the authenticated user's channel.
    uploads_list_id = channel["contentDetails"]["relatedPlaylists"]["uploads"]

    # Retrieve the list of videos uploaded to the authenticated user's channel.
    playlistitems_list_request = youtube.playlistItems().list(
      playlistId=uploads_list_id,
      part="snippet", #contains title and position and other info in playlist
      maxResults=50
    )

    while playlistitems_list_request: 
      playlistitems_list_response = playlistitems_list_request.execute()

      # filters through video information, building the dictionary. 
      for playlist_item in playlistitems_list_response["items"]:
        title = playlist_item["snippet"]["title"] # Get's the video's title
        video_id = playlist_item["snippet"]["resourceId"]["videoId"] # get's the specific video's unique ID
        video_list.append(video_id) 

        #while loop update statement, fails once out of items and kicks out of while loop.
      playlistitems_list_request = youtube.playlistItems().list_next(
        playlistitems_list_request, playlistitems_list_response) 

  return video_list   

