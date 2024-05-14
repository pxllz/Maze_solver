from cell import Cell
import random
import time

# MAZE CLASS
# The Maze class should hold all the cells in the maze.
class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        
        

    # CREATE_CELLS(SELF) METHOD
    # Should fill a self.cells list with lists of cells.
    # Each top-level list is a collumn of cell objects.
    # Once the matrix is populated it should call its draw_cells() method on each Cell.

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    # DRAW_CELLS(SELF,I,J) METHOD
    # Should calculate x/y position of the Cell based of i,j.
    # Should calculate the cell_size and the x/y position of the Maze itself.
    # the x/y position of the maze represents the top-left corner of the maze.
    # Should call the draw() method on the cell object to draw it.

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()


    # ANIMATE(SELF) METHOD
    # Visualize what the algorithm is doing.
    # Should call the window's redraw() method.
    # Sleep for a short time to slow down the animation.
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    # _BREAK_ENTRANCE_AND_EXIT METHOD
    # The entrance will always be the top-left cell.
    # The exit will always be the bottom-right cell.
    # add _break_entrance_and_exit() method tha
    # t removes an outer wall from those cells
    # call _draw_cell() after each removal
    def _break_entrance_and_exit(self):

        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)


    # _BREAK_WALL_R(SELF,I,J) METHOD
    # Recursive break_wals_r method is a depth-first traversal through the cell.
    # breaking some walls as it goes.
    # It should call itself on the neighboring cell if it hasn't been visited.
    # It should call _draw_cell() after each wall removal.
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])


    # _RESET_CELLS_VISITED(SELF) METHOD
    # Should reset the visited property of all the cells in the maze to False.
    # Call it after _break_walls_r() 
    # so we can reuse the visited property when solving the maze in the next step.
    
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False


    
    # _SOLVE_R(SELF,I,J) METHOD
    # Return True if the current cell is an end cell Or if it leads to an end cell.
    # Return False if the current cell is a dead end.
    # 1. Call the _animate() method.
    # 2. Mark the current cell as visited.
    # 3. If the current cell is the exit cell, return True.
    # 4. For each direction :
    #    - If there is a cell in that direction , no walls blocking, cell is not visited
    #           - Draw a move from the current cell to the next cell.
    #           - Call _solve_r() recursivly on the next cell. if it returns True, return True.
    #           - draw an "undo" move from the current cell to the next cell.
    # 5. If none of the directions worked, return False.

    def _solve_r(self, i, j):
        self._animate()

        # vist the current cell
        self._cells[i][j].visited = True

        # if we are at the end cell, we are done!
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        # move left if there is no wall and it hasn't been visited
        if (
            i > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i - 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        # move right if there is no wall and it hasn't been visited
        if (
            i < self._num_cols - 1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i + 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        # move up if there is no wall and it hasn't been visited
        if (
            j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j - 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        # move down if there is no wall and it hasn't been visited
        if (
            j < self._num_rows - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j + 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        # we went the wrong way let the previous cell know by returning False
        return False
    


    # SOLVE_MAZE(SELF) METHOD
    # Should simple calls the _solve_r method on the top-left cell.
    # Should return True if the exit was found, False otherwise.
    # This is the same return value as the _solve_r method.

    def solve(self):
        return self._solve_r(0, 0)