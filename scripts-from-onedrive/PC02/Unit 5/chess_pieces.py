class ChessPiece:
    def __init__(self, symbol, colour, rank, file):
        self.symbol = symbol
        self.colour = colour
        self._position = Position(rank, file)
        
    def get_rank(self):
        return self._position.get_row()
    
    def get_file(self):
        return self._position.get_column()
    
    def __str__(self):
        return f"{self.symbol}, {self.colour}"
    
        
class Pawn(ChessPiece):
    def __init__(self, colour: str, rank, file):
        ChessPiece.__init__(self, "P", colour, rank, file)


class Knight(ChessPiece):
    def __init__(self, colour: str, rank, file):
        ChessPiece.__init__(self, "K", colour, rank, file)


class Rook(ChessPiece):
    def __init__(self, colour: str, rank, file):
        ChessPiece.__init__(self, "R", colour, rank, file)


class Bishop(ChessPiece):
    def __init__(self, colour: str, rank, file):
        ChessPiece.__init__(self, "B", colour, rank, file)


class Queen(ChessPiece):
    def __init__(self, colour: str, rank, file):
        ChessPiece.__init__(self, "Q", colour, rank, file)


class King(ChessPiece):
    def __init__(self, colour: str, rank, file):
        ChessPiece.__init__(self, "C", colour, rank, file)


class Position:
    def __init__(self, row: int, column: int):
        self.__row = row
        self.__column = column
    
    def set_row(self, set_to):
        if 0 <= set_to <= 7:
            self.__row = set_to
        
    def set_column(self, set_to):
        if 0 <= set_to <= 7:
            self.__column = set_to
        
    def get_row(self):
        return self.__row
    
    def get_column(self):
        return self.__column


class ChessBoard:
    def __init__(self):
        self.board = []
        for row in range(8):
            self.row_list = []
            for piece in range(8):
                self.row_list.append("    ")
            self.board.append(self.row_list)
    
    def set_up(self):
        self.board[0][0] = Rook("B", 0, 0)
        self.board[0][1] = Knight("B", 0, 1)
        self.board[0][2] = Bishop("B", 0, 2)
        # add rest of board...

    def __str__(self) -> str:
        result = ""
        for rows in self.board:
            for piece in rows:
                result += "|{}|".format(piece)
            result += "\n"
        return result
                

board = ChessBoard()
board.set_up()
print(board)