"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    newlist = []
    for num4 in range(0,len(line)):
        newlist.append(line[num4])
    for num in range(0,len(newlist)-1):        
        if newlist[num] == 0:
            for num2 in range(num+1,len(newlist)):
                if newlist[num2] != 0:
                    newlist[num] = newlist[num2]
                    newlist[num2] = 0 
                    break 
        if newlist[num] != 0:
            count = 0
            for num3 in range(num+1,len(newlist)):
                count = count + newlist[num3]
                if newlist[num] == newlist[num3] and newlist[num] == count:
                    newlist[num] = newlist[num]*2
                    newlist[num3] = 0
                    break
               
    return newlist


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._cells = []
        self._is_occupied = False
        self._is_changed = False
        self.reset() 

    def reset(self):
        """
        reset function
        """
        self._cells = [[0 for dummy_col in range(self.get_grid_width())] for dummy_row in range(self.get_grid_height())]     
        self.new_tile()
        self.new_tile()

    def __str__(self):
        return str(self._cells)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def new_tile(self):
        """
        new title function
        """
        available_tiles = []
        for row in range(self.get_grid_height()):
            for col in range(self.get_grid_width()):
                if self._cells[row][col] == 0:
                    available_tiles.append([row,col])
        values = {0:2,1:2,2:2,3:2,4:2,5:2,6:2,7:2,8:2,9:4}

        random_tile = random.choice(available_tiles)
        self.set_tile(random_tile[0],random_tile[1],(random.choice(values.values())))

    def set_tile(self, row, col, value):  
        """
        set_title function
        """
        self._cells[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._cells[row][col]
    
   
    def move(self, direction):
        """
        The main logic function
        """
        
        self._direction = direction     
        before_move = str(self._cells)

        if self._direction == UP:
            self.move_helper1()
             
        # Down
        elif self._direction == DOWN:
            self.move_helper2()
           
        # Left
        elif self._direction == LEFT:
            self.move_helper3()
    
        # Right                    
        elif self._direction == RIGHT:
            self.move_helper4()
            
        
        after_move = str(self._cells)
        
        if before_move != after_move:
            self.new_tile()
    
    def move_helper1(self):
        """
        UP
        """
        offset = OFFSETS[UP]
        temp_grid = [] 
        for col in range(self.get_grid_width()):
            start = 0
            temp_list = []
            for row in range(self.get_grid_height()):
                temp_list.append(self._cells[start][col])
                start += offset[0]
            temp_list = merge(temp_list)
            temp_grid.append(temp_list)
        for row in range(self.get_grid_height()):
            for col in range(self.get_grid_width()):
                self._cells[row][col] = temp_grid[col][row]

    def move_helper2(self):
        """
        DOWN
        """
        offset = OFFSETS[DOWN]
        temp_grid = [] 
        for col in range(self.get_grid_width()):
            start = self.get_grid_height() -1
            temp_list = []
            for row in range(self.get_grid_height()):
                temp_list.append(self._cells[start][col])
                start += offset[0]
            temp_list = merge(temp_list)
            temp_grid.append(temp_list)
        for row in range(self.get_grid_height()):
            for col in range(self.get_grid_width()):
                self._cells[row][col] = temp_grid[col][self.get_grid_height() -1 -row]
            
    def move_helper3(self):
        """
        LEFT
        """
        offset = OFFSETS[LEFT]
        temp_grid = [] 
        for row in range(self.get_grid_height()):
            start = 0
            temp_list = []
            for col in range(self.get_grid_width()):
                temp_list.append(self._cells[row][start])
                start += offset[1]
            temp_list = merge(temp_list)
            temp_grid.append(temp_list)
        for row in range(self.get_grid_height()):
            for col in range(self.get_grid_width()):
                self._cells[row][col] = temp_grid[row][col]
            
    def move_helper4(self):
        """
        RIGHT
        """
        offset = OFFSETS[RIGHT]
        temp_grid = [] 
        for row in range(self.get_grid_height()):
            start = self.get_grid_width() -1
            temp_list = []
            for col in range(self.get_grid_width()):
                temp_list.append(self._cells[row][start])
                start += offset[1]
            temp_list = merge(temp_list)
            temp_grid.append(temp_list)
        for row in range(self.get_grid_height()):
            for col in range(self.get_grid_width()):
                self._cells[row][col] = temp_grid[row][self.get_grid_width() -1 -col]


poc_2048_gui.run_gui(TwentyFortyEight(8, 4))
