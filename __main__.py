if __name__ == "__main__":
    from sys import argv as Arguments
    from TicTacToeEngine import TicTacToeEngine
    ArgumentsCount = len(Arguments)
    if ArgumentsCount == 2 and Arguments[1].isdigit() == True:
        if int(Arguments[1]) > 9:
            print("Maximum board size is 9. Defaulting to 3.")
            Engine = TicTacToeEngine(3)
        else:
            Engine = TicTacToeEngine(int(Arguments[1]))
    else:
        Engine = TicTacToeEngine(3)