import tkinter as tk
from PlanetTk import PlanetTk
from Element import *

class Turm(PlanetTk):
    __AUTHORIZED_CLASS = {Turmite, Sand}

    def __init__(self, root, WIDTH, HEIGHT, DIM, DELAY=1, rgb=None):
        '''Initialize the Turmite.'''
        PlanetTk.__init__(self, root, DIM, DIM, Turm.__AUTHORIZED_CLASS, HEIGHT // DIM, 0, 0)
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self.__DIM = DIM
        self.__UNIT = HEIGHT // DIM
        self.__DELAY = DELAY if isinstance(DELAY, int) else 5

        # Set the color of the Turmite
        self.__COLOR_ON = self.rgb_to_hex(rgb) if rgb else Turmite().get_color()
        print(f"Color applied to the Turmite: {self.__COLOR_ON}")
        self.__COLOR_OFF = Sand().get_color()

        self.__items = [[0] * DIM for _ in range(DIM)]

        # Set the initial position and direction of the Turmite
        self.__pos = (DIM // 2, DIM // 2)
        self.__drn = "N"

        self._animating = False

        # Start the animation
        self.anim(self.__pos, self.__drn)

    def get_dim(self):
        '''Return the dimension of the Turmite.'''
        return self.__DIM

    def draw_square(self, i, j):
        '''Draw a square at position (i, j) with the Turmite's color.'''
        x = j * self.__UNIT
        y = i * self.__UNIT
        x = min(x, self.__WIDTH - self.__UNIT)
        y = min(y, self.__HEIGHT - self.__UNIT)
        square = self.create_rectangle(x, y, x + self.__UNIT, y + self.__UNIT, fill=self.__COLOR_ON, outline='')
        return square

    def draw(self, pos, drn, items):
        '''Draw the Turmite at position (i, j) with direction drn.'''
        i, j = pos
        i, j = i % self.__DIM, j % self.__DIM
        (ii, jj), ndrn = self.bouger(pos, drn, items)
        square = items[i][j]
        if square == 0:
            square = self.draw_square(i, j)
            items[i][j] = square
        else:
            self.delete(square)
            items[i][j] = 0
        return (ii, jj), ndrn

    def bouger(self, pos, drn, items):
        '''Move the Turmite to position (i, j) with direction drn.'''
        i, j = pos
        i, j = i % self.__DIM, j % self.__DIM
        if items[i][j] == 0:
            if drn == "N":
                r = (i - 1, j), "E"
            elif drn == "S":
                r = (i + 1, j), "W"
            elif drn == "E":
                r = (i, j + 1), "S"
            elif drn == "W":
                r = (i, j - 1), "N"
        else:
            if drn == "N":
                r = (i + 1, j), "W"
            elif drn == "S":
                r = (i - 1, j), "E"
            elif drn == "E":
                r = (i, j - 1), "N"
            elif drn == "W":
                r = (i, j + 1), "S"
        i, j = r[0]
        i, j = i % self.__DIM, j % self.__DIM
        return (i, j), r[1]

    def anim(self, pos, drn):
        '''Start the Turmite animation.'''
        if not self._animating:
            self._animating = True
            pos, drn = self.draw(pos, drn, self.__items)
            if isinstance(self.__DELAY, int):
                self.after(self.__DELAY, self._anim_complete, pos, drn)
            else:
                print(f"Error: DELAY is not an integer, but {type(self.__DELAY)}.")

    def _anim_complete(self, pos, drn):
        '''Complete the Turmite animation.'''
        self._animating = False
        self.anim(pos, drn)

    def rgb_to_hex(self, rgb):
        '''Convert an RGB value to a hexadecimal string.'''
        print(f"Converting RGB -> Hex: {rgb}")
        if isinstance(rgb, tuple) and len(rgb) == 3:
            r, g, b = rgb
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return f"#{r:02x}{g:02x}{b:02x}".upper()
        print(f"Invalid RGB value: {rgb}, using #FFFFFF")
        return "#FFFFFF"

