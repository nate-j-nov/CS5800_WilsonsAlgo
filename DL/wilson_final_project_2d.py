'''
Daryle Lamoureux
CS5800 Fall 2022
Final Project

Wilson's Algorithm Implementation
'''
from random import randint

def choose_direction(x, y, dir):
    '''
    Return a random direction
    '''
    temp_x = x
    temp_y = y
    # Array of tuples with coordinates and direction
    direction = [(x, y-1, 'N'),(x+1, y, 'E'),(x, y+1, 'S'),(x-1, y, 'W')]
    #Randomly pick a direction
    next_dir = direction[randint(0,3)]

    # Use this option if looking for a random direction
    if dir not in ['N','E','S','W']:
        return next_dir
    # Use this if a direction is passed so as not to select the same direction
    else:
        while next_dir[2] == dir:
            x = temp_x
            y = temp_y
            next_dir = direction[randint(0,3)]

    #Return direction and the coordinates that it will reach
    return next_dir

def create_maze(cols, rows):
    '''
    Create a maze
    '''
    maze = [[0 for i in range(cols)] for j in range(rows)]
    # Return a blank maze
    return maze

def starting_point(cols, rows, maze):
    '''
    Set the starting point for the discovery walk
    '''
    # Choose a random starting point
    x = randint(0,cols-1)
    y = randint(0,rows-1)

    # If the starting point is not empty, then continue to select an empty spot is found
    while maze[x][y] != 0:
        x = randint(0,cols-1)
        y = randint(0,rows-1)

    # Return the starting point coordinates
    return (x, y)

def discover_path(cols, rows, maze):
    '''
    Create a path starting at a random point and continue to walk through the
    maze until a previously discovered cell is found
    '''
    walk = True

    # Create a maze to hold the random path
    path = create_maze(cols, rows)

    # Create a random starting point
    start = starting_point(cols, rows, maze)
    # Assign to start_x, start_y to be used in the path walk
    start_x, start_y = start[0], start[1]
    # Assign starting point to current_x, current_y
    current_x, current_y = start_x, start_y
    # Create a path until reaching a previously discovered cell
    while walk:
        legal = False
        # Select a direction and ensure that it is on the board
        while legal is False:
            # Select a random direction
            direction = choose_direction(current_x, current_y, 'Y')
            # Check to see if the move is on the board
            legal = on_board(direction[0], direction[1], cols, rows)
        # Add the selected direction to the path
        path[current_x][current_y] = direction[2]

        # Assign values to next_x, next_y
        next_x, next_y = direction[0], direction[1]
        # Check if the next move is open
        if is_open(next_x, next_y, maze) is False:
            walk = False
            break

        # Check if the next cell has been visited in the discovery walk
        no_visit = is_open(next_x, next_y, path)
        if no_visit is True:
            current_x, current_y = next_x, next_y
        else:
            # Get the opposite direction of the cell
            opp = get_opposite(path[next_x][next_y])
            # Update direction of cell
            path[next_x][next_y] = opp
            # Get original direction
            original = get_opposite(opp)
            legal = False
            # Select new direction until the direction is in the maze
            while legal is False:
                # Make the next step reflect the new direction
                change_direction = choose_direction(next_x, next_y, original)
                legal = on_board(change_direction[0], change_direction[1], cols, rows)
                # Update direction of cell
                path[next_x][next_y] = change_direction[2]
                
            # Assign next_x, next_y to current_x, current_y
            current_x, current_y = next_x, next_y

    # Apply the discovered path to the maze
    result = visited_path(start_x, start_y, path, maze)

    # Return number of visits and the updated maze
    return result[0], result[1]

def get_direction(x, y, dir):
    '''
    Return the coordinates of the next step
    '''
    # Array of tuples with coordinates and direction
    direction = [(x, y-1, 'N'),(x+1, y, 'E'),(x, y+1, 'S'),(x-1, y, 'W')]

    if dir == 'N':
        return (direction[0][0], direction[0][1])
    elif dir == 'E':
        return (direction[1][0], direction[1][1])
    elif dir == 'S':
        return (direction[2][0], direction[2][1])
    else:
        return (direction[3][0], direction[3][1])

def get_opposite(dir):
    '''
    Get the opposite direction
    '''
    if dir == 'N':
        return 'S'
    elif dir == 'S':
        return 'N'
    elif dir == 'E':
        return 'W'
    else:
        return 'E'

def is_open(x, y, maze):
    '''
    Check if a cell is occupied
    '''
    if maze[x][y] != 0:
        return False
    
    return True

def on_board(x, y, cols, rows):
    '''
    Check to see if the next move is within the maze
    '''
    if (x >= 0 and y >= 0 and x <= cols-1 and y <= rows-1):
        return True

    return False

def print_maze(cols, rows, maze):
    '''
    Print the maze
    '''
    for i in range(rows):
        for j in range(cols):
            print(maze[j][i], end=' ')
        print()
    print('\n')

def visited_path(x, y, path, maze):
    '''
    Walk the visited path and update the maze board
    '''
    visits = 0
    walk = True

    # Assign x, y to new_x, new_y
    current_x, current_y = x, y

    # Loop through remainint path until an empty spot is found
    while walk:
        # Add current_x, current_y value to the maze
        maze[current_x][current_y] = path[current_x][current_y]
        # Get the next cell using the current cell's direction value
        direction = get_direction(current_x, current_y, path[current_x][current_y])
        # Assign the coordinates from the direction query to current_x, current_y
        current_x = direction[0]
        current_y = direction[1]
        # If the cell just identified is empty, the end the walk -- otherwise continue the walk
        if path[current_x][current_y] == 0:
            walk = False
        visits += 1

    # Return the number of visits added as well as the updated board
    return visits, maze

def test_create_path(cols, rows):
    '''
    Test data to create a path to ensure functionality works
    '''
    my_path = create_maze(cols, rows)
    my_path[0][0] = 'E'
    my_path[1][0] = 'S'
    my_path[1][1] = 'S'
    my_path[1][2] = 'W'

    print_maze(cols, rows, my_path)

def main():
    '''
    Main function
    '''
    rows = 10
    cols = 10
    unvisited = (rows * cols) - 1

    # Create a new maze
    current_maze = create_maze(cols, rows)

    # Create the "end" point of the maze
    end = starting_point(cols, rows, current_maze)
    x, y = end[0], end[1]
    # Add to the maze
    current_maze[x][y] = 'O'

    # Print initialze maze
    print('Initial maze:')
    print_maze(cols, rows, current_maze)

    while unvisited > 0:
        # Create a new path in the maze
        results = discover_path(cols, rows, current_maze)

        # Print the results of the latest path discovery
        print('Maze with path')
        print_maze(cols, rows, results[1])

        # Deduct the visited cells from the path from the unvisited cells
        unvisited -= results[0]
        print('Remaining unvisited cells: ' + str(unvisited))

    return 0

if __name__ == "__main__":
    main()
