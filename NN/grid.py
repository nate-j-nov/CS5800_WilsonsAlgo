# Grid
from cell import cell

class grid:
    def __init__(self, rows, columns, height): 
        self.rows = rows
        self.cols = columns
        self.aisles = height
        self.block = self.generateBlock()
    
    def generateBlock(self): 
        block = []
        for row in range(self.rows): 
            for col in range(self.cols): 
                for aisle in range(self.aisles): 
                    temp = cell(row, col, aisle, self)
                    block.append(temp)
        return block
            
    def printBlock(self): 
        for cell in self.block: 
            print(cell)

    def getCell(self, x, y, z): 
        for cell in self.block: 
            if cell.x == x and cell.y == y and cell.z == z: 
                return cell

    def getAllCells(self): 
        return self.block[:]


if __name__ == '__main__':
    x = grid(3, 3, 3)
    x.printBlock()
    

