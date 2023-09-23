import random

class Robot:


    def __init__(self, name, id, position, direction, grid_size) -> None:
        self.id = id
        self.name = name
        self.grid_size = grid_size
        self.position = position
        self.direction = direction
        self.target = (9,9)

    def __repr__(self):
        return (f"{self.name}, id = {self.id}")
    
    def turn_right(self):
        '''Changes robot direction to the one 90 degrees clockwise'''
        directions = ['n', 'e', 's', 'w']
        idx = directions.index(self.direction)
        self.direction = directions[(idx+1)%4]
    
    def move_a_square(self):
        '''
        Moves robot forward by one square in its current direction
        If the robot is facing the edge of the board it remains in the same position
        '''
        row = self.position[0]
        column = self.position[1]
        if self.direction == 'n':
            row = max(0, row-1)
        elif self.direction == 's':
            row = min(self.grid_size-1, row+1)
        elif self.direction == 'e':
            column = min(self.grid_size-1, column+1)    
        elif self.direction == 'w':
            column = max(0, column-1)
        self.position = (row, column)

    def move_forward_to_wall(self):
        '''
        Robot moves in its direction until it reaches a wall
        '''
        while not self.is_facing_wall():
            self.move_a_square()


    def is_facing_wall(self):
        '''
        Checks if the robot is facing a wall
        Returns a boolean
        '''
        facing_north_wall = self.position[0] == 0 and self.direction == 'n'
        facing_south_wall = self.position[0] == self.grid_size-1 and self.direction == 's'
        facing_east_wall = self.position[1] == 0 and self.direction == 'w'
        facing_west_wall = self.position[1] == self.grid_size - 1 and self.direction == 'e'
        
        return facing_north_wall or facing_south_wall or facing_west_wall or facing_east_wall

    def is_at_target(self):
        '''
        Returns whether the robot is at its target
        '''
        return self.position == self.target


    def navigate(self):
        '''
        The robot moves forward until it reaches a wall then turns right, and does so until it reaches its target
        '''
        counter = 0
        while not self.is_at_target():
            self.move_forward_to_wall()
            print(self.position, self.direction)
            self.turn_right()
            counter +=1


    def print_greeting(self):
        '''
        Prints a greeting including the robot's name and id
        '''
        print(f"Hi, my name is {self.name}. My ID is {self.id}")


if __name__ == "__main__":
    jj = Robot('jj')
    jj.navigate()
    print(jj)
        

        