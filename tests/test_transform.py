import json
from code.transform import transform_earthquakes

def test_transform_filters_and_columns():
    # ▪︎ Build the simplest earthquake JSON with two quakes
    fake = {
        "features": [
            # quake below 4.0 (should be filtered out)
            {"properties": {"time": 0, "mag": 3.5, "place": "X"},
             "geometry": {"coordinates": [1, 2, 0]}},
            # quake at 5.0 (should remain)
            {"properties": {"time": 0, "mag": 5.0, "place": "Y"},
             "geometry": {"coordinates": [3, 4, 0]}}
        ]
    }

    # ▪︎ Run our transform logic on the fake JSON
    df = transform_earthquakes(fake)

    # ▪︎ It should have exactly these columns
    assert list(df.columns) == ["time", "mag", "place", "lon", "lat"]
    # ▪︎ Only magnitudes >= 4.0 survive
    assert (df.mag >= 4.0).all()
    # ▪︎ And only one row remains (the mag 5.0 quake)
    assert df.shape[0] == 1
