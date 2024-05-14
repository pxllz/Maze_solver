# Import the unittest module
import unittest 

# Import the Maze class from the maze module
from maze import Maze





# MAZE TEST
# We need to test the Maze class's methods.
# We need to run the logic without the graphics.
# We want to test the logic not the visuals.

# Make the Window parameter to the Cell and Maze class optional and hae it default to None.
# This will allow us to test the logic without the graphics.

import unittest

from maze import Maze


class Tests(unittest.TestCase):                             # Create a class that inherits from unittest.TestCase
    def test_maze_create_cells(self):                       # Create a test method
        num_cols = 12                                       # Set the number of columns
        num_rows = 10                                       # Set the number of rows
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)         # Create a Maze object
        self.assertEqual(len(m1._cells),num_cols,)          # Assert that the number of columns is correct
        self.assertEqual(len(m1._cells[0]),num_rows,)       # Assert that the number of rows is correct


    def test_maze_create_cells_large(self):                 # Create a test method
        num_cols = 16                                       # Set the number of columns                
        num_rows = 12                                       # Set the number of rows
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)         # Create a Maze object
        self.assertEqual(len(m1._cells),num_cols,)          # Assert that the number of columns is correct
        self.assertEqual(len(m1._cells[0]),num_rows,)       # Assert that the number of rows is correct

    def test_maze_create_cells_small(self):                 # Create a test method
        num_cols = 4                                        # Set the number of columns
        num_rows = 4                                        # Set the number of rows
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)         # Create a Maze object
        self.assertEqual(len(m1._cells),num_cols,)          # Assert that the number of columns is correct
        self.assertEqual(len(m1._cells[0]),num_rows,)       # Assert that the number of rows is correct

    def test_maze_create_cells_single(self):                # Create a test method
        num_cols = 1                                        # Set the number of columns
        num_rows = 1                                        # Set the number of rows
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)         # Create a Maze object
        self.assertEqual(len(m1._cells),num_cols,)          # Assert that the number of columns is correct
        self.assertEqual(len(m1._cells[0]),num_rows,)       # Assert that the number of rows is correct


    # add a test method for the _Break_entrance_and_exit() method
    def test_break_entrance_and_exit(self):                     # Create a test method
        num_cols = 12                                           # Set the number of columns
        num_rows = 10                                           # Set the number of rows
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)             # Create a Maze object
        m1._break_entrance_and_exit()                           # Call the _break_entrance_and_exit() method
        self.assertFalse(m1._cells[0][0].has_top_wall,False)          # Assert that the top wall of the top-left cell is False
        self.assertFalse(
            m1._cells[num_cols-1][num_rows-1].has_bottom_wall,False)  # Assert that the bottom wall of the bottom-right cell is False



    # add a test for the maze_reset_cells_visited() method
    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )
if __name__ == "__main__":
    unittest.main()