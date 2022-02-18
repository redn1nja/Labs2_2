"""map generator"""
import json
from geopy import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import folium
import twitter2


def generate_json(arg):
    """
    generates a dictionary from Twitter API
    """
    data = twitter2.data_return(arg)
    with open('data.json', 'w')as file:
        json.dump(data, file, indent=4)
    with open('data.json', 'r')as file:
        data_dict = json.load(file)
    return data_dict


def parse_dict(data):
    """
    gets location and names from dictionary of data
    """
    dict_data = {}
    for ele in data['users']:
        dict_data[ele['name']] = ele['location']
    return dict_data


def get_locations(data):
    """
    re-arranges dictionary of places
    """
    geolocator = Nominatim(user_agent='map')
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=0.5)

    for elem in data:
        location = geocode(data[elem], timeout=None)
        try:
            data[elem] = (location.latitude, location.longitude)
        except AttributeError:
            data[elem] = ''

    return data


def create_map(data):
    """
    creates a folium map
    """
    map1 = folium.Map(location=(40, 50), zoom_start=5)
    featgr = folium.FeatureGroup(name='Closest places')
    for item in data:
        if data[item] != '':
            featgr.add_child(folium.Marker(
                location=data[item], popup=folium.Popup(item)))
    map1.add_child(featgr)
    map1.save('templates/map.html')


def main(val):
    """main function"""
    create_map(get_locations(parse_dict(generate_json(val))))
# print(get_locations(parse_dict(generate_json('redn1njaa'))))
# main('redn1njaa')
