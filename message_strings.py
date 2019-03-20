class IllegalPlacement:
    creature_unavailable = "Player does not have creature available for placement"
    queen_placement_required = "Queen must be played in the first 4 moves"
    space_not_empty = "Tile must be placed in an empty space"
    opponent_tile_adjacent = "Tile cannot be placed touching opponents piece"
    no_friendly_tile_adjacent = "Tile must be placed touching a friendly piece"


class IllegalMovement:
    queen_not_placed = "The queen must be placed before pieces can be moved"
    not_friendly_tile = "The tile selected is not yours"
    hive_not_connected = "Moving this tile would break the hive"
    too_far = "Piece cannot move that far"
    tile_at_target = "There is already a tile there"
    cannot_fit_between_tiles = "Tile cannot slide between neighbouring tiles"
