import random

class Robot:
    instances = 0
    grid_size = 10

    def __init__(self, name) -> None:
        self.instances += 1
        self.id = self.instances
        self.name = name
        self.position = (random.randint(0, self.grid_size-1) , random.randint(0,self.grid_size-1))
        self.direction = random.choice(['n', 'e', 's', 'w'])
        self.target = (9,9)

    def __repr__(self):
        return f"Hi, my name is {self.name}. My ID is {self.id}"
    
    def turn_right(self):
        directions = ['n', 'e', 's', 'w']
        idx = directions.index(self.direction)
        self.direction = directions[(idx+1)%4]
    
    def move_a_square(self):
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
        while not self.is_facing_wall():
            self.move_a_square()


    def is_facing_wall(self):
        facing_north_wall = self.position[0] == 0 and self.direction == 'n'
        facing_south_wall = self.position[0] == self.grid_size-1 and self.direction == 's'
        facing_east_wall = self.position[1] == 0 and self.direction == 'w'
        facing_west_wall = self.position[1] == self.grid_size - 1 and self.direction == 'e'
        
        return facing_north_wall or facing_south_wall or facing_west_wall or facing_east_wall

    def is_at_target(self):
        return self.position == self.target


    def navigate(self):
        counter = 0
        while not self.is_at_target():
            self.move_forward_to_wall()
            print(self.position, self.direction)
            self.turn_right()
            counter +=1

if __name__ == "__main__":
    jj = Robot('jj')
    jj.navigate()
    print(jj.position)
        

        