# Urban Heat Risk Analysis for Critical Infrastructure

## Overview
This project develops a geospatial decision-support tool to identify and prioritise
hospitals in Bengaluru that are relatively more vulnerable to extreme heat.

The analysis combines infrastructure location data with an explainable risk-scoring
framework to support urban resilience and planning decisions.

## Methodology
Risk is assessed using three components:
- Exposure (relative heat stress proxy)
- Sensitivity (criticality of hospitals)
- Adaptive Capacity (proxy for local cooling support)

Risk Score = (Exposure × Sensitivity) − Adaptive Capacity

This framework is designed for prioritisation, not prediction.

## Outputs
- Interactive Folium map visualising hospital risk levels
- Streamlit application for decision-support exploration

## Tools
Python, GeoPandas, OSMnx, Folium, Streamlit

## Running the App
The Streamlit app is designed to be run locally or deployed via Streamlit Cloud.

```bash
pip install -r requirements.txt
streamlit run app.py
