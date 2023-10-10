"""Module used to visualize API data"""

import sys
import json
import matplotlib.pyplot as plt


def plot(data, mode: str):
    """Plots data parameter based on mode parameter"""

    data = json.loads(data)

    if mode == 'receiving':
        teams = []
        yards = []
        try:
            for i in data['_embedded']['teamReceivingStatsList']:
                teams.append(i['name'])

            for i in data['_embedded']['teamReceivingStatsList']:
                yards.append(i['yards'])
        except KeyError:
            print('Error, API data is invalid, check api key')
            sys.exit()

        plt.bar(teams, yards)
        plt.xlabel('Teams')
        plt.ylabel('Yards')
        plt.title('2022 NFL Receiving Yards')
        plt.xticks(rotation='vertical')
        plt.show()

    elif mode == 'rushing':
        teams = []
        yards = []
        try:
            for i in data['_embedded']['teamRushingStatsList']:
                teams.append(i['name'])

            for i in data['_embedded']['teamRushingStatsList']:
                yards.append(i['yards'])
        except KeyError:
            print('Error, invalid API data, check api key')
            sys.exit()
        plt.bar(teams, yards)
        plt.xlabel('Teams')
        plt.ylabel('Yards')
        plt.title('2022 NFL Rushing Yards')
        plt.xticks(rotation='vertical')
        plt.show()
    elif mode == 'movies':

        titles = []
        ratings = []
        try:
            for i in data['results']:
                titles.append(i['title'])
            for i in data['results']:
                ratings.append(i['vote_average'])
        except KeyError:
            print('Invalid API data, check API key')
            sys.exit()

        plt.bar(titles, ratings)
        plt.xlabel('Titles')
        plt.ylabel('Ratings')
        plt.title('Top Movies all Time')
        plt.xticks(rotation='vertical')
        plt.show()
