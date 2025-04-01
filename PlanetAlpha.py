# -*- coding: utf-8 -*-
from Grid import Grid
import random

class PlanetAlpha(Grid):
    NORTH, EAST, SOUTH, WEST = (-1, 0), (0, 1), (1, 0), (0, -1)
    NORTH_EAST, SOUTH_EAST, SOUTH_WEST, NORTH_WEST = (-1, 1), (1, 1), (1, -1), (-1, -1)
    CARDINAL_POINTS = (NORTH, EAST, SOUTH, WEST)
    WIND_ROSE = (NORTH, NORTH_EAST, EAST, SOUTH_EAST, SOUTH, SOUTH_WEST, WEST, NORTH_WEST)

    def __init__(self, name, latitude_cells_count, longitude_cells_count, ground):
        '''Initializes the Planet with its name, latitude, longitude, and ground as a Grid.'''
        grid_init = [[ground for _ in range(longitude_cells_count)] for _ in range(latitude_cells_count)]
        Grid.__init__(self, grid_init)
        
        self.__name = name
        self.__ground = ground

    def get_name(self):
        '''Returns the name of the planet.'''
        return self.__name
    
    def get_ground(self):
        '''Returns what is used as the ground on the planet.'''
        return self.__ground
    
    def get_random_free_place(self):
        '''Returns an unused cell on the planet.'''
        if self.get_same_value_cell_numbers(self.get_ground()) != []:
            return random.choice(self.get_same_value_cell_numbers(self.get_ground()))
        return -1
    
    def born(self, cell_number, element):
        '''Sets a cell as the desired element.'''
        if self.get_cell(cell_number) == self.get_ground():
            self.set_cell(cell_number, element)
            return 1
        else:
            return 0

    def die(self, cell_number):
        '''Removes everything from a cell.'''
        if self.get_cell(cell_number) != self.get_ground():
            self.set_cell(cell_number, self.get_ground())
            return 1
        else:
            return 0
    
    def __repr__(self):
        '''Returns the alphanumerical representation of the planet.'''
        habitants = sum(1 for row in self.get_grid() for cell in row if cell != self.get_ground())
        print('\n******** Planet with ' + str(self.get_lines_count() * self.get_columns_count()) + ' places (' + str(self.get_ground()) + ') available ********')
        affiche = f"{self.get_name()} ({habitants} inhabitants)\n"
        for line in range(self.get_lines_count()):
            for column in range(self.get_columns_count()):
                if self.get_grid()[line][column] == self.get_ground():
                    affiche += str(self.get_ground())
                else:
                    affiche += str(self.get_grid()[line][column])
            affiche += '\n'
        return affiche

