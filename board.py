import pygame
from constants import *
import random
from sprite_object import Target

class Board:
    def __init__(self, grid_size) -> None:
        self.grid_size = grid_size
        self.robots = []
        self.targets = [] #((row,col), color)
        self.previous_targets = set()
        self.current_move_count = 0
        self.current_target = None
        self.disallowed_moves = disallowed_moves
        self.barriers = self.disallowed_moves.copy()
        reversed_disallowed = [(end, start) for (start,end) in self.disallowed_moves]
        self.disallowed_moves += reversed_disallowed
        self.history = []
        
    def has_space(self):
        for row in range(self.grid_size):
            for column in range(self.grid_size):
                if not self.square_has_robot(row, column):
                    return True
        return False

    def take_snapshot(self):
        snapshot = []
        for robot in self.robots:
            snapshot.append(robot.position)
        return snapshot

    def reset_history(self):
        self.history = [self.take_snapshot()]

    def initiate_target(self):
        self.current_target = random.choice(self.targets)
        while self.robot_is_at_target():
            self.current_target = random.choice(self.targets)
        target_sprite = Target(62+self.current_target[0][1]*SQUARE_SIZE,62+self.current_target[0][0]*SQUARE_SIZE, self.current_target[1].color)
        return target_sprite

    def initiate_random_target(self):
        self.current_target = ((random.randint(0,15), random.randint(0,15)), random.choice(self.robots))
        while self.robot_is_at_target() or self.current_target[0] in [(7,7),(7,8),(8,7),(8,8)]:
            self.current_target = random.choice(self.targets)
        target_sprite = Target(62+self.current_target[0][1]*SQUARE_SIZE,62+self.current_target[0][0]*SQUARE_SIZE, self.current_target[1].color)
        return target_sprite
    
    def append_targets(self, targets):
        #((row,col), robot_id)
        for target in targets:
            for robot in self.robots:
                if robot.id == target[1]:
                    self.targets.append((target[0],robot))

            



    def square_has_robot(self,row, column):
        for robot in self.robots:
            if robot.position == (row, column):
                return True
        return False
    
    def is_legal_move(self, robot, direction):
        robot.direction = direction
        if robot.is_facing_edge():
            return False
        elif robot.test_move_a_square() in self.disallowed_moves:
            return False
        elif self.square_has_robot(*robot.test_move_a_square()[1]):
            return False
        return True
    
    def make_a_robot_move(self, robot):
        direction = robot.direction
        if self.is_legal_move(robot, direction):
            robot.move_forward_to_obstacle()
            self.current_move_count += 1
            self.history.append(self.take_snapshot())

    

    def robot_is_at_target(self):
        return self.current_target[1].position == self.current_target[0]
    

    def draw_board(self, win):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                pygame.draw.rect(win, WHITE, (40+col*SQUARE_SIZE, 40+row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.rect(win, LIGHT_GREY, (40+col*SQUARE_SIZE, 40+row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),2)
        for barrier in self.barriers:
            first_square = barrier[0]
            second_square = barrier[1]
            if (first_square[0], first_square[1]+1) == (second_square[0], second_square[1]):
                pygame.draw.rect(win, BROWN, (38+second_square[1]*SQUARE_SIZE, 38+second_square[0]*SQUARE_SIZE, 4,SQUARE_SIZE+4))
            elif (first_square[0]+1, first_square[1]) == (second_square[0], second_square[1]):
                pygame.draw.rect(win, BROWN, (38+second_square[1]*SQUARE_SIZE, 38+second_square[0]*SQUARE_SIZE, SQUARE_SIZE+4, 4))


