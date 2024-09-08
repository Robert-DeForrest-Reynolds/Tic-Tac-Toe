class TicTacToeEngine:
    def __init__(Self, Size) -> None:
        Self.Size = Size
        Self.Build_Board()
        Self.Winner = None
        Self.PlayerOne = "X"
        Self.PlayerTwo = "O"
        Self.CurrentPlayer = Self.PlayerOne
        Self.CurrentMove = None
        Self.WinningCases = {"X" * Self.Size:"X",
                             "O" * Self.Size:"O",}
        
        while Self.Winner == None:
            Self.Render_Board()
            Self.User_Turn()
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


    def Check_If_Winning_Row(Self) -> bool:
        Row = Self.Board[Self.CurrentMove[0]]
        MatchCase ="".join([Character for Character in Row.values()])
        if MatchCase in Self.WinningCases.keys():
            Self.Winner = Self.WinningCases[MatchCase]
            return True
        return False


    def Check_If_Winning_Column(Self) -> bool:
        MatchCase = "".join([list(Self.Board[Row].values())[Self.CurrentMove[1]] for Row in Self.Board])
        if MatchCase in Self.WinningCases.keys():
            Self.Winner = Self.WinningCases[MatchCase]
            return True
        return False


    def Check_If_Winning_Diagonals(Self) -> bool:
        MatchCaseLeft = "".join([list(Self.Board[Row].values())[Index] for Index, Row in enumerate(Self.Board)])
        MatchCaseRight = "".join([list(Self.Board[Row].values())[(Self.Size - 1) - Index] for Index, Row in enumerate(Self.Board)])
        if MatchCaseLeft in Self.WinningCases.keys():
            Self.Winner = Self.WinningCases[MatchCaseLeft]
            return True
        if MatchCaseRight in Self.WinningCases.keys():
            Self.Winner = Self.WinningCases[MatchCaseRight]
            return True
        return False


    def Check_If_Winning_Board(Self) -> bool:
        if Self.Check_If_Winning_Row():
            return True
        if Self.Check_If_Winning_Column():
            return True
        if Self.Check_If_Winning_Diagonals():
            return True
        return False


    def User_Turn(Self, OutOfBounds=False, SpotTaken=False, InvalidInput=False) -> None:
        if OutOfBounds == True:
            print("You're previous move was not within the bounds of the board.\n")
            Self.Render_Board()
        if SpotTaken == True:
            print("That position is taken already.")
            Self.Render_Board()
        if InvalidInput == True:
            print("Invalid input. Formatting: RowNumber, ColumnNumber. Example: 2,3")
            Self.Render_Board()
        UserMove = input(f"Alright {Self.CurrentPlayer}'s, what is your move?\n")
        MovePosition = UserMove.split(",")
        if len(MovePosition) != 2 or MovePosition[0].isdigit() == False or MovePosition[1].isdigit() == False:
            Self.User_Turn(InvalidInput=True)
            return
        MoveY, MoveX = int(MovePosition[0])-1, int(MovePosition[1])-1
        Self.CurrentMove = [MoveY, MoveX]
        if MoveY > Self.Size-1 or MoveY < 0 or MoveX > Self.Size-1 or MoveX < 0:
            Self.User_Turn(WarnOutOfBoundsing=True)
            return
        elif Self.Board[MoveY][MoveX] in ["X", "O"]:
            Self.User_Turn(SpotTaken=True)
            return
        else:
            Self.Board[MoveY][MoveX] = Self.CurrentPlayer
        
        if Self.Check_If_Winning_Board() == True:
            print(f"{Self.Winner} has won!")
            Self.Render_Board()


    def Render_Board(Self) -> None:
        InitialFormat = "\n".join([f"| {" ".join([Position for Position in Self.Board[Row].values()])} |" for Row in Self.Board])
        InitialFormat = "\n".join([f"{Index + 1} {Line}" for Index, Line in enumerate(InitialFormat.split("\n"))])
        Render = "    " + " ".join([str(Number + 1) for Number in range(Self.Size)]) + "\n" + InitialFormat
        print(Render)