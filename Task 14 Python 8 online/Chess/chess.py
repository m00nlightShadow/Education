class ChessPiece:
    WHITE = 'white'
    BLACK = 'black'

    def __init__(self, name, color, position):
        self.name = name
        self.color = color
        self.position = position

    def change_color(self):
        self.color = self.BLACK if self.color == self.WHITE else self.WHITE

    def change_position(self, changed_position):
        x, y = changed_position
        if 0 <= x <= 7 and 0 <= y <= 7:
            self.position = changed_position
        else:
            print("Out of board")

    def accessible_moves(self):
        ...


class Pawn(ChessPiece):
    def accessible_moves(self):
        x, y = self.position
        moves = [(x + 1, y), (x + 2, y)] if self.color == "white" else [(x - 1, y), (x - 2, y)]
        valid_moves = [(x, y) for x, y in moves if 0 <= x <= 7 and 0 <= y <= 7]
        return valid_moves


class Knight(ChessPiece):
    def accessible_moves(self):
        x, y = self.position
        moves = [(x + 2, y + 1), (x + 2, y - 1), (x + 1, y + 2), (x + 1, y - 2),
                 (x - 2, y + 1), (x - 2, y - 1), (x - 1, y + 2), (x - 1, y - 2)]
        valid_moves = [(x, y) for x, y in moves if 0 <= x <= 7 and 0 <= y <= 7]
        return valid_moves


class Bishop(ChessPiece):
    def accessible_moves(self):
        x, y = self.position
        moves = [(x + i, y + i) for i in range(-7, 8) if i != 0] + [(x + i, y - i) for i in range(-7, 8) if i != 0]
        valid_moves = [(x, y) for x, y in moves if 0 <= x <= 7 and 0 <= y <= 7]
        return valid_moves


class Rook(ChessPiece):
    def accessible_moves(self):
        x, y = self.position
        moves = [(x+i, y) for i in range(-7, 8) if i != 0] + [(x, y+i) for i in range(-7, 8) if i != 0]
        valid_moves = [(x, y) for x, y in moves if 0 <= x <= 7 and 0 <= y <= 7]
        return valid_moves


class Queen(ChessPiece):
    def accessible_moves(self):
        x, y = self.position
        moves = [(x+i, y+i) for i in range(-7, 8) if i != 0] + [(x+i, y-i) for i in range(-7, 8) if i != 0]
        moves += [(x+i, y) for i in range(-7, 8) if i != 0] + [(x, y+i) for i in range(-7, 8) if i != 0]
        valid_moves = [(x, y) for x, y in moves if 0 <= x <= 7 and 0 <= y <= 7]
        return valid_moves


class King(ChessPiece):
    def accessible_moves(self):
        x, y = self.position
        moves = [(x+i, y+j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]
        valid_moves = [(x, y) for x, y in moves if 0 <= x <= 7 and 0 <= y <= 7]
        return valid_moves


def changed_pos_pieces(pieces, position):
    reachable = []
    for piece in pieces:
        if position in piece.accessible_moves():
            reachable.append(piece)
    return reachable


# Example usage
pawn_white = Pawn('white pawn', "white", (2, 3))
pawn_black = Pawn('black pawn', "black", (5, 4))
knight_black = Knight('black knight', "black", (6, 3))
rook_white = Rook('white rook', 'white', (1, 4))
bishop_black = Bishop('black bishop', 'black', (2, 6))
king_white = King('white king', 'white', (5, 3))
queen_black = Queen('black queen', 'black', (6, 6))
my_pieces = [pawn_white, pawn_black, knight_black, rook_white, bishop_black, king_white, queen_black]

target_position = (4, 4)
reachable_pieces = changed_pos_pieces(my_pieces, target_position)
print("Reachable pieces:", [piece.name for piece in reachable_pieces])
