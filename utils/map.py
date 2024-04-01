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
    list_of_hospital_name = ['Bệnh viện Tâm Anh',
                             'Bệnh viện Chợ Rẫy',
                             "Bệnh viện Đa khoa Quốc tế Vinmec Central Park",
                             "Bệnh viện Quân đội 175",
                             "Bệnh Viện Đa Khoa Quốc Tế Nam Sài Gòn",
                             "Bệnh viện Nhiệt Đới",
                             "Bệnh viện Phạm Ngọc Thạch",
                             "Bệnh viện Đa khoa khu vực Thủ Đức",
                             "Bệnh viện Quân Dân Y Miền Đông",
                             "Bệnh viện Hoàn Mỹ",
                             "Bệnh viện An Bình",
                             "Bệnh viện đa khoa Lê Văn Việt",
                             "Bệnh viện thành phố Thủ Đức",
                             "Bệnh viện Đa khoa Sài Gòn",
                             "Bệnh viện quận Tân Bình",
                             "Bệnh viện Đại học Y Dược TP.HCM",
                             "Bệnh viện Ung Bướu TP.HCM",
                             "Bệnh viện Đa Khoa Tâm Trí",
                             "Bệnh viện Sài Gòn ITO Phú Thuận",
                             "Bệnh viện Thống Nhất"]
    list_of_hospital_locations = [(10.802585706989044, 106.66604675178056),
                                  (10.75698075, 106.6596804015127),
                                  (10.794472422426885, 106.72023017704245),
                                  (10.81879585, 106.68053605718562),
                                  (10.7360956, 106.6908405011356),
                                  (10.7518286, 106.6839605),
                                  (10.7559516, 106.6650059),
                                  (10.861787233941671, 106.77992295441767),
                                  (10.8444665, 106.7785683),
                                  (10.8000464, 106.68415529525788),
                                  (10.7547449, 106.6709585),
                                  (10.8445906, 106.7902088),
                                  (10.8644079, 106.7455702173566),
                                  (10.772004866444599, 106.6994237461669),
                                  (10.7945273052823, 106.65499398942931),
                                  (10.7551908, 106.6622487),
                                  (10.8051886, 106.6951713),
                                  (10.832052719670008, 106.62188470958347),
                                  (10.797957838504837, 106.67683000080417),
                                  (10.7915574, 106.6527376)]
    list_of_hospital_phone = ["028 7102 6789", "028 3855 4138", "028 3622 1166", "1900 1175",
                              "1800 6767", "028 3923 5804", "028 3855 0207", "028 3722 3556",
                              "028 3730 7125", "028 3990 2468", "028 3923 4260", "028 3897 3628",
                              "0966 331 010" "028 3829 1711", "NA", "NA", "028 3843 3022",
                              "0985 095 100", "028 3844 1399", '028 3844 1399', "028 3869 0277"]
    location_of_hospital = ["2B Đ. Phổ Quang, Phường 2, Tân Bình, Thành phố Hồ Chí Minh",
                            "201B Đ. Nguyễn Chí Thanh, Phường 12, Quận 5, Thành phố Hồ Chí Minh",
                            "208 Đ. Nguyễn Hữu Cảnh, Bình Thạnh, Thành phố Hồ Chí Minh",
                            "786 Đ. Nguyễn Kiệm, Phường 3, Gò Vấp, Thành phố Hồ Chí Minh",
                            "88 Đường Số 8, Bình Chánh, Thành phố Hồ Chí Minh",
                            "764 Đ. Võ Văn Kiệt, Phường 1, Quận 5, Thành phố Hồ Chí Minh",
                            "120 Đ. Hồng Bàng, Phường 12, Quận 5, Thành phố Hồ Chí Minh",
                            "64 Lê Văn Chí, Phường Linh Trung, Thủ Đức, Thành phố Hồ Chí Minh",
                            "50 Lê Văn Việt, Hiệp Phú, Quận 9, Thành phố Hồ Chí Minh",
                            "60-60A Phan Xích Long, Phường 1, Phú Nhuận, Thành phố Hồ Chí Minh",
                            "146 Đ. An Bình, Phường 7, Quận 5, Thành phố Hồ Chí Minh",
                            "387 Lê Văn Việt, Tăng Nhơn Phú A, Thành Phố Thủ Đức, Thành phố Hồ Chí Minh",
                            "29 Phú Châu, Tam Phú, Thủ Đức, Thành phố Hồ Chí Minh",
                            "125 Đ. Lê Lai, Phường Bến Thành, Quận 1, Thành phố Hồ Chí Minh",
                            "605 Đ. Hoàng Văn Thụ, Phường 4, Tân Bình, Thành phố Hồ Chí Minh",
                            "215 Đ. Hồng Bàng, Phường 11, Quận 5, Thành phố Hồ Chí Minh",
                            "47 Nguyễn Huy Lượng, Phường 14, Bình Thạnh, Thành phố Hồ Chí Minh",
                            "171 Đ. Trường Chinh, Tân Thới Nhất, Thành phố Hồ Chí Minh",
                            "140C Nguyễn Trọng Tuyển, Phường 8, Phú Nhuận, Thành phố Hồ Chí Minh",
                            "1 Lý Thường Kiệt, Phường 7, Tân Bình, Thành phố Hồ Chí Minh"]

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
    h = []
    for r in list_of_hospital_locations:
        value = handle_value(coordinate, r)  # Extract the distance (int)
        h.append(value)
    m.add_basemap(BASEMAPS)
    template = Template(open(popup_dir).read())
    for index, station in enumerate(list_of_hospital_locations):
        my_data = {
            'hospital_name': f"{list_of_hospital_name[index]}",
            "hospital_phone": f"{list_of_hospital_phone[index]}",
            "location_of_hospital": f"{location_of_hospital[index]}",
        }
        html = template.render(my_data)
        iframe = folium.IFrame(html,height = 200)
        popup = folium.Popup(iframe, min_width=300, max_width=300)
        m.add_marker(location=list(station), icon=folium.Icon(color='green', icon='hospital', prefix='fa'), popup=popup)
    m.add_marker(location=list(coordinate), icon=folium.Icon(color='red', icon='suitcase', prefix='fa'))
    st.write("The closest: ", list_of_hospital_name[h.index(min(h))],f" which is {round(min(h), 2)} km")
    m.to_streamlit()


if __name__ == "__main__":
    pinpoint()
