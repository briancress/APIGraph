"""Module used to get api data"""

import sys
import http.client
import urllib
from urllib import request, error
import socket


def get_football_data(mode: str):
    """Downloads data from football API with parameter mode
    to determine what data to download"""
    conn = http.client.HTTPSConnection("nfl-team-stats.p.rapidapi.com")
    decoded = ''
    headers = {
        # Enter your API Key
        'X-RapidAPI-Key': "",
        'X-RapidAPI-Host': "nfl-team-stats.p.rapidapi.com"
        }
    try:
        if mode == 'receiving':
            conn.request("GET", "/v1/nfl-stats/teams/receiving-stats/offense/2022", headers=headers)
        elif mode == 'rushing':
            conn.request("GET", "/v1/nfl-stats/teams/rushing-stats/offense/2022", headers=headers)

        res = conn.getresponse()
        data = res.read()
        decoded = data.decode('utf-8')
    except urllib.error.URLError:
        print('Error, could not connect to api server')
        sys.exit()
    except socket.gaierror:
        print('Error, could not connect to api server')
        sys.exit()
    except http.client.ResponseNotReady:
        print('Error with API data, please enter either "rushing" or "receiving"')
        sys.exit()

    return decoded


def get_movie_data(page):
    """Downloads movie data with page to specify which data to download"""
    json_results = ''
    # FIll in your API Key
    url = f'https://api.themoviedb.org/3/movie/top_rated?api_key=YOUR_API_KEY&language=en-US&page={page}'
    try:
        data = urllib.request.urlopen(url)
        json_results = data.read()
    except urllib.error.URLError:
        print('Error, could not connect to api server')
        sys.exit()
    except socket.gaierror:
        print('Error, could not connect to api server')
        sys.exit()

    return json_results
