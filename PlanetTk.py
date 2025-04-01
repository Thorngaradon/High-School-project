# -*- coding: utf-8 -*-
import tkinter as tk
from PlanetAlpha import PlanetAlpha
from Element import *

class PlanetTk(PlanetAlpha, tk.Canvas):
    __COLORS = {'cell_background': 'white', 'cell_foreground': 'red', 'grid_lines': 'black', 'grid_text': 'dark blue', 'widget_text': 'orange'}
    __FONTS = {'basic': ('arial', '16', 'bold')}
    __AUTHORIZED_TYPES = {Cow, Ground}
    
    def __init__(self, root, latitude_cells_count, longitude_cells_count, authorized_classes, background_color='white', foreground_color='dark blue', gridlines_color='maroon', cell_size=40, gutter_size=0, margin_size=0, show_content=True, show_gridlines=True, **kw):
        '''Initialization of PlanetTk, derived from PlanetAlpha and TkInter Canvas.'''
        PlanetAlpha.__init__(self, 'Earth', latitude_cells_count, longitude_cells_count, Ground())
        kw['width'] = cell_size * longitude_cells_count + 2 * margin_size + (longitude_cells_count - 1) * gutter_size
        kw['height'] = cell_size * latitude_cells_count + 2 * margin_size + (latitude_cells_count - 1) * gutter_size
        tk.Canvas.__init__(self, root, **kw)
        
        self.__cell_size = cell_size
        self.__gutter_size = gutter_size
        self.__margin_size = margin_size
        self.__root = root
        self.__show_content = show_content
        self.__show_gridlines = show_gridlines
        self.__authorized_classes = authorized_classes
        self.__background_color = background_color
        self.__foreground_color = foreground_color
        self.__gridlines_color = gridlines_color
        
    def get_root(self):
        '''Returns the root of the PlanetTk.'''
        return self.__root

    def get_background_color(self):
        '''Returns the background color of the cell, mostly used in Turmites.'''
        return self.__background_color

    def get_foreground_color(self):
        '''Returns the foreground color of the cell, mostly used in Turmites.'''
        return self.__foreground_color
    
    '''Void functions'''

    def born(self, cell_number, element):
        '''Sets a cell as the desired element.'''
        self.set_cell(cell_number, element)
        self.lift('t_' + str(cell_number))
    
    def die(self, cell_number):
        '''Removes all elements from a cell.'''
        if self.get_cell(cell_number) != self.get_ground():
            self.set_cell(cell_number, self.get_ground())
    
    def born_randomly(self, element):
        '''Same as born(), but the cell is chosen randomly.'''
        cell = self.get_random_free_place()
        if cell != -1:
            self.set_cell(cell, element)
            self.lift('t_' + str(cell))

    def populate(self, class_names_count):
        '''Same as born(), but used to set multiple cells at the same time.'''
        for elm in class_names_count:
            if elm in self.__AUTHORIZED_TYPES:
                for _ in range(class_names_count[elm]):
                    self.born_randomly(elm())

    def move_element(self, cell_number, new_cell_number):
        '''Moves an element from one cell to another.'''
        self.born(new_cell_number, self.get_cell(cell_number))
        self.die(cell_number)
        
    '''End Void functions'''

    def get_classes_cell_numbers(self):
        '''Returns the list of cells for each class.'''
        classes_cell_numbers = {}
        for type in self.__authorized_classes:
            cells = []
            for cell_number in range(self.get_columns_count() * self.get_lines_count() - 1):
                if not isinstance(self.get_cell(cell_number), Ground) and isinstance(self.get_cell(cell_number), type):
                    cells.append(cell_number)
            classes_cell_numbers[type.__name__] = cells
        del classes_cell_numbers['Ground']
        return classes_cell_numbers
    
    def __repr__(self):
        '''Returns the alphanumerical representation of the planet.'''
        habitants = sum(1 for row in self.get_grid() for cell in row if cell != self.get_ground())
        print('Earth\n' + f'{habitants}' + '/' + f'{self.get_lines_count() * self.get_columns_count()}' + ' inhabitants')
        
        for cell_number in range(self.get_lines_count() * self.get_columns_count()):
            i, j = self.get_coordinates_from_cell_number(cell_number)
            x = j * (self.__cell_size + self.__gutter_size) + self.__margin_size
            y = i * (self.__cell_size + self.__gutter_size) + self.__margin_size
            z = self.get_cell_number_from_coordinates(i, j)
            self.create_rectangle(x, y, x + self.__cell_size, y + self.__cell_size, tags=(f'c_{cell_number}'))
            self.create_text(x + self.__cell_size // 2, y + self.__cell_size // 2, text=f'{self.get_cell(z)}', font=PlanetTk.__FONTS['basic'], tags=(f't_{cell_number}'))
            self.lift('t_' + str(cell_number))
        return 'OK'
    
    def __str__(self):
        '''Same as __repr__, but for the terminal.'''
        return self.__repr__()
