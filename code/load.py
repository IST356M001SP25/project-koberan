# code/load.py
import pandas as pd
from pathlib import Path

# same place again
CACHE = Path(__file__).parent.parent / "cache"

def load_data():
    """
    Read the cleaned CSV from cache into a DataFrame and return it.
    """
    return pd.read_csv(CACHE / "transformed_eq.csv")

if __name__=="__main__":
    # sanity check
    print(load_data().head())
