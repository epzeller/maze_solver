import unittest
from maze import maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = maze(0,0,num_rows,num_cols,10,10)
        self.assertEqual(
            len(m1._cells), num_cols
        )
        self.assertEqual(
            len(m1._cells[0]), num_rows
        )

    def test_maze_create_cells_2(self):
        num_cols = 50
        num_rows = 2
        m1 = maze(0,0,num_rows,num_cols,10,10)
        self.assertEqual(
            len(m1._cells), num_cols
        )
        self.assertEqual(
            len(m1._cells[0]), num_rows
        )

    def test_entrance_exit(self):
        num_cols = 10
        num_rows = 10
        m1 = maze(0,0,num_rows,num_cols,10,10)
        m1._break_entrance_and_exit()
        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[num_cols-1][num_rows-1].has_bottom_wall)

if __name__ == "__main__":
    unittest.main() 
