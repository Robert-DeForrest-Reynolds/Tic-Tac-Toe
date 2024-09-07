class TicTacToeEngine:
    def __init__(Self, Size) -> None:
        Self.Size = Size
        Self.Build_Board()
        Self.Winner, Self.Loser = None, None
        Self.PlayerOne = "X"
        Self.PlayerTwo = "O"
        Self.CurrentPlayer = Self.PlayerOne
        Self.CurrentMove = None
        
        while [Self.Winner, Self.Loser] == [None, None]:
            Self.User_Turn()
            Self.Render_Board()
            if Self.CurrentPlayer == Self.PlayerOne:
                Self.CurrentPlayer = Self.PlayerTwo
            else:
                Self.CurrentPlayer = Self.PlayerOne


    def Build_Board(Self) -> None:
        Self.Board = {}
        for Y in range(Self.Size):
            Self.Row = {}
            for X in range(Self.Size):
                Self.Row.update({(X):"~"})
            Self.Board.update({Y:Self.Row})


    def User_Turn(Self, OutOfBounds=False, SpotTaken=False) -> None:
        if OutOfBounds == True:
            print("You're previous move was not within the bounds of the board.\n")
        if SpotTaken == True:
            print("That position is taken already.")
        UserMove = input(f"Alright {Self.CurrentPlayer}'s, what is your move? (Formatting: RowNumber, ColumnNumber)\n")
        MovePosition = UserMove.split(",")
        MoveY, MoveX = int(MovePosition[0])-1, int(MovePosition[1])-1
        Self.CurrentMove = [MoveY, MoveX]
        if MoveY > Self.Size-1 or MoveY < 0 or MoveX > Self.Size-1 or MoveX < 0:
            Self.User_Turn(WarnOutOfBoundsing=True)
        elif Self.Board[MoveY][MoveX] in ["X", "O"]:
            Self.User_Turn(SpotTaken=True)
        else:
            Self.Board[MoveY][MoveX] = Self.CurrentPlayer


    def Render_Board(Self) -> None:
        InitialFormat = "\n".join([f"| {" ".join([Position for Position in Self.Board[Row].values()])} |" for Row in Self.Board])
        InitialFormat = "\n".join([f"{Index + 1} {Line}" for Index, Line in enumerate(InitialFormat.split("\n"))])
        Render = "    " + " ".join([str(Number + 1) for Number in range(Self.Size)]) + "\n" + InitialFormat
        print(Render)