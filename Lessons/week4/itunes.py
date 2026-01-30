import json # Comes with Python
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Wrong arguments.")
    
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

# Listing songs from a band using itunes API call

o = response.json() # Storing json form of response in an object.
for result in o["results"]: # Iterating over each result body dictionary in the list of results
    print(result["trackName"])


# Whole result:

# Python will convert the json response to a default dictionary format (unless I'm using a library to format it -> json, dump string)
# print(json.dumps(response.json(), indent=2))