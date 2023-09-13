grid_size = 10

name = input("Robot name: ")
while True:
    try:
        row = int(input("Row coordinate: "))
        break
    except:
        print("Enter an integer")
        continue
#"Clipping" the values so the robot is in the grid

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

age = 4
id = 1
message = f'My name is {name} and my id is {id}.'
print(message)
if row<grid_size//2:
    row_half = "top"
else:
    row_half = "bottom"

if column<grid_size//2:
    column_half = "left"
else:
    row_half = "right"

quadrant = row_half+" "+column_half
print(f"Current location: ({row},{column}), {quadrant} quadrant")

