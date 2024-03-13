import random
from robot import Robot
from robot_init import RobotFactory
from board import Board
import pygame
from constants import *
from sprite_object import RobotSprite, Target
import sys


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ricochet Robots!")


def main():
    pygame.init()
    clock = pygame.time.Clock()
    
    #Start game
    game = RobotFactory(GRID_SIZE)
    board = game.board
    robot_group = [robot for robot in board.robots]
    robot_sprite_group = pygame.sprite.Group([robot.repr_sprite for robot in board.robots])
    board.append_targets(TARGETS)
    current_target_sprite = pygame.sprite.Group(board.initiate_random_target())
    board.reset_history()
    currently_selected_robot = None



    run = True
    while run:
        
        clock.tick(FPS)
        event_list = pygame.event.get()
        
        for event in event_list:
            
            if board.robot_is_at_target():
                current_target_sprite = pygame.sprite.Group(board.initiate_random_target())
                #Unselect all robots
                for robot in robot_group:
                    robot.repr_sprite.selected = False
                    currently_selected_robot = None
                board.reset_history()

            if event.type == pygame.QUIT:
                run = False
            
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Select the robot that was clicked on
                pos = pygame.mouse.get_pos()
                clicked_sprites = [robot for robot in robot_group if robot.repr_sprite.rect.collidepoint(pos)]
                if len(clicked_sprites)>0:
                    for robot in robot_group:
                        if robot not in clicked_sprites:
                            robot.repr_sprite.selected = False
                        else:
                            robot.repr_sprite.selected = not robot.repr_sprite.selected
                            if robot.repr_sprite.selected == True:
                                currently_selected_robot = robot
                            else: 
                                currently_selected_robot = None
            
            if event.type == pygame.KEYDOWN:
                #Move the selected robot according to the arrow key that is pressed
                if currently_selected_robot is not None:
                    if event.key == pygame.K_LEFT:
                        currently_selected_robot.direction = 'l'
                        board.make_a_robot_move(currently_selected_robot)
                    if event.key == pygame.K_UP:
                        currently_selected_robot.direction = 'u'
                        board.make_a_robot_move(currently_selected_robot)
                    if event.key == pygame.K_DOWN:
                        currently_selected_robot.direction = 'd'
                        board.make_a_robot_move(currently_selected_robot)
                    if event.key == pygame.K_RIGHT:
                        currently_selected_robot.direction = 'r'
                        board.make_a_robot_move(currently_selected_robot)
                    currently_selected_robot.update_sprite()
                if event.key == pygame.K_u and len(board.history) > 1:
                    for robot_idx in range(len(board.robots)):
                        loop_robot = board.robots[robot_idx]
                        loop_robot.position = board.history[-2][robot_idx]
                        loop_robot.update_sprite()
                    board.history = board.history[:-1]
                    board.current_move_count -= 1


        board.draw_board(WIN)
        current_target_sprite.draw(WIN)
        robot_sprite_group.update()
        robot_sprite_group.draw(WIN)
        
        pygame.display.update()
    pygame.quit()
    
if __name__ == '__main__':
    main()
