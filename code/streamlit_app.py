# code/streamlit_app.py
import streamlit as st
import plotly.express as px
import folium
from streamlit_folium import st_folium

from extract import fetch_earthquakes
from transform import transform_earthquakes
from load import load_data

st.title("🌎 Earthquake Dashboard")

# refresh button to re-pull & re-process the latest data
if st.button("🔄 Refresh Data"):
    raw = fetch_earthquakes()
    df = transform_earthquakes(raw)
else:
    df = load_data()  # load existing CSV if we already have it

# let the user pick the minimum magnitude to display
min_mag = st.sidebar.slider("Min Magnitude", min_value=4.0, max_value=8.0, value=4.0)
df = df[df.mag >= min_mag]

# show a histogram of quake magnitudes
fig = px.histogram(df, x="mag", nbins=20, title="Magnitude Distribution")
st.plotly_chart(fig, use_container_width=True)

# build a Folium map centered on the average location
m = folium.Map(location=[df.lat.mean(), df.lon.mean()], zoom_start=2)
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row.lat, row.lon],
        radius=row.mag * 2,
        popup=row.place
    ).add_to(m)

# render the interactive map
st_folium(m, width=700)

# and finally, show the raw DataFrame at the bottom
st.dataframe(df)
