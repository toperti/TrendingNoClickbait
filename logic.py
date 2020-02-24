# this module uses the Youtube Data API v3, particularly the PlaylistItems resource
# https://developers.google.com/youtube/v3/docs/playlistItems
# The playlist contains all the videos on the trending page in the same order as the trending page

import requests
import json

def getCreds(filename):
	with open(filename) as creds:
		# Using read because creds file should only be one line long
		return creds.read().strip()

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

def getTrending():
	auth = getCreds("creds.txt")
	
	vidList = []

	for item in getJson(auth)["items"]:
		title = item["snippet"]["title"]
		videoId = item["contentDetails"]["videoId"]
		thumbnail = item["snippet"]["thumbnails"]["default"]["url"]
		vidList.append((title, videoId, thumbnail))

	return vidList

	
