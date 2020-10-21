RANK = 0
COUNTRY = 1
RATING = 2
BYEAR = 3


def open_file(filename):
    try:
        return open(filename,"r")
    except FileNotFoundError:
        return

def create_players_dict(file_stream):
    the_dict = {}
    for line in file_stream:
        rank, name, country, rating, byear = line.strip().split(";")
        last_name, first_name = name.split(",")
        first_name = first_name.strip()
        last_name = last_name.strip()
        key = f"{first_name} {last_name}"
        value_tuple = (int(rank), country.strip(), int(rating), int(byear))
        the_dict[key] = value_tuple
    return the_dict

def create_countries_dict( dict_players ):
    country_dict = {}

    for chess_player, chess_player_data in dict_players.items():
        country = chess_player_data[COUNTRY]

        if country not in country_dict:
            country_dict[country] = [chess_player]
        else:
            name_list = country_dict[country]
            name_list.append(chess_player)

    return country_dict

def create_year_dict( dict_players ):
    year_dict = {}

    for chess_player, chess_player_data in dict_players.items():
        year = chess_player_data[BYEAR]

        if year not in year_dict:
            year_dict[year] = [chess_player]
        else:
            name_list = year_dict[year]
            name_list.append(chess_player)

    return year_dict


def print_header(header_str):
    print(header_str)
    dashes = "-" * len(header_str)
    print(dashes)

def get_average_rating(players, dict_players):
    ratings = [dict_players[player][RATING] for player in players]
    average = sum(ratings)/len(ratings)
    return average

def print_sorted(dict_, dict_players):
    # get average for country
    sorted_ = sorted(dict_.items())
    for key,players in sorted_:
        print(f"{key} ({len(dict_[key])}) ({get_average_rating(players, dict_players):.1f}):")
        for player in players:
            rating = dict_players[player][RATING]
            print("{:>40}{:>10d}".format(player, rating))


# Lesa skrá
filename = input("Enter filename: ")
file_stream = open_file( filename )
if file_stream:
    # splitta upp skrá
    # seta í uppflettitöflu
    # flokka eftir 3-staki í röð
    dict_players = create_players_dict( file_stream )
    dict_countries = create_countries_dict( dict_players )
    dict_years = create_year_dict( dict_players )

    # prenta út
    print_header("Players by country:")
    print_sorted(dict_countries, dict_players)
    print()
    print_header("Players by birth year:")
    print_sorted(dict_years, dict_players)


    # error tékka
