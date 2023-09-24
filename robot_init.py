from robot import Robot
import random
from board import Board

class RobotFactory:
    
    factory_instances = 0

    def __init__(self, grid_size = 10, 
                names = ["Wall-E", "R2D2", "C3PO", "Gaios"], 
                random_direction = True, random_position = True, unique_positions = True) -> None:
        '''
        Initialises a robot factory

        ---
        grid_size: The size of the n*n grid the robots are placed on.
        names: list[str] The list of robot names. Created robots will adopt these names in the order of the list. 
        Once the list is over, the user will be prompted for names.

        random_direction (bool): The robot's direction is chosen at random instead of prompted
        random_position (bool): The robot's position is chosen at random instead of prompted
        unique_positions (bool): A robot's position cannot the be same as any other robot in the factory

        '''
        self.robot_instances = 0
        self.names = names
        self.random_direction = random_direction
        self.random_position = random_position
        self.factory_id = self.factory_instances * 10000
        RobotFactory.factory_instances += 1
        self.unique_positions = unique_positions
        self.board = Board(grid_size)

        

    def create_robots(self, quantity):
        robots = []
        for i in range(quantity):
            new_robot = self.initialise_robot()
            if new_robot is not None:
                robots.append(new_robot)
            else: 
                break
        return robots
    
    def initialise_robot(self):
        if self.board.has_space():
            name = self._generate_name()
            id = self.robot_instances + self.factory_id
            direction = self._generate_direction()
            if self.unique_positions:
                same_position = True
                while same_position == True:
                    position = self._generate_position()
                    same_position = False
                    for robot in self.board.robots:
                        if robot.position == position:
                            same_position = True
            else:
                position = self._generate_position
            self.robot_instances += 1
            new_robot = Robot(name, id, position, direction, self.board)
            self.board.robots.append(new_robot)
            return new_robot
        else: 
            print("Maximum robot limit reached")
            return None

    def _generate_name(self):
        try:
            robot_name = self.names[self.robot_instances]
        except:
            robot_name = input("What is the robot's name? ")
        return robot_name

    
    def _generate_direction(self):
        if self.random_direction:
            return random.choice(['u','d','l','r'])
        else:
            input_direction = None
            while input_direction not in ['u','d','l','r']:
                    input_direction = input("What is the direction? (u|d|l|r) ")
            return input_direction
    
    
    def _generate_position(self):
        if self.random_position:
            random_position = (random.randint(0,self.board.grid_size-1), random.randint(0,self.board.grid_size-1))
            while random_position in [(8,8),(7,8),(8,7),(7,7)]:
                random_position = (random.randint(0,self.board.grid_size-1), random.randint(0,self.board.grid_size-1))
            return random_position
        else:
            while True:
                try:
                    row = int(input("What is the row? "))
                    assert 0<=row<=(self.board.grid_size-1)
                except: 
                    "Enter a valid number"
                    continue
                break
            while True:
                try:
                    column = int(input("What is the column? "))
                    assert 0<=column<=(self.board.grid_size-1)
                except: 
                    "Enter a valid number"
                    continue
                break
            return (row,column)
