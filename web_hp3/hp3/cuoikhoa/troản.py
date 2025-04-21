import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master, canvas_size=400, cell_size=20):
        self.master = master
        self.master.title("Snake Game")
        self.canvas_size = canvas_size
        self.cell_size = cell_size
        self.canvas = tk.Canvas(master, width=canvas_size, height=canvas_size, bg="black")
        self.canvas.pack()

        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.direction = "Right"
        self.food = self.create_food()

        self.master.bind("<KeyPress>", self.on_key_press)
        self.update()

    def create_food(self):
        x = random.randrange(0, self.canvas_size, self.cell_size)
        y = random.randrange(0, self.canvas_size, self.cell_size)
        return self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size, fill="red")

    def move(self):
        head = list(self.snake[0])
        if self.direction == "Right":
            head[0] += self.cell_size
        elif self.direction == "Left":
            head[0] -= self.cell_size
        elif self.direction == "Up":
            head[1] -= self.cell_size
        elif self.direction == "Down":
            head[1] += self.cell_size

        self.snake.insert(0, tuple(head))

        if self.check_collision():
            self.game_over()
            return

        if self.check_food():
            self.canvas.delete(self.food)
            self.food = self.create_food()
        else:
            self.canvas.delete(self.snake[-1])
            self.snake.pop()

        self.draw_snake()

    def draw_snake(self):
        self.canvas.delete("snake")
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + self.cell_size,
                                         segment[1] + self.cell_size, fill="green", tags="snake")

    def check_collision(self):
        head = self.snake[0]
        return (
            head in self.snake[1:] or
            head[0] < 0 or head[0] >= self.canvas_size or
            head[1] < 0 or head[1] >= self.canvas_size
        )

    def check_food(self):
        head = self.snake[0]
        food_coords = self.canvas.coords(self.food)
        return head[0] == food_coords[0] and head[1] == food_coords[1]

    def on_key_press(self, event):
        key = event.keysym
        if key in ["Up", "Down", "Left", "Right"]:
            opposite_directions = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
            if key != opposite_directions.get(self.direction):
                self.direction = key

    def game_over(self):
        self.canvas.create_text(self.canvas_size // 2, self.canvas_size // 2, text="Game Over", fill="white",
                                font=("Helvetica", 16, "bold"))

    def update(self):
        self.move()
        self.master.after(100, self.update)

if __name__ == "__main__":
    root = tk.Tk()
    snake_game = SnakeGame(root)
    root.mainloop()
