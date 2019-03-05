#!/usr/bin/env python3

import unittest
from life import live, live_neighbors


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

    def test_that_cell_with_dead_downstairs_dies(self):
        self.assertNextGen([
            '*',
            '.'
        ], [
            '.',
            '.'
        ])

    def test_that_middle_cell_survives_from_three_live(self):
        self.assertNextGen(['***'], ['.*.'])

    def test_that_two_neighbour_cell_doesnt_come_to_life(self):
        self.assertNextGen(['*.*'], ['...'])

    def test_that_cell_without_neighbors_has_no_live_neighbors(self):
        self.assertEqual(
            live_neighbors(['.'], 0, 0),
            0)

    def test_that_cell_with_live_neighbor_has_live_neighbor(self):
        self.assertEqual(
            live_neighbors(['.*'], 0, 0),
            1)

    @unittest.skip('later')
    def test_that_middle_cell_of_three_living_floors_lives(self):
        self.assertNextGen(
            [
                '*',
                '*',
                '*'
            ],
            [
                '.',
                '*',
                '.'
            ]

        )

    @unittest.skip('Implement after the less-mature step above')
    def test_that_corner_cell_with_two_live_neighbors_lives(self):
        self.assertNextGen([
            '**',
            '*.'
        ], [
            '**',
            '**'
        ])


if __name__ == '__main__':
    unittest.main()
