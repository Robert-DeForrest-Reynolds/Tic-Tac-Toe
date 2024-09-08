if __name__ == "__main__":
    from sys import argv as Arguments
    from TicTacToeEngine import TicTacToeEngine
    ArgumentsCount = len(Arguments)
    if ArgumentsCount == 2 and Arguments[1].isdigit() == True:
        Engine = TicTacToeEngine(int(Arguments[1]))
    else:
        Engine = TicTacToeEngine(3)