import gradient_descent
import board
import os

def main():

    globalresult = 1
    gd = gradient_descent.subject()
    
    while globalresult > 0:
        os.system('clear')
        gd.gradient_descent()
        queens_coordinates = gd.queens_coordinates()
        number_attacks = int(gd.getFitness())
        ## Print tabuleiro resultado
        print(f'Vetor rainhas: {gd.positions}')
        print(gd.board)
        print(f'\nNúmero de ataques (h) = {int(gd.getFitness())}')
        board.print_queen_board(queens_coordinates, number_attacks)
        globalresult = gd.fitness


if __name__ == "__main__":
    main()
