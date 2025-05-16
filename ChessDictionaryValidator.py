def is_valid_position(pos):
    if len(pos) != 2:
        return False
    column, row = pos[0], pos[1]
    return column in 'abcdefgh' and row in '12345678'

def is_valid_piece(piece):
    valid_pieces = {
        'K', 'Q', 'R', 'B', 'N', 'P',      
        'k', 'q', 'r', 'b', 'n', 'p'     
    }
    return piece in valid_pieces

def validate_chess_dict(chess_dict):
    for position, piece in chess_dict.items():
        if not is_valid_position(position):
            print(f"Invalid position: {position}")
        elif not is_valid_piece(piece):
            print(f"Invalid piece: {piece} at {position}")
        else:
            print(f"Valid move: {piece} at {position}")


chess_board = {
    'a1': 'R', 'b1': 'N', 'c1': 'B', 'd1': 'Q',
    'e1': 'K', 'f1': 'B', 'g1': 'N', 'h1': 'R',
    'a2': 'P', 'b2': 'P', 'c2': 'P', 'd2': 'P',
    'e2': 'P', 'f2': 'P', 'g2': 'P', 'h2': 'P',
    'a9': 'P', 
    'e4': 'X'
}

validate_chess_dict(chess_board)
