# init 
    # assign indexes, max indexes etc...
    # default pos (1,1)
# current pos
    # return tuple of pos as string
# move down
# move up
# move left
# move right
# __str__
    # return grid of x as pos and o as grid


class Grid(object):
    """
    A class that creates a grid of size (rows,cols) with 
    starting position at (x,y) = (1,1).
    
    Attributes
    ----------
    rows: int
        height of grid, default as 1.
    cols: int
        width of grid, default as 1.
    
    Methods
    -------
    make_grid():
        Creates a grid of size(rows,cols) of o's with 
        current position as the letter x and returns it as a string.
    current_pos():
        Returns the current position (x,y) as a tuple.
    move_left():
        Moves the current position to the left.
    move_right():
        Moves the current position to the right.
    move_up():
        Moves the current position up.
    move_down():
        Moves the current position down.
    """
    def __init__(self,rows = 1,cols = 1):
        """
        Constructs all required attributes for the grid object.

        Parameters
        ----------
            rows: int
                height of grid, default as 1.
            cols: int
                width of grid, default as 1.
        
        Returns
        -------
            None
        """
        self.MIN_INDEX = 0
        self.MAX_ROW_INDEX = rows - 1
        self.MAX_COL_INDEX = cols - 1
        self.rows = rows
        self.cols = cols
        self.pos_row_index = 0
        self.pos_col_index = 0

    def make_grid(self):
        """
        Creates a grid of size(rows,cols) of o's with 
        current position as the letter x and returns it as a string.

        Parameters
        ----------
            None

        Returns
        -------
        Grid of o's and current position as the letter x as a string
        """
        grid_str = ""
        grid = [list(self.cols * "o") for k in range(self.rows)] 
        grid[self.pos_row_index][self.pos_col_index] = "x"

        for floor in grid: 
            grid_str += "".join(floor)+"\n"
        return grid_str

    def current_pos(self):
        """
        Current position (x,y) as a tuple.

        Parameters
        ----------
            None
        
        Returns
        -------
            (x,y) position as a tuple
        
        """
        row_pos = self.pos_row_index + 1
        col_pos = self.pos_col_index + 1
        return row_pos,col_pos

    def move_left(self):
        """
        Changes the value of the current position to the coordinates
        left to it. If coordinate is min, it becomes max.

        Parameters
        ----------
            None

        Returns
        -------
            None
        
        """
        if self.pos_col_index == self.MIN_INDEX:
            self.pos_col_index = self.MAX_COL_INDEX
        else:
            self.pos_col_index -= 1

    def move_right(self):
        """
        Changes the value of the current position to the coordinates
        right to it. If coordinate is max, it becomes min.

        Parameters
        ----------
            None

        Returns
        -------
            None
        """
        if self.pos_col_index == self.MAX_COL_INDEX:
            self.pos_col_index = self.MIN_INDEX
        else:
            self.pos_col_index += 1

    def move_up(self):
        """
        Changes the value of the current position to the coordinates
        above. If coordinate is min, it becomes max.

        Parameters
        ----------
            None

        Returns
        -------
            None
        """
        if self.pos_row_index == self.MIN_INDEX:
            self.pos_row_index = self.MAX_ROW_INDEX
        else:
            self.pos_row_index -= 1

    def move_down(self):
        """
        Changes the value of the current position to the coordinates
        below. If coordinate is max, it becomes min.

        Parameters
        ----------
            None

        Returns
        -------
            None
        """
        if self.pos_row_index == self.MAX_ROW_INDEX:
            self.pos_row_index = self.MIN_INDEX
        else:
            self.pos_row_index += 1

    def __str__(self):
        return self.make_grid()
