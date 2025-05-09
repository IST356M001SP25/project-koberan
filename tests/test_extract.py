import pytest
from code.extract import fetch_earthquakes

def test_fetch_keys(tmp_path, monkeypatch):
    # create a fake JSON response that only has what we need
    fake = {"metadata": {"count": 1}, "features": [{}]}

    # make a tiny dummy response class so .json() and .raise_for_status() behave
    class DummyResponse:
        def __init__(self, data):
            self._data = data
        def raise_for_status(self):
            pass  # pretend everything was OK
        def json(self):
            return self._data

    # patch requests.get inside our extract module to return DummyResponse(fake)
    monkeypatch.setattr(
        "code.extract.requests.get",
        lambda *args, **kwargs: DummyResponse(fake)
    )

    # call the real function; it should pick up our fake response
    data = fetch_earthquakes()

    # check that our stubbed data made it through
    assert "features" in data
    assert data["metadata"]["count"] == 1
