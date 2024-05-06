import streamlit.components.v1 as components
import os
import time
import streamlit as st
from jinja2 import Template
import folium
from streamlit_geolocation import streamlit_geolocation
import leafmap.foliumap as leafmap
import base64
TRAVEL_OPTIMIZER = ['Length', 'Time']
BASEMAPS = "OpenStreetMap"
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="MyApp", timeout = 5)
from jinja2 import Template
parent_dir = os.path.dirname(os.path.abspath(__file__))
popup_dir = os.path.join(parent_dir, "my_map.html")
from geopy.distance import geodesic

def handle_value(initial_value, loc_hos):

    dist = geodesic(initial_value, loc_hos).km
    return dist
def pinpoint():

    location = streamlit_geolocation(key=1)
    if location['latitude'] and location['longitude'] is not None:
        coordinate = (location['latitude'], location['longitude'])
    else:
        coordinate = (10.877600593377078, 106.80162093651423)
    
    #xóa đoạn này
    key_map ={'center': coordinate,
              'zoom':12,
              'height':20
              }
    m = leafmap.Map(**key_map)
    m.add_basemap(BASEMAPS)
    m.add_marker(location=list(coordinate), icon=folium.Icon(color='red', icon='suitcase', prefix='fa'))
    m.to_streamlit()


if __name__ == "__main__":
    pinpoint()
