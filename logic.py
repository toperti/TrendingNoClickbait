# this module uses the Youtube Data API v3, particularly the PlaylistItems resource
# https://developers.google.com/youtube/v3/docs/playlistItems

# The playlist accessed here contains all the videos on the trending page in the same order as the trending page

import requests
import json

# structure of the directory
# /whatever
# 	creds.txt
# 	/app
# 		logic.py
# 		__init__.py
# 		/templates
# 			base.html
# 			home.html
# 		/static
# 			/css 
# 				main.css


# function gets API key from creds.txt file
def getCreds(filename):
	with open(filename) as creds:
		# Using read because creds file should only be one line long
		return creds.read().strip()

# function executes a get request and retrieves the videos in the Playlist
# in JSON format
def getJson(auth):
	params = {"part": 'contentDetails, snippet',
		"playlistId": 'PLrEnWoR732-BHrPp_Pm8_VleD68f9s14-', 
		"maxResults": 50,
		"key": auth}

	response = requests.get("https://www.googleapis.com/youtube/v3/playlistItems/", 
		params = params)

	# response is loaded in json
	jsonResult = json.loads(response.content)
	return jsonResult

# This function calls the above functions, and parses the JSON response
# it returns a list consisting of 3-tuples, which are formatted as such:

# [(title, videoUrl, thumbnail)]
# title = the title of the video in str format
# videoUrl = the URL of the video in str format
# thumbnail = the URL to the default thumbnail for the video
def getTrending():
	auth = getCreds("creds.txt")
	
	vidList = []

	for item in getJson(auth)["items"]:
		title = item["snippet"]["title"]
		videoUrl = "https://www.youtube.com/watch?v=" + item["contentDetails"]["videoId"]
		thumbnail = item["snippet"]["thumbnails"]["default"]["url"]
		vidList.append((title, videoUrl, thumbnail))

	return vidList

	
