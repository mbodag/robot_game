import random
from board import Board
from constants import *
from sprite_object import RobotSprite

class Robot:


    def __init__(self, name, id, position, direction, board: Board, color = (0,0,0)) -> None:
        self.id = id
        self.name = name
        self.board = board
        self.position = position
        self.direction = direction
        self.target = (9,9)
        self.color = color
        self.screen_position = (40 + SQUARE_SIZE* (self.position[1]+ 1/2), 40 + SQUARE_SIZE* (self.position[0]+ 1/2))
        self.repr_sprite = RobotSprite(*self.screen_position,self.color)

    def __repr__(self):
        return (f"{self.name}, id = {self.id}")
    
    def move_a_square(self):
        '''
        Moves robot forward by one square in its current direction
        If the robot is facing the edge of the board it remains in the same position
        '''
        row = self.position[0]
        column = self.position[1]
        if self.direction == 'u':
            row = max(0, row-1)
        elif self.direction == 'd':
            row = min(self.board.grid_size-1, row+1)
        elif self.direction == 'r':
            column = min(self.board.grid_size-1, column+1)    
        elif self.direction == 'l':
            column = max(0, column-1)
        self.position = (row, column)

    def update_sprite(self):
        self.repr_sprite.x, self.repr_sprite.y = (40 + SQUARE_SIZE* (self.position[1]+ 1/2), 40 + SQUARE_SIZE* (self.position[0]+ 1/2))
    
    def test_move_a_square(self):
        '''
        Moves robot forward by one square in its current direction
        If the robot is facing the edge of the board it remains in the same position
        '''
        before_row = self.position[0]
        before_column = self.position[1]
        if self.direction == 'u':
            after_row = max(0, before_row-1)
            after_column = before_column
        elif self.direction == 'd':
            after_row = min(self.board.grid_size-1, before_row+1)
            after_column = before_column
        elif self.direction == 'r':
            after_column = min(self.board.grid_size-1, before_column+1)    
            after_row = before_row
        elif self.direction == 'l':
            after_column = max(0, before_column-1)
            after_row = before_row
        return ((before_row, before_column),(after_row, after_column))

    def move_forward_to_obstacle(self):
        '''
        Robot moves in its direction until it reaches a wall
        '''
        while self.board.is_legal_move(self,self.direction):
            self.move_a_square()


    def is_facing_edge(self):
        '''
        Checks if the robot is facing a wall
        Returns a boolean
        '''
        facing_north_wall = self.position[0] == 0 and self.direction == 'u'
        facing_south_wall = self.position[0] == self.board.grid_size-1 and self.direction == 'd'
        facing_east_wall = self.position[1] == 0 and self.direction == 'l'
        facing_west_wall = self.position[1] == self.board.grid_size - 1 and self.direction == 'r'
        
        return facing_north_wall or facing_south_wall or facing_west_wall or facing_east_wall



if __name__ == "__main__":
    pass