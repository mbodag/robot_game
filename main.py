import random
from robot import Robot

def ask_name():
    ''' 
    Prompts the user for the name of the robot and returns it
    '''
    return input("What is the robot's name? ")


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
rob1 = Robot(ask_name())
rob1.navigate()


















