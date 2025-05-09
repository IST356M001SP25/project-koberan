# About My Project

Student Name:  Kobe Sukhatme
Student Email:  kmsukhat@syr.edu


### What it does

This Earthquake Dashboard fetches the last 30 days of worldwide earthquakes (magnitude ≥ 4.0) from the USGS GeoJSON API, transforms and caches the data, then displays an interactive Streamlit dashboard including:

- A **Histogram** of earthquake magnitudes  
- A **Folium map** showing each quake as a circle sized by magnitude  
- A **Sidebar slider** to filter by minimum magnitude  
- A **Data table** of the filtered quakes  

### Folder Structure (full)
IST356_Project/
code/
    init.py
    extract.py # fetch & cache raw GeoJSON
    transform.py # flatten JSON → DataFrame → CSV
    load.py # read CSV → DataFrame
    streamlit_app.py # Streamlit dashboard UI
tests/
    init.py
    test_extract.py
    test_transform.py
    test_load.py
cache/ # holds raw_earthquakes.json & transformed_eq.csv
about-project.md
reflection.md

### Dependencies

bash
pip3 install \
    requests \
    pandas \
    streamlit \
    plotly-express \
    folium \
    streamlit-folium \
    pytest

## How you run my project
1. Fetch & transform the data (optional—Streamlit does this on Refresh):
- python3 code/extract.py
- python3 code/transform.py

2. Run tests to confirm everything is wired up:
- python3 -m pytest -q

3. Launch the dashboard:
- streamlit run code/streamlit_app.py
(IMPORTANT: you may have to refresh data to get the data to load)

### Other things you need to know
The cache/ folder stores intermediate files:

raw_earthquakes.json (the full GeoJSON from USGS)

transformed_eq.csv (filtered & flattened DataFrame)

If you want fresh data, click Refresh Data in the app.

By default the slider is set from magnitude 4.0–8.0; adjust to see different subsets.

All core logic lives in code/ with unit tests under tests/.