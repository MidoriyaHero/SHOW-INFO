import streamlit.components.v1 as components
import os
import time
import streamlit as st
from jinja2 import Template
import folium
from streamlit_geolocation import streamlit_geolocation
import leafmap.foliumap as leafmap
import base64
from geopy.distance import geodesic
TRAVEL_OPTIMIZER = ['Length', 'Time']
BASEMAPS = "OpenStreetMap"
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="MyApp", timeout = 5)
from jinja2 import Template
parent_dir = os.path.dirname(os.path.abspath(__file__))
popup_dir = os.path.join(parent_dir, "my_map.html")
def pinpoint():
    location = streamlit_geolocation(key=1)
    if location['latitude'] and location['longitude'] is not None:
        coordinate = (location['latitude'], location['longitude'])
    else:
        coordinate = (10.877600593377078, 106.80162093651423)
   
    # reverse_location = geolocator.reverse(coordinate)

    # # Traverse the data
    # address = reverse_location.raw['address']
    # print(address)
    # amenity_address = address.get("amenity", '')
    # road_address = address.get("road", '')
    # quarter_address = address.get('state', '')
    # suburb_address = address.get('suburb', '')
    # city_address = address.get('county', '')
    # country_address = address.get('country', '')

    st.write("Address: International University")
    st.write("Suburb & State: Phường Đông Hòa, Tỉnh Bình Dương")
    st.write("City: Thành phố Dĩ An")
    st.write("Country: Việt Nam")
    m = leafmap.Map(center=coordinate, zoom=13)
    m.add_basemap(BASEMAPS)

    m.add_marker(location=list(coordinate), icon=folium.Icon(color='red', icon='suitcase', prefix='fa'))
    m.to_streamlit()
if __name__ == "__main__":
    pinpoint()
