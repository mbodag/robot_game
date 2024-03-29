WIDTH, HEIGHT = 800, 800
FPS = 60

SQUARE_SIZE = 45
GRID_SIZE = 16

#Colors for the display
WHITE = (240,240,240)
BROWN = (150,75,0)
RED = (255,0,0)
GREEN = (0,150,0)
BLUE = (0,0,255)
YELLOW = (196,180,84)
LIGHT_GREY = (211,211,211)

#Potential target squares. The targets can also be randomly generated into any square
TARGETS = {((6,3),1),((11,10),3), ((5,14),2), ((2,1),0),((11,1),2),((14,3),0), ((1,4),1),((1,13),3)}

#This is where the walls are
disallowed_moves = [((0,1),(0,2)),((0,11),(0,12)),((1,3),(1,4)),((1,12),(1,13)),((2,1),(2,2)),((2,9),(2,10)),((3,6),(3,7)),((5,13),(5,14)),((6,2),(6,3)),((6,11),(6,12)),((7,6),(7,7)),((7,8),(7,9)),((8,6),(8,7)),((8,8),(8,9)),((10,4),(10,5)),((10,7),(10,8)),((10,12),(10,13)),((11,0),(11,1)),((11,10),(11,11)),((12,6),(12,7)),((12,13),(12,14)),((14,3),(14,4)),((14,9),(14,10)),((15,5),(15,6)),((15,11),(15,12)),((0,4),(1,4)),((0,13),(1,13)),((1,1),(2,1)),((2,9),(3,9)),((3,6),(4,6)),((3,15),(4,15)),((5,0),(6,0)),((5,11),(6,11)),((5,14),(6,14)),((6,3),(7,3)),((6,7),(7,7)),((6,8),(7,8)),((8,7),(9,7)),((8,8),(9,8)),((8,15),(9,15)),((9,8),(10,8)),((9,13),(10,13)),((10,1),(11,1)),((11,10),(12,10)),((12,14),(13,14)),((13,0),(14,0)),((13,9),(14,9)),((14,3),(15,3)),((10,5),(11,5)),((11,6),(12,6))]