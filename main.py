import random


def run_simulation(grid_size=10, target_row=9, target_column=9):
    name, id, row, column, direction = setup_robot(grid_size)
    print_greeting(name, id)
    navigate_robot(row, column, direction, grid_size, target_row, target_column)
    

    

def setup_robot(grid_size):
    name = input("Robot name: ")
    id = 1
    row, column, direction = generate_position(grid_size)
    return name, id, row, column, direction

def generate_position(grid_size):
    row = random.randint(0,grid_size-1)
    column = random.randint(0,grid_size-1)
    direction = random.choice(['n', 'e', 's', 'w'])
    return row, column, direction

def print_greeting(name,id):
    print(f"Hi, my name is {name}. My ID is {id}")

def navigate_robot(row, column, direction, grid_size, target_row, target_column):
    stop_point = (target_row, target_column)
    send_message(row, column, direction, grid_size)

    while (row,column) != stop_point:
        row, column = move_a_square(row, column, direction, grid_size)
        print("Moving one step forward")
        if is_stuck(row, column, direction, grid_size):
            direction = turn_right(direction)
        send_message(row, column, direction, grid_size)

def move_a_square(row, column, direction, grid_size):
    if direction == 'n':
        row = max(0, row-1)
    elif direction == 's':
        row = min(grid_size-1, row+1)
    elif direction == 'e':
        column = min(grid_size-1, column+1)    
    elif direction == 'w':
        column = max(0, column-1)
    
    return row, column


def is_stuck(row, column, direction, grid_size):
    return (row, column) == move_a_square(row, column, direction, grid_size)


def turn_right(direction):
    list_of_directions = ['n', 'e', 's', 'w']
    for d in range(4):
        if list_of_directions[d] == direction:
            return(list_of_directions[(d+1) % 4])
    print('Turning right')
    

def find_direction_name(direction):
    return {'n': 'North', 'e': 'East', 's': 'South', 'w': 'West'}[direction]


def send_message(row, column, direction, grid_size):
    direction_name = find_direction_name(direction)
    print(f"Current location: ({row},{column}). I am facing {direction_name}")



# Randomise robot name and coordinates
run_simulation()


















