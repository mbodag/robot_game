class Board:
    def __init__(self, grid_size,) -> None:
        self.grid_size = grid_size
        self.robots = []
        self.targets = [] #((row,col), robot)
        self.current_move_count = 0
        self.current_target = None
        self.disallowed_moves = [((0,1),(0,2)),((0,11),(0,12)),((1,3),(1,4)),((1,12),(1,13)),((2,1),(2,2)),((2,9),(2,10)),((3,6),(3,7)),((5,13),(5,14)),((6,2),(6,3)),((6,11),(6,12)),((7,6),(7,7)),((7,8),(7,9)),((8,6),(8,7)),((8,8),(8,9)),((10,4),(10,5)),((10,7),(10,8)),((10,12),(10,13)),((11,0),(11,1)),((11,10),(11,11)),((12,6),(12,7)),((12,13),(12,14)),((14,3),(14,4)),((14,9),(14,10)),((15,5),(15,6)),((15,11),(15,12)),((0,4),(1,4)),((0,13),(1,13)),((1,1),(2,1)),((2,9),(3,9)),((3,6),(4,6)),((3,15),(4,15)),((5,0),(6,0)),((5,11),(6,11)),((5,14),(6,14)),((6,3),(7,3)),((6,7),(7,7)),((6,8),(7,8)),((8,7),(9,7)),((8,8),(9,8)),((8,15),(9,15)),((9,8),(10,8)),((9,13),(10,13)),((10,1),(11,1)),((11,10),(12,10)),((12,14),(13,14)),((13,0),(14,0)),((13,9),(14,9)),((14,3),(15,3))]
        reversed_disallowed = [(end, start) for (start,end) in self.disallowed_moves]
        self.disallowed_moves += reversed_disallowed
        
    def has_space(self):
        for row in range(self.grid_size):
            for column in range(self.grid_size):
                if not self.square_has_robot(row, column):
                    return True
        return False


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
        else:
            print("Illegal move")
    
    def visualise(self):
        pass

    def robot_is_at_target(self):
        return self.current_target[1].position == self.current_target[0]

                    
