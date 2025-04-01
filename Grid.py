# -*- coding: utf-8 -*-
import random

class Grid:
    def __init__(self, grid_init):
        '''Initializes the grid with its lines and column count, and its content.'''
        self.__grid = grid_init
        self.__lines_count = len(grid_init)
        self.__columns_count = len(grid_init[0]) if len(grid_init) else 0

    def get_grid(self):
        '''Returns the content of the grid.'''
        return self.__grid

    def get_lines_count(self):
        '''Returns the number of lines in the grid.'''
        return self.__lines_count

    def get_columns_count(self):
        '''Returns the number of columns in the grid.'''
        return self.__columns_count

    def fill_random(self, values):
        '''Fills the grid randomly with the given values.'''
        self.__grid = [[random.choice(values)
                        for _ in range(self.__columns_count)]
                       for _ in range(self.__lines_count)]

    def get_line(self, line_number):
        '''Returns the specified line.'''
        return self.__grid[line_number]

    def get_column(self, column_number):
        '''Returns the specified column.'''
        return [line[column_number] for line in self.__grid]

    def get_diagonal(self):
        '''Returns the main diagonal, from top left to bottom right.'''
        diagonal_size = min(self.__lines_count, self.__columns_count)
        return [self.__grid[line_number][line_number] for line_number in range(diagonal_size)]

    def get_anti_diagonal(self):
        '''Returns the anti-diagonal, from top right to bottom left.'''
        diagonal_size = min(self.__lines_count, self.__columns_count)
        return [self.__grid[line_number][self.__columns_count - line_number - 1]
                for line_number in range(diagonal_size)]

    def get_line_str(self, line_number, separator='\t'):
        '''Returns a textual representation of the specified line of the grid.'''
        return separator.join(str(value) for value in self.__grid[line_number])

    def get_grid_str(self, separator='\t'):
        '''Returns a textual representation of the entire grid.'''
        return '\n'.join(self.get_line_str(line_number, separator) for line_number in range(self.__lines_count))

    def has_equal_values(self, value):
        '''Returns True if the entire grid contains the same value, False otherwise.'''
        return all([all([value == grid_value for grid_value in line]) for line in self.__grid])

    def is_square(self):
        '''Returns True if the grid is square, False otherwise.'''
        return self.__lines_count == self.__columns_count

    def get_count(self, value):
        '''Returns the number of occurrences of the specified value in the grid.'''
        return sum(line.count(value) for line in self.__grid)

    def get_sum(self):
        '''Returns the sum of all values in the grid.'''
        return sum(sum(line) for line in self.__grid)

    def get_coordinates_from_cell_number(self, cell_number):
        '''Returns the coordinates (x, y) of the specified cell number.'''
        return cell_number // self.__columns_count, cell_number % self.__columns_count

    def get_cell_number_from_coordinates(self, line_number, column_number):
        '''Returns the cell number of the specified coordinates (x, y).'''
        return line_number * self.__columns_count + column_number

    def get_cell(self, cell_number):
        '''Returns the value of the specified cell.'''
        line_number, column_number = self.get_coordinates_from_cell_number(cell_number)
        return self.__grid[line_number][column_number]

    def set_cell(self, cell_number, value):
        '''Sets the value of the specified cell.'''
        line_number, column_number = self.get_coordinates_from_cell_number(cell_number)
        self.__grid[line_number][column_number] = value

    def get_same_value_cell_numbers(self, value):
        '''Returns all cells with the same value as the specified one.'''
        return [cell_number
                for cell_number in range(self.__lines_count * self.__columns_count)
                if self.get_cell(cell_number) == value]

    def get_neighbour(self, line_number, column_number, delta, is_tore=True):
        '''Returns the neighbor of a cell based on the specified delta.'''
        new_line_number, new_column_number = line_number + delta[0], column_number + delta[1]
        if is_tore or 0 <= new_line_number < self.__lines_count and 0 <= new_column_number < self.__columns_count:
            return self.__grid[new_line_number % self.__lines_count][new_column_number % self.__columns_count]
        return None

    def get_neighborhood(self, line_number, column_number, deltas, is_tore=True):
        '''Returns the neighborhood of a cell based on the specified deltas.'''
        return [self.get_neighbour(line_number, column_number, delta, is_tore)
                for delta in deltas]

    def get_cell_neighbour_number(self, cell_number, delta, is_tore=True):
        '''Returns the cell number of a neighbor based on the specified delta.'''
        line_number, column_number = self.get_coordinates_from_cell_number(cell_number)
        line_number, column_number = line_number + delta[0], column_number + delta[1]
        if is_tore or 0 <= line_number < self.__lines_count and 0 <= column_number < self.__columns_count:
            line_number %= self.__lines_count
            column_number %= self.__columns_count
            return self.get_cell_number_from_coordinates(line_number, column_number)
        return None

    def get_cell_neighborhood_numbers(self, cell_number, deltas, is_tore=True):
        '''Returns the cell numbers of all neighbors based on the specified deltas.'''
        res = []
        for delta in deltas:
            neighbour = self.get_cell_neighbour_number(cell_number, delta, is_tore)
            if neighbour is not None:
                res.append(neighbour)
        return sorted(res)

