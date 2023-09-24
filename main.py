import random
from robot import Robot
from robot_init import RobotFactory








# Randomise robot name and coordinatesppy
ricochet_factory = RobotFactory(16, ['Red', 'Green','Blue', 'Yellow'])
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
    

    




















