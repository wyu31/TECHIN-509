board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]


def flood_fill(input_board, old, new, x, y):

    if (x < 0 or x > 7 or y < 0 or y > 21 or board[x][y] == new_value):
        return

    if board[x][y] != old_value:
        return
    
    board[x][y] = new_value

    flood_fill(input_board, old, new, x + 1, y)
    flood_fill(input_board, old, new, x - 1, y)
    flood_fill(input_board, old, new, x, y + 1)
    flood_fill(input_board, old, new, x, y - 1)

# change the parameter
modified_board = flood_fill(input_board=board, old=".", new="*", x=1, y=1)

for a in modified_board:
    print(a)
    
#Ensure all the rows of the input board are of the same lengths through assert statements
for n in input_board:
        if len(n) != len(input_board[0]):
            return("input boards length is not allowed")
