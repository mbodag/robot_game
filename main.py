import random
from robot import Robot
from robot_init import RobotFactory


def find_direction_name(direction):
    '''
    Returns the full name of the direction
    '''
    return {'n': 'North', 'e': 'East', 's': 'South', 'w': 'West'}[direction]


def send_message(row, column, direction):
    '''
    Send the user a message with the current location and direction
    '''
    direction_name = find_direction_name(direction)
    print(f"Current location: ({row},{column}). I am facing {direction_name}")



# Randomise robot name and coordinates
fac1 = RobotFactory()
robots = fac1.create_robots(4)
for rob in robots:
    print(rob)




















