# code/extract.py
import requests, json
from pathlib import Path

# where we’ll stash raw JSON so we don’t hammer the API every time
CACHE = Path(__file__).parent.parent / "cache"

def fetch_earthquakes():
    """
    Hit the USGS API, save the raw JSON locally, and return it.
    """
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
    resp = requests.get(url) # fetch data from USGS
    resp.raise_for_status() # crash early if something’s wrong
    data = resp.json() # parse the JSON
    CACHE.mkdir(exist_ok=True) # make sure our cache folder exists
    with open(CACHE / "raw_earthquakes.json", "w") as f:
        json.dump(data, f) # save a copy on disk
    return data # hand it back to whoever called us

if __name__=="__main__":
    # quick-and-dirty check: print how many quakes in the raw feed
    print(fetch_earthquakes()["metadata"]["count"])
