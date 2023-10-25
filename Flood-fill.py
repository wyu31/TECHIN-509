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
    #Ensure all the rows of the input board are of the same lengths through assert statements
    for n in input_board:
        if len(n) != len(input_board[0]):
            return("input boards length is not allowed")
    
    if old == new:
        return input_board
    if x < 0 or x >= len(input_board) or y < 0 or y >= len(input_board[0]):
        return
    if input_board[x][y]!= old:
        return input_board
        
    if input_board[x][y] == old:
        # To achieve input_board[x][y] = new
        input_board[x] = input_board[x][:y] + new + input_board[x][y+1:]
        flood_fill(input_board, old, new, x + 1, y)
        flood_fill(input_board, old, new, x - 1, y)
        flood_fill(input_board, old, new, x, y + 1)
        flood_fill(input_board, old, new, x, y - 1)
        return input_board

# change the parameter
modified_board = flood_fill(input_board=board, old=".", new="*", x=2, y=2)

for a in modified_board:
    print(a)
    
