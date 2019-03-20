from tile import Creature
from message_strings import IllegalMovement


def is_queen_movement_legal(board, start_coordinate, end_coordinate):
    if end_coordinate not in board.get_neighbouring_coordinates(start_coordinate):
        return False, IllegalMovement.too_far

    if board.get_tile_at(end_coordinate):
        return False, IllegalMovement.tile_at_target

    return shares_exactly_one_neighbour(board, start_coordinate, end_coordinate)


def is_beetle_movement_legal(board, start_coordinate, end_coordinate):
    if end_coordinate not in board.get_neighbouring_coordinates():
        return False, IllegalMovement.too_far

    # If beetle on top of hive, any movement to a neighbouring space is valid
    # Yes, this is a lot of reaching into classes
    if len(board.grid[start_coordinate].stack) > 1:
        return True

    if board.get_tile_at(end_coordinate):
        return True

    return shares_exactly_one_neighbour(board, start_coordinate, end_coordinate)


# If more than one neighbours is shared, the tile cannot fit through the gap
# If no neighbours are shared, the tile cannot move here
def shares_exactly_one_neighbour(board, start_coordinate, end_coordinate):
    shared_neighbours = 0
    for coord in board.get_neighbouring_coordinates(start_coordinate):
        if board.get_tile_at(coord):
            if end_coordinate in board.get_neighbouring_coordinates(coord):
                shared_neighbours += 1

    if shared_neighbours == 0:
        return False, IllegalMovement.too_far
    elif shared_neighbours > 1:
        return False, IllegalMovement.cannot_fit_between_tiles
    else:
        return True


rules = {Creature.QUEEN: is_queen_movement_legal,
         Creature.BEETLE: is_beetle_movement_legal}
