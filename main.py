from typer import Typer

from Game import TicTacToe

app = Typer()


@app.command()
def main(pruning: bool = True):
    game = TicTacToe(pruning)
    print("Give your move with this format: i j")
    while True:
        game.show_board()
        value, move = game.find_best_move()
        print(f"Best move is {move[0]+1}, {move[1]+1} with {value} value.")
        i, j = map(int, input("Now whats your move? ").split())
        state = game.move(i-1, j-1)
        if state:
            break

    game.show_board()
    print(game.counter)


if __name__ == "__main__":
    app()
