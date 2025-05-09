import pandas as pd
import pytest
from code.load import load_data, CACHE

def test_load(tmp_path, monkeypatch):
    # create a fake cache directory
    fake_cache = tmp_path / "cache"
    fake_cache.mkdir()
    # write a tiny CSV there
    df0 = pd.DataFrame([{
        "time": "2025-01-01T00:00:00",
        "mag": 4.5,
        "place": "Z",
        "lon": 0.0,
        "lat": 0.0
    }])
    df0.to_csv(fake_cache / "transformed_eq.csv", index=False)

    # monkeypatch the CACHE constant in code.load to point at our fake
    monkeypatch.setattr("code.load.CACHE", fake_cache)

    # now load_data() should pick up our CSV
    df = load_data()
    assert isinstance(df, pd.DataFrame)
    assert df.mag.iloc[0] == 4.5
