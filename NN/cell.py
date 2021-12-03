# Cell Class

class cell:
    def __init__(self, x, y, z, grid): 
        self.x = x
        self.y = y
        self.z = z
        self.openDoors = []
        self.NorthDoor = False
        self.SouthDoor = False
        self.EastDoor = False
        self.WestDoor = False
        self.UpDoor = False
        self.DownDoor = False
        self.grid = grid

    def openDoor(self, direction): 
        match direction: 
            case 'N': 
                self.NorthDoor = True
                self.openDoors.append(self.NorthDoor)
            case 'S': 
                self.SouthDoor = True
                self.openDoors.append(self.SouthDoor)
            case 'E': 
                self.EastDoor = True
                self.openDoors.append(self.EastDoor)
            case 'W': 
                self.WestDoor = True
                self.openDoors.append(self.WestDoor)
            case 'U': 
                self.UpDoor = True
                self.openDoors.append(self.UpDoor)
            case 'D': 
                self.DownDoor = True
                self.openDoors.append(self.DownDoor)
            case _: pass
    
    def __str__(self): 
        return "(X: " + str(self.x) + " Y: " + str(self.y) + " Z: " + str(self.z) + ")"

    def __repr__(self): 
        return self.__str__()

    def hasNeighbor(self, direction): 
        match direction: 
            case 'N': 
                if self.x - 1 < 0: return False
                else: return True
            case 'S': 
                if self.x + 1 > self.grid.rows: return False
                else: return True
            case 'E': 
                if self.y - 1 < 0: return False
                else: return True
            case 'W': 
                if self.y + 1 > self.grid.cols: return False
                else: return True
            case 'U': 
                if self.z + 1 > self.grid.aisles: return False
                else: return True
            case 'D': 
                if self.z - 1 < 0: return False
                else: return True
            case _: print("Issue in hasneighbor")

    def closeOpenDoors(self): 
        for door in self.openDoors: 
            door = False


if __name__ == '__main__':
    x = cell(1, 1, 1)
    print(x)