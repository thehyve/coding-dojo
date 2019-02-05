#!/usr/bin/env python3

import unittest
from life import live


class LifeTestCase(unittest.TestCase):

    def test_that_cell_without_neighbours_remains_dead(self):
        grid = ['.']
        new_gen = live(grid)
        self.assertEqual(new_gen, ['.'])

    def test_that_living_cell_without_neighbours_dies(self):
        grid = ['*']
        new_gen = live(grid)
        self.assertEqual(new_gen, ['.'])

    def test_that_two_dead_cells_remain_dead(self):
        grid = ['..']
        new_gen = live(grid)
        self.assertEqual(new_gen, ['..'])

    def test_that_two_live_cells_die(self):
        grid = ['**']
        new_gen = live(grid)
        self.assertEqual(new_gen, ['..'])

    def test_that_live_cell_next_to_dead_cell_dies(self):
        grid = ['*.']
        new_gen = live(grid)
        self.assertEqual(new_gen, ['..'])


if __name__ == '__main__':
    unittest.main()
