import tkinter as tk


def print_queen_board(int_list, number_attacks):
    # Define the size of the chessboard
    board_size = 8
    square_size = 70

    # Create a tkinter window
    window = tk.Tk()
    window.title(f'Chessboard h={number_attacks}')

    # Create a canvas to draw on
    canvas = tk.Canvas(window, width=square_size*board_size,
                       height=square_size*board_size)
    canvas.pack()

    # Function to draw queens at specific squares
    def draw_queens(coords_list):
        img = tk.PhotoImage(file="../images/queen.png").subsample(5)
        for row, col in coords_list:
            canvas.create_image(col*square_size + square_size/2, row*square_size + square_size/2, image=img)
        canvas.image = img

    # Draw the chessboard
    for row in range(board_size):
        for col in range(board_size):
            if (row+col) % 2 == 0:
                canvas.create_rectangle(
                    col*square_size, row*square_size, (col+1)*square_size, (row+1)*square_size, fill="white")
            else:
                canvas.create_rectangle(
                    col*square_size, row*square_size, (col+1)*square_size, (row+1)*square_size, fill="black")

    # Draw queens on squares
    draw_queens([(int_list[0]-1, 0), (int_list[1]-1, 1), (int_list[2]-1, 2), (int_list[3]-1, 3),
                (int_list[4]-1, 4), (int_list[5]-1, 5), (int_list[6]-1, 6), (int_list[7]-1, 7)])

    # Run the tkinter event loop
    window.mainloop()
