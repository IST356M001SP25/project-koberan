# code/transform.py
import pandas as pd, json
from pathlib import Path

# same cache folder, but now we’ll write our cleaned CSV here
CACHE = Path(__file__).parent.parent / "cache"

def transform_earthquakes(data):
    """
    Take the raw USGS JSON (or its text), flatten it into a DataFrame,
    drop small quakes (<4.0), save to CSV, and return the DataFrame.
    """
    if isinstance(data, str):
        # maybe they passed in JSON text instead of a dict
        data = json.loads(data)

    rows = []
    for feature in data["features"]:
        props = feature["properties"]
        lon, lat, _ = feature["geometry"]["coordinates"]
        rows.append({
            "time": pd.to_datetime(props["time"], unit="ms"),
            "mag": props["mag"],
            "place": props["place"],
            "lon": lon,
            "lat": lat
        })

    df = pd.DataFrame(rows) # build a DataFrame
    df = df[df.mag >= 4.0] # keep only magnitude ≥ 4
    CACHE.mkdir(exist_ok=True)
    df.to_csv(CACHE / "transformed_eq.csv", index=False) # cache cleaned data
    return df

if __name__=="__main__":
    # demo: read the raw JSON we saved earlier and show the final size
    raw = json.load(open(CACHE / "raw_earthquakes.json"))
    print(transform_earthquakes(raw).shape)
