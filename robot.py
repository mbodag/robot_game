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

    def __repr__(self):
        return f"Hi, my name is {self.name}. My ID is {self.id}"

if __name__ == "__main__":
    jj = Robot('jj')
    print(str(jj))
        

        