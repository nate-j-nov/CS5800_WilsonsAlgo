# Wilsons

from random import choice
from cell import * 
from grid import *

class wilsons: 
    

    def __init__(self, x, y, z): 
        self.block = grid(x, y, z)
        self.DIRECTIONS = {
        'N': (0, -1, 0), 
        'S':(0, 1, 0), 
        'E':(-1, 0, 0),
        'W': (1, 0, 0), 
        'U': (0, 0, 1), 
        'D':(0, 0, -1)
        }

    def algo(self): 
        # generate stack of unvisited cells
        unvisited = self.block.getAllCells()

        # select origin and remove from unvisited
        origin = choice(unvisited)
        unvisited.remove(origin)

        #Now, iterate through unvisited nodes until they are all visited
        while len(unvisited) > 0: 
            current = choice(unvisited)
            currentPath = [current]

            # This is the random walk to find a path
            while current in unvisited: 
                # BS to determine if a neighbor exists here
                canUseNeighbor = False
                direction = ''
                while not canUseNeighbor: 
                    direction = choice(list(self.DIRECTIONS.keys()))
                    print(direction)
                    if current.hasNeighbor(direction): 
                        movements = self.DIRECTIONS.get(direction)
                        canUseNeighbor = True
                        nextX = current.x + movements[0]
                        nextY = current.y + movements[1]
                        nextZ = current.z + movements[2]
                        nextCell = self.block.getCell(nextX, nextY, nextZ)
                        print("next determined")

                        
                # Determine if the current cell is within the current path
                if nextCell in currentPath: 
                    # Find beginning and end of deleted portion
                    deletedPathStart = currentPath.index(nextCell)
                    deletedPathEnd = len(current)
                    # close all open doors (each cell should only have one outgoing open door)
                    for cell in range(deletedPathStart, deletedPathEnd): 
                        currentPath[cell].closeOpenDoors()
                    currentPath = currentPath[0:deletedPathStart + 1]
                else: 
                    currentPath.append(nextCell)
                    current.openDoor(direction)
                    unvisited.remove(current)
                current = nextCell
        

if __name__ == '__main__':
    w = wilsons(2, 2, 2)
    w.algo()




