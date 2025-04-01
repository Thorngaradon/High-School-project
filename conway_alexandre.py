import tkinter as tk
import random
from Element import Human  # Make sure this import is available
from PlanetTk import PlanetTk

class Conway(PlanetTk):
    def __init__(self, root, nbcell_latitude, nbcell_longitude, gutter_size=0, margin_size=0, cell_size=40):
        self.cell_size = cell_size
        self.nbcell_latitude = nbcell_latitude
        self.nbcell_longitude = nbcell_longitude
        self.taille_conway = nbcell_latitude * cell_size

        # Initialize the canvas to draw the grid
        self.canvas = tk.Canvas(root, width=self.nbcell_longitude * self.cell_size, 
                                height=self.nbcell_latitude * self.cell_size)
        self.canvas.pack()

        # Initialize the grid with empty cells
        self.grid = [[None for _ in range(self.nbcell_longitude)] for _ in range(self.nbcell_latitude)]
        self.initialize_grid()

    def initialize_grid(self):
        """Fill the grid with randomly alive cells."""
        for i in range(self.nbcell_latitude):
            for j in range(self.nbcell_longitude):
                # 50% chance for each cell to be alive
                if random.random() < 0.5:
                    self.grid[i][j] = Human()  # Alive cell
                else:
                    self.grid[i][j] = None  # Dead cell
        self.draw_grid()

    def draw_grid(self):
        """Draw the grid on the canvas."""
        for i in range(self.nbcell_latitude):
            for j in range(self.nbcell_longitude):
                color = "green" if isinstance(self.grid[i][j], Human) else "white"
                self.canvas.create_rectangle(j * self.cell_size, i * self.cell_size, 
                                             (j + 1) * self.cell_size, (i + 1) * self.cell_size,
                                             fill=color, outline="black")

    def etape(self):
        """Perform one cycle of Conway's game and replace the current grid with a new one."""
        nouvelle_grille = [[None for _ in range(self.nbcell_longitude)] for _ in range(self.nbcell_latitude)]

        for i in range(self.nbcell_latitude):
            for j in range(self.nbcell_longitude):
                # Apply Conway's rules
                nb_voisins = self.count_neighbors(i, j)
                current_cell = self.grid[i][j]

                if current_cell is None and nb_voisins == 3:
                    nouvelle_grille[i][j] = Human()  # Birth of a human cell
                elif isinstance(current_cell, Human) and 2 <= nb_voisins <= 3:
                    nouvelle_grille[i][j] = Human()  # The human cell survives
                else:
                    nouvelle_grille[i][j] = None  # The cell dies

        # Update the grid and redraw
        self.grid = nouvelle_grille
        self.canvas.delete("all")  # Clear the old drawing
        self.draw_grid()  # Redraw the updated grid

    def count_neighbors(self, x, y):
        """Count the number of living neighbors of a cell."""
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0
        for dx, dy in deltas:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.nbcell_latitude and 0 <= ny < self.nbcell_longitude:
                if isinstance(self.grid[nx][ny], Human):
                    count += 1
        return count

    def reset_jeu(self):
        '''Reset the game by setting all cells to None.'''
        self.grid = [[None for _ in range(self.nbcell_longitude)] for _ in range(self.nbcell_latitude)]
        self.canvas.delete("all")
        self.initialize_grid()

    def count_cell(self):
        """Count the number of living cells."""
        compteur = sum(1 for i in range(self.nbcell_latitude) for j in range(self.nbcell_longitude) if isinstance(self.grid[i][j], Human))
        self.canvas.update_idletasks()  # Force canvas update after counting
        return compteur
