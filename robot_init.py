from robot import Robot
import random

class RobotFactory:
    
    factory_instances = 0

    def __init__(self, grid_size = 10, 
                names = ["Wall-E", "R2D2", "C3PO", "Gaios"], 
                random_direction = True, random_position = True) -> None:

        self.robot_instances = 0
        self.grid_size = grid_size
        self.names = names
        self.random_direction = random_direction
        self.random_position = random_position
        self.factory_id = self.factory_instances * 10000
        RobotFactory.factory_instances += 1

        

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
        if self.robot_instances < 10000:
            name = self._generate_name()
            id = self.robot_instances + self.factory_id
            direction = self._generate_direction()
            position = self._generate_position()
            self.robot_instances += 1
            return Robot(name, id, position, direction, self.grid_size)
        else: 
            print("Maximum robot limit of the factory reached")
            return None

    def _generate_name(self):
        try:
            robot_name = self.names[self.robot_instances]
        except:
            robot_name = input("What is the robot's name? ")
        return robot_name

    
    def _generate_direction(self):
        if self.random_direction:
            return random.choice(['w','e','n','s'])
        else:
            input_direction = None
            while input_direction not in ['w','e','n','s']:
                    input_direction = input("What is the direction? (n|e|s|w) ")
            return input_direction
    
    
    def _generate_position(self):
        if self.random_position:
            return (random.randint(0,self.grid_size-1), random.randint(0,self.grid_size-1))
        else:
            while True:
                try:
                    row = int(input("What is the row? "))
                    assert 0<=row<=(self.grid_size-1)
                except: 
                    "Enter a valid number"
                    continue
                break
            while True:
                try:
                    column = int(input("What is the column? "))
                    assert 0<=column<=(self.grid_size-1)
                except: 
                    "Enter a valid number"
                    continue
                break