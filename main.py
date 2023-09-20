import random


def input_direction():
    direction = None
    while direction not in ['n', 's', 'e', 'w']:
        direction = input("Enter a direction ('n', 's', 'e' or 'w'): ").lower()
    return direction

def generate_position():
    row = random.randint(0,grid_size-1)
    column = random.randint(0,grid_size-1)
    return row,column


def move_a_square(row, column, direction):
    if direction == 'n':
        row = max(0, row-1)
    elif direction == 's':
        row = min(grid_size-1, row+1)
    elif direction == 'e':
        column = min(grid_size-1, column+1)    
    elif direction == 'w':
        column = max(0, column-1)
    
    return row, column


def is_stuck(row, column, direction):
    return (row, column) == move_a_square(row, column, direction)


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
grid_size = 10
name = input("Robot name: ")
row, column = generate_position()
age = 4
id = 1


message = f'My name is {name} and my id is {id}.'

direction = input_direction()
stop_point = (grid_size-1, grid_size-1)
send_message(row, column, direction, grid_size)


while (row,column) != stop_point:
    row, column = move_a_square(row, column, direction)
    print("Moving one step forward")
    if is_stuck(row, column, direction):
        direction = turn_right(direction)
    send_message(row, column, direction, grid_size)













