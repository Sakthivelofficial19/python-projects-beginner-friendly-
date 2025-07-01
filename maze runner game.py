import time

def timing(sec):
    time.sleep(sec)
    return "Time's up! Here you go."

def maze(maze_lst):
    for mazes in maze_lst:
        for maze in mazes:
            print(maze, end=" ")
        print()

print("Here is your maze:")
print('''IT IS A MAZE GAME
--------------
* You need to reach the end from the beginning.
* U - UP
* D - DOWN
* R - RIGHT
* L - LEFT''')

maze_lst = [
    ['S', '|', '°', '°', '|', '|', '°', '|', '°', '|'],
    ['°', '|', '|', '°', '|', '°', '°', '|', '|', '°'],
    ['°', '°', '|', '°', '°', '°', '|', '|', '°', '°'],
    ['|', '°', '|', '|', '|', '°', '|', '°', '|', '|'],
    ['|', '°', '°', '°', '|', '°', '°', '°', '|', '°'],
    ['|', '|', '|', '°', '|', '|', '|', '°', '|', '°'],
    ['°', '°', '|', '°', '°', '°', '°', '°', '|', '°'],
    ['|', '°', '|', '|', '|', '°', '|', '|', '°', '|'],
    ['|', '°', '°', '°', '|', '°', '°', '°', '|', '°'],
    ['|', '|', '|', '°', '|', '|', '|', '°', '°', 'E']]

response = input("Press Enter to play (or 'x' to exit): ")
track_row = range(len(maze_lst))
track_col = range(len(maze_lst[0]))

maze(maze_lst)  # Show only once
print("You have 5 seconds to analyse the maze...")
print(timing(5))

ind1, ind2 = 0, 0
tracer_row, tracer_clm = 0, 0

while True:
    move = input("(U/D/R/L): ").upper()
    match move:
        case "U":
            if maze_lst[ind1][ind2] == "°":
                maze_lst[ind1][ind2] = "•"
            ind1 -= 1
            tracer_row -= 1
            if tracer_row not in track_row or maze_lst[ind1][ind2] == "|":
                print("Oops! Invalid move or you hit a wall. You lose!")
                break
        case "D":
            if maze_lst[ind1][ind2] == "°":
                maze_lst[ind1][ind2] = "•"
            ind1 += 1
            tracer_row += 1
            if tracer_row not in track_row or maze_lst[ind1][ind2] == "|":
                print("Oops! Invalid move or you hit a wall. You lose!")
                break
        case "R":
            if maze_lst[ind1][ind2] == "°":
                maze_lst[ind1][ind2] = "•"
            ind2 += 1
            tracer_clm += 1
            if tracer_clm not in track_col or maze_lst[ind1][ind2] == "|":
                print("Oops! Invalid move or you hit a wall. You lose!")
                break
        case "L":
            if maze_lst[ind1][ind2] == "°":
                maze_lst[ind1][ind2] = "•"
            ind2 -= 1
            tracer_clm -= 1
            if tracer_clm not in track_col or maze_lst[ind1][ind2] == "|":
                print("Oops! Invalid move or you hit a wall. You lose!")
                break
        case _:
            print("Invalid move, try again.")
            continue

    if maze_lst[ind1][ind2] == "E":
        print("Hurray! You won the game!")
        break
