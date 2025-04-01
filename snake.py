from tkinter import *
import random
from Element import *
from PlanetTk import PlanetTk

# === Game Constants ===
GRID_WIDTH = 25  # grid width
GRID_HEIGHT = 25  # grid height
SPACE_SIZE = 20  # size of each square
WIDTH = GRID_WIDTH * SPACE_SIZE  # total width
HEIGHT = GRID_HEIGHT * SPACE_SIZE  # total height
INITIAL_SPEED = 200  # initial speed in milliseconds
SPEED_DECREASE = 10  # speed decrease when eating food
MIN_SPEED = 50  # minimum speed

SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FFFFFF"
OBSTACLE_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

NUM_OBSTACLES = 18  # number of obstacles

# === Main Game Class ===
class SnakeGame(PlanetTk):
    '''Main class for the snake game'''

    def __init__(self, master):
        # Initialize the game
        super().__init__(
            master,
            WIDTH,
            HEIGHT,
            [],
            cell_size=40,
            gutter_size=0,
            margin_size=5 
        )

        self.score = 0
        self.direction = 'down'
        self.speed = INITIAL_SPEED  # Initial speed

        self.snake = Snake()
        self.food = Food()
        self.obstacles = self.create_obstacles()  # To manage obstacles

        # UI Elements
        self.label = Label(self, text=f"Points: {self.score}", font=('consolas', 20))
        self.label.pack()

        self.canvas = Canvas(self, bg=BACKGROUND_COLOR, height=HEIGHT, width=WIDTH)
        self.canvas.pack(fill=BOTH, expand=True)

        self.snake.create_snake(self.canvas)
        self.food.create_food(self.canvas)
        self.draw_obstacles()

        # Controls
        self.bind_all('<Left>', lambda event: self.change_direction('left'))
        self.bind_all('<Right>', lambda event: self.change_direction('right'))
        self.bind_all('<Up>', lambda event: self.change_direction('up'))
        self.bind_all('<Down>', lambda event: self.change_direction('down'))

        self.next_turn()

    def create_obstacles(self):
        '''Generates a list of obstacle positions, avoiding the initial position of the snake and the food.'''
        obstacles = []
        for _ in range(NUM_OBSTACLES):
            while True:
                x = random.randint(0, GRID_WIDTH - 1) * SPACE_SIZE
                y = random.randint(0, GRID_HEIGHT - 1) * SPACE_SIZE
                if (x, y) not in self.snake.coordinates and (x, y) != tuple(self.food.coordinates):
                    obstacles.append((x, y))
                    break
        return obstacles

    def draw_obstacles(self):
        '''Draws obstacles on the canvas.'''
        for x, y in self.obstacles:
            self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=OBSTACLE_COLOR, tag="obstacle")

    def next_turn(self):
        '''Handles the snake's movement and game progression.'''
        x, y = self.snake.coordinates[0]

        if self.direction == "up":
            y -= SPACE_SIZE
        elif self.direction == "down":
            y += SPACE_SIZE
        elif self.direction == "left":
            x -= SPACE_SIZE
        elif self.direction == "right":
            x += SPACE_SIZE

        self.snake.coordinates.insert(0, (x, y))
        square = self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
        self.snake.squares.insert(0, square)

        # Collision with food
        if (x, y) == tuple(self.food.coordinates):
            self.score += 1
            self.label.config(text=f"Points: {self.score}")
            self.canvas.delete("food")
            self.food = Food()
            self.food.create_food(self.canvas)

            # Increase game speed
            self.speed = max(self.speed - SPEED_DECREASE, MIN_SPEED)

        else:
            # Move the snake by removing the tail
            del self.snake.coordinates[-1]
            self.canvas.delete(self.snake.squares[-1])
            del self.snake.squares[-1]

        if self.check_collisions():
            self.game_over()
        else:
            self.after(self.speed, self.next_turn)  # Use the updated speed

    def change_direction(self, new_direction):
        '''Changes the snake's direction based on user input.'''
        opposite_directions = {
            'left': 'right',
            'right': 'left',
            'up': 'down',
            'down': 'up'
        }
        if new_direction != opposite_directions.get(self.direction):
            self.direction = new_direction

    def check_collisions(self):
        '''Checks if the snake collides with a wall, itself, or an obstacle.'''
        x, y = self.snake.coordinates[0]

        # Collision with walls
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            return True

        # Collision with the snake's body
        for body_part in self.snake.coordinates[1:]:
            if (x, y) == body_part:
                return True

        # Collision with obstacles
        if (x, y) in self.obstacles:
            return True

        return False

    def game_over(self):
        '''Displays the game over screen.'''
        self.canvas.delete(ALL)
        self.canvas.create_text(
            self.canvas.winfo_width() / 2,
            self.canvas.winfo_height() / 2,
            font=('consolas', 70),
            text="GAME OVER",
            fill="red",
            tag="gameover"
        )
