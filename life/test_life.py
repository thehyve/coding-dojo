#!/usr/bin/env python3

import unittest
from life import live


class LifeTestCase(unittest.TestCase):

    def assertNextGen(self, gen1, gen2):
        new_gen = live(gen1)
        self.assertEqual(new_gen, gen2)

    def test_that_cell_without_neighbours_remains_dead(self):
        self.assertNextGen(['.'], ['.'])

    def test_that_living_cell_without_neighbours_dies(self):
        self.assertNextGen(['*'], ['.'])

    def test_that_two_dead_cells_remain_dead(self):
        self.assertNextGen(['..'], ['..'])

    def test_that_two_live_cells_die(self):
        self.assertNextGen(['**'], ['..'])

    def test_that_live_cell_next_to_dead_cell_dies(self):
        self.assertNextGen(['*.'], ['..'])

    def test_that_cell_with_dead_floor_cell_dies(self):
        self.assertNextGen([
            '*',
            '.'], [
            '.',
            '.'])

if __name__ == '__main__':
    unittest.main()
