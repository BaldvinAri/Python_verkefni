import random


# ... add your functions here
def read_board_layout_from_input():
    """
    Asks user how many ladders and snakes should be in the game 
    and which tiles they should be on.
    Returns two lists of snake and ladder tiles
    """
    snake_list = []
    ladder_list = []
    FIRST = 0
    SECOND = 1
    
    snakes_or_ladders = int( input("Number of snakes and ladders: ") )
    for i in range( snakes_or_ladders ):
        get_tiles = input( "Snake/ladder {} leads from where to where: ".format(i+1) ).split()
        get_tiles = list_2_intlist(get_tiles)

        if get_tiles[FIRST] < get_tiles[SECOND]:
            ladder_list.append( get_tiles )
        elif get_tiles[SECOND] < get_tiles[FIRST]:
            snake_list.append( get_tiles )

    return snake_list, ladder_list

def read_player_names_from_input():
    """
    Asks user for two names and returns two strings.
    """
    p1 = input("Name of player 1: ")
    p2 = input("Name of player 2: ")
    return p1, p2

def list_2_intlist(L):
    """
    Takes in a list and returns a new list of integers.
    """
    return [int(obj) for obj in L]

def player_rolled(player, die_roll, current_tile):
    """
    Takes in the player name, roll of the die and the current tile, prints out text and returns
    the new tile the player is on.
    """
    WINNER_TILE = 100
    new_tile = current_tile + die_roll
    if new_tile >= WINNER_TILE:
        new_tile = WINNER_TILE

    print("{} rolled {} and is now at square {}".format(player, die_roll, new_tile ))
    return new_tile


def check_snake_or_ladder(current_tile, player, snakes, ladders):
    """
    Takes in the current tile a player is on, the player name and the tiles of the snakes and ladders
    returns a new tile if a player was on a snake or a ladder tile; otherwise returns the original tile.
    """
    FIRST = 0
    SECOND = 1

    for snake in snakes:
        if snake[FIRST] == current_tile:
            new_tile = snake[SECOND]
            print( "Darn! A bloody snake brought {} down to square {}".format(player, new_tile) )
            return new_tile
            
    for ladder in ladders:
        if ladder[FIRST] == current_tile:
            new_tile = ladder[SECOND]
            print( "Splendid! {} climbed a ladder up to square {}".format(player, new_tile) )
            return new_tile

    return current_tile

            
def whose_turn_to_roll(p1_turn, p2_turn, dice_roll):
    """
    Takes in bool parameters of whose turn it is to roll the dice and the number that
    was rolled.
    if the roll of the dice was 6(the max roll), the player gets to roll again.
    returns the bool of whose turn it is to play.
    """
    MAX_DICE_ROLL = 6
    if dice_roll == MAX_DICE_ROLL:
        return p1_turn, p2_turn

    if p1_turn:
        p1_turn = False
        p2_turn = True
    elif p2_turn:
        p1_turn = True
        p2_turn = False
    
    return p1_turn, p2_turn


def play_game(snakes, ladders, p1, p2):
    """
    Takes a list of snake tiles, a list of ladder tiles and two player names.
    Plays the game of snakes and ladders.
    Returns the name of the winner.
    """
    WINNER_TILE = 100
    p1_turn = True
    p2_turn = False
    p1_tile = p2_tile = 0

    while p1_tile < WINNER_TILE and p2_tile < WINNER_TILE:
        die = roll_die()
        if p1_turn:
            p1_tile = player_rolled(p1, die, p1_tile)
            p1_tile = check_snake_or_ladder(p1_tile, p1, snakes, ladders )

        elif p2_turn:
            p2_tile = player_rolled(p2, die, p2_tile )
            p2_tile = check_snake_or_ladder(p2_tile, p2, snakes, ladders )

        p1_turn, p2_turn = whose_turn_to_roll(p1_turn, p2_turn, die)

    if p1_tile == WINNER_TILE:
        winner = p1
    elif p2_tile == WINNER_TILE:
        winner = p2

    return winner

def declare_winner(winner_name):
    """
    Takes in a name of a player that won the game
    and prints out a string
    """
    print( "{} won the game".format(winner_name) )

    

# DON'T CHANGE THE CODE BELOW
def main():
    # Ensure that games play out deterministically by specifying the random seed.
    # This is needed to ensure that the sequence of die rolls is exactly as expected by the tests in Mimir.
    random.seed(1337)
    snakes, ladders = read_board_layout_from_input()
    player1, player2 = read_player_names_from_input()
    winner = play_game(snakes, ladders, player1, player2)
    declare_winner(winner)


# Make use of this method whenever a player rolls a die
def roll_die() -> int:
    """ Simulate a roll of a 6-sided die """
    return random.randint(1, 6)


main()
