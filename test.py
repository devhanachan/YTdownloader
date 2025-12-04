import requests
import json
api= 'https://returnyoutubedislikeapi.com/votes?videoId=EUNw8oY3W7g'
fetch = requests.get(api)
data=fetch.json()
dumbp=json.dumps(data, indent=4, sort_keys=True)
print(dumbp)