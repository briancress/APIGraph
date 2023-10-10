"""Module used for saving API data to files"""

def file_save(message, mode: str):
    """Takes api data and string as input and
    saves api data to a file that is named based on the string"""

    if mode == 'receiving':
        with open('nfl_receiving_stats_2022.txt', 'w', encoding='utf-8') as file:
            file.write(str(message))

    elif mode == 'rushing':
        with open('nfl_rushing_stats_2022.txt', 'w', encoding='utf-8') as file:
            file.write(str(message))

    elif mode == 'movies':
        with open('top_movies.txt', 'w', encoding='utf-8') as file:
            file.write(str(message))
