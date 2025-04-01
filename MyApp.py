import tkinter as tk
import random
from Turmites import *
from conway_alexandre import *
from snake import *

class MyApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Projet Fil rouge groupe n°5")
        
        #starts initial frame
        self.__initial_frame = tk.Frame(self, width=800, height=500)
        self.__initial_frame.grid(row=0, column=0, padx=10, pady=10)
        
        #title's frame
        self.__titre_frame = tk.Label(self.__initial_frame, text="Projet fil rouge", height=2, font=("Arial", 30, "bold"))
        self.__titre_frame.grid(row=0, column=0, columnspan=3, pady=10)

        #start buttons for the games
        self.__initial_turmite = tk.Button(self.__initial_frame, text="TURMITE", width=20, height=5, font=("Arial", 20), command=self.play_turm)
        self.__initial_conway = tk.Button(self.__initial_frame, text="CONWAY", width=20, height=5, font=("Arial", 20), command=self.play_conway)
        self.__initial_snake = tk.Button(self.__initial_frame, text="SNAKE", width=20, height=5, font=("Arial", 20), command=self.play_snake)

        self.__initial_turmite.grid(row=1, column=0, padx=10, pady=10)
        self.__initial_conway.grid(row=1, column=1, padx=10, pady=10)
        self.__initial_snake.grid(row=1, column=2, padx=10, pady=10)

        #turmite's entries and buttons
        self.entries = []
        self.rgb = (255, 0, 0)
        self.taille = 400
        self.create_entries_and_buttons()

        #quite button frame
        self.__quit_button = tk.Button(self.__initial_frame, text="Quitter", width=10, height=2, font=("Arial", 10), command=self.quit)
        self.__quit_button.grid(row=7, column=0, columnspan=3, pady=20)

    def create_entries_and_buttons(self):
        '''create entries and button for turmite frames and turmite color'''
        tk.Label(self.__initial_frame, text="Taille de la frame Turmite (carré) :").grid(row=2, column=0, pady=5, sticky="w", padx=10)
        entry = tk.Entry(self.__initial_frame, width=30)
        entry.grid(row=2, column=1, pady=5, padx=10)
        self.entries.append(entry)

        ## Labels and entries for RGB values
        rgb_labels = ["Rouge", "Vert", "Bleu"]
        for i, color in enumerate(rgb_labels):
            tk.Label(self.__initial_frame, text=f"Couleur {color} :").grid(row=3+i, column=0, pady=5, sticky="w", padx=10)
            color_entry = tk.Entry(self.__initial_frame, width=30)
            color_entry.grid(row=3+i, column=1, pady=5, padx=10)
            self.entries.append(color_entry)

        #randomizer button and submit button
        tk.Button(self.__initial_frame, text="Submit", command=self.submit).grid(row=6, column=1, pady=5, padx=10)
        tk.Button(self.__initial_frame, text="Random", command=self.generate_random_color).grid(row=6, column=0, pady=5, padx=10)

    def generate_random_color(self):
        '''set random values for color'''
        self.rgb = tuple(random.randint(0, 255) for _ in range(3))
        for entry, value in zip(self.entries[1:4], self.rgb):
            entry.delete(0, tk.END)
            entry.insert(0, str(value))
        print(f"Nouvelle couleur RGB : {self.rgb}")

    def submit(self):
        '''Create the submit button'''
        taille_value = self.entries[0].get()
        if taille_value.isdigit() and int(taille_value) > 0:
            self.taille = int(taille_value)
        else:
            print("Veuillez entrer une taille valide (entier positif).")
            return

        rgb_values = []
        for entry in self.entries[1:4]:
            try:
                color_value = int(entry.get())
                if 0 <= color_value <= 255:
                    rgb_values.append(color_value)
                else:
                    print("Valeur RGB invalide. Entrez un nombre entre 0 et 255.")
                    return
            except ValueError:
                print("Veuillez entrer un nombre valide pour la couleur RGB.")
                return

        self.rgb = tuple(rgb_values)
        print(f"Taille de la frame : {self.taille}, Couleur RGB : {self.rgb}")

    def play_turm(self):
        '''make a game window for turmite experiment'''
        game_window = tk.Toplevel(self)
        game_window.title("Turmite experiment")
        game_window.geometry("1000x500")
        
        ## Create a frame for the turmite game
        self.__turmite_frame = tk.Frame(game_window, width=self.taille, height=self.taille, bd=2, relief="solid")
        self.__turmite_frame.pack_propagate(False)
        self.__turmite_frame.pack(side=tk.LEFT, padx=50)
        
        #label for the turmite game
        tk.Label(game_window, text="Turmite, les fourmis de Langton", height=2, font=("Arial", 15)).pack(side=tk.TOP, pady=1)
        
        #laucnh the turmite game
        turmite_game = Turm(self.__turmite_frame, self.taille, self.taille, 100, rgb=self.rgb)
        turmite_game.pack()

        #makes the game work
        turmite_game.anim((self.taille // 2, self.taille // 2), "N")
        
        #quit button
        tk.Button(game_window, text="Quitter", command=game_window.destroy).pack(side=tk.BOTTOM, pady=10)

    def play_conway(self):
        '''make game window for conway game'''
        game_window = tk.Toplevel(self)
        game_window.title("Conway Game")
        game_window.geometry("1000x700")
        
        #create a frame for the conway game
        self.__conway_frame = tk.Frame(game_window, width=600, height=600, bd=2, relief="solid")
        self.__conway_frame.pack_propagate(False)
        self.__conway_frame.pack(side=tk.LEFT, padx=50)

        #initiates the game
        conway_game = Conway(self.__conway_frame, 20, 20, cell_size=30)

        #add a frame for the side bar
        self._side_frame = tk.Frame(game_window, width=200, height=400, bd=2, relief="solid", padx=-10)
        self._side_frame.pack_propagate(False)
        self._side_frame.pack(side=tk.RIGHT)

        #label for alive cells
        self._cell_count_label = tk.Label(self._side_frame, text=f"Cellules vivantes : {conway_game.count_cell()}")
        self._cell_count_label.pack(pady=10)

        #quit button
        tk.Button(game_window, text="Quitter", command=game_window.destroy).pack(side=tk.BOTTOM, pady=10)
        tk.Button(game_window, text="Rejouer", command=lambda: self.reset_conway(conway_game)).pack(side=tk.BOTTOM, pady=10)

        #automatically start the game
        self.update_conway(conway_game, game_window)

    def update_conway(self, conway_game, game_window):
        """met a jour le jeu de Conway en appelant la méthode etape() périodiquement."""
        conway_game.etape()  

        #update the grid and the label
        self._cell_count_label.config(text=f"Cellules vivantes : {conway_game.count_cell()}")
        self._cell_count_label.update_idletasks()
        game_window.after(1000, self.update_conway, conway_game, game_window)

    def reset_conway(self, conway_game):
        """Réinitialise le jeu de Conway."""
        conway_game.reset_jeu()  #reset the game
        self._cell_count_label.config(text=f"Cellules vivantes : {conway_game.count_cell()}")  #update the label

    def play_snake(self):
        '''make a window for the snake game'''
        game_window = tk.Toplevel(self)
        game_window.title("Snake game")
        game_window.geometry("1000x700")

        #initiate the game
        snake_game = SnakeGame(game_window)
        snake_game.pack()

        #quit button
        tk.Button(game_window, text="Quitter", command=game_window.destroy).pack(side=tk.BOTTOM, pady=10)
        tk.Button(game_window, text="Rejouer", command=snake_game.reset_jeu).pack(side=tk.BOTTOM, pady=10)

if __name__ == '__main__':
    #start the main application
    my_app = MyApp()
    my_app.mainloop()
