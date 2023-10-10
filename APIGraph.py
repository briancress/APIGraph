"""Main module for WP4"""

import sys
import api
import visual
import file_io


def main():
    """Main function used for UI and the use of imported modules"""
    print('---------------------------------------------------------')
    print('Welcome to API Data Collector!')
    print('You can get the following data: 2022 NFL Receiving Stats,')
    print('Please enter your desired keyword:')
    print()
    print('"football": 2022 NFL Receiving Stats')
    print('"movies": Top Rated Movies of all Time')
    print('---------------------------------------------------------')
    api_choice = input()

    if api_choice == 'football':
        print('Would you like to see Rushing or Receiving Stats')
        print('Enter "rushing" or "receiving"')
        fb_mode = input()
        data = api.get_football_data(fb_mode)
        file_io.file_save(data, fb_mode)
        visual.plot(data, fb_mode)

    elif api_choice == 'movies':
        print('You can choose which page you want (Each page has 20 movies)')
        print('Example: Page 1 has the top 1-20 movies, Page 2 has top 21-40, etc.')
        print('Type an integer to display which page you desire (Only pages 1-100 are available)')
        page = input()
        try:
            if int(page) > 100:
                print('Error: You can only go up to page 100')
                sys.exit()
        except ValueError:
            print('Error, please enter an integer for page number')
            sys.exit()
        data = api.get_movie_data(page)
        file_io.file_save(data, api_choice)
        visual.plot(data, api_choice)
    else:
        print('No valid input detected')


if __name__ == '__main__':
    main()
