grid_size = 10

# Input robot name and coordinates
name = input("Robot name: ")
while True:
    try:
        row = int(input("Row coordinate: "))
        break
    except:
        print("Enter an integer")
        continue

# "Clipping" the values so the robot is in the grid
if row<0: 
    row = 0
elif row>=grid_size:
    row = grid_size-1

while True:
    try:
        column = int(input("Column coordinate: "))
        break
    except:
        print("Enter an integer")
        continue
if column<0:
    column = 0
elif column>=grid_size:
    column = grid_size-1


direction = None
while direction not in ['n', 's', 'e', 'w']:
    direction = input("Enter a direction ('n', 's', 'e' or 'w')")
if direction == 'n':
    row-=1
    direction_name = "North"
elif direction == 's':
    row +=1
    direction_name = "South"
elif direction == 'e':
    column +=1
    direction_name = "East"
elif direction == 'w':
    column -=1
    direction_name = "West"
#Clip values again
if column<0:
    column = 0
elif column>=grid_size:
    column = grid_size-1
if row<0: 
    row = 0
elif row>=grid_size:
    row = grid_size-1

age = 4
id = 1

message = f'My name is {name} and my id is {id}.'
print(message)
#Find quadrant
if row<grid_size//2:
    row_half = "top"
else:
    row_half = "bottom"

if column<grid_size//2:
    column_half = "left"
else:
    column_half = "right"

quadrant = row_half+" "+column_half
print(f"Current location: ({row},{column}), {quadrant} quadrant. I am facing {direction_name}")





