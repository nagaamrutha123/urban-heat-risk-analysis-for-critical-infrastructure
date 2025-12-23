import streamlit as st
import geopandas as gpd
import folium
from streamlit.components.v1 import html

st.set_page_config(page_title="Urban Heat Risk", layout="wide")
hospitals = gpd.read_file("bengaluru_hospitals_with_risk.geojson")

st.title("Bengaluru Hospitals Heat Risk Analysis Map")
col1, col2 = st.columns(2)
col1.metric("Total Sites", len(hospitals))
col2.metric("High Risk", (hospitals["Risk_Level"]=="High").sum())

m = folium.Map(location=[12.9716, 77.5946], zoom_start=11, tiles="cartodb dark_matter")
colors = {"High": "red", "Medium": "orange", "Low": "green"}

for _, row in hospitals.iterrows():
    if row.geometry.geom_type == "Point":
        folium.CircleMarker(
            location=[row.geometry.y, row.geometry.x],
            radius=5, color=colors.get(row["Risk_Level"], "gray"),
            fill=True, popup=row["name"]
        ).add_to(m)

html(m._repr_html_(), height=500)
