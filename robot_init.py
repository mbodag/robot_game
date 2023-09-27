from robot import Robot
import random
from board import Board
from constants import *

class RobotFactory:
    
    factory_instances = 0

    def __init__(self, grid_size = 16, 
                names = ["Red", "Green", "Blue", "Yellow"], 
                random_direction = True, random_position = True, unique_positions = True, colors = (RED, GREEN, BLUE, YELLOW)) -> None:
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
        self.colors = colors
        if len(names) > 0:
            self.create_robots(len(names))

        

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
            color = self.colors[self.robot_instances]
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
            new_robot = Robot(name, id, position, direction, self.board, color)
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

if __name__ == '__main__':
    ricochet_factory = RobotFactory(16, ['Red', 'Green', 'Blue', 'Yellow'],colors = [(255,0,0),(0,255,0),(0,0,255),(0,255,255)])
    robots = ricochet_factory.create_robots(4)
    ricochet_factory.board.current_target = ((0,0),ricochet_factory.board.robots[0])
    for rob in ricochet_factory.board.robots:
        print(rob, rob.position, rob.direction)
        print(ricochet_factory.board.is_legal_move(rob,rob.direction))



    while not ricochet_factory.board.robot_is_at_target():
        nm = input("Choose robot: ")
        if nm.lower().strip() == 'quit':
            break
        for robot in ricochet_factory.board.robots:
            if robot.name.lower() == nm.lower().strip():
                current_rob = robot
        dir = input("Choose direction: ")
        if dir.lower().strip() == 'quit':
            break
        current_rob.direction = dir
        current_pos = current_rob.position
        ricochet_factory.board.make_a_robot_move(current_rob)
        print(f"Moving {nm} from {current_pos} to {current_rob.position}. Direction {dir}")
        print(f"Number of moves: {ricochet_factory.board.current_move_count}")

        if ricochet_factory.board.robot_is_at_target():
            print('You have reached the target!')
    