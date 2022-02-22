from re import S
from textwrap import fill
import tkinter as tk

class GameObject(object):
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item
    def get_position(self):
        return self.canvas.coords(self.item)
    def move(self, x, y):
        self.canvas.move(self.item, x, y)
    def delete(self):
        self.canvas.delete(self.item)

class Ball(GameObject):
    def __init__(self, canvas, x, y):
        self.radius = 10
        self.direction = (1, -1)
        self.speed = 10
        item = canvas.create_oval(x-self.radius, y-self.radius, x+self.radius, y+self.radius, fill="#ffffff")
        super(Ball, self).__init__(canvas, item)

    def update(self):
        coords = self.get_position()
        width = self.canvas.winfo_width()
        x = self.speed * self.direction[0]
        y = self.speed * self.direction[1]
        if coords[0] + x < 0 or coords[2] + x > 0:
            x = -x
        if coords[1] + y < 50:
            y = -y
        self.move(x, y)

class Paddle(GameObject):
    def __init__(self, canvas, x, y):
        self.width = 80
        self.height = 20
        item = canvas.create_rectangle(x-self.width/2, y-self.height/2, x+self.width/2, y+self.height/2, fill="#ffaa00")
        super(Paddle, self).__init__(canvas, item)

    def set_ball(self, ball):
        self.ball = ball

    def move(self, offset):
        paddle_coords = self.get_position()
        canvas_width = self.canvas.winfo_width()
        if paddle_coords[0] + offset > 0 and paddle_coords[2] + offset < canvas_width:
            super().move(offset, 0)
            if self.ball is not None:
                self.ball.move(offset, 0)

class Brick(GameObject):
    def __init__(self, canvas, x, y):
        self.width = 75
        self.height = 20
        item = canvas.create_rectangle(x-self.width/2, y-self.height/2, x+self.width/2, y+self.height/2, fill="#cccccc")
        super(Brick, self).__init__(canvas, item)

class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.width = 610
        self.height = 600
        self.canvas = tk.Canvas(master, width=self.width, height=self.height, background="#cfffff")
        self.canvas.pack()
        self.pack()

        self.ball = Ball(self.canvas, self.width/2, self.height/2)
        self.paddle = Paddle(self.canvas, self.width/2, self.height/2+20)
        self.canvas.focus_set()
        self.canvas.bind('<Left>', lambda _: self.paddle.move(-10))
        self.canvas.bind('<Right>', lambda _: self.paddle.move(10))
        for i in range(5, self.width-5, 75):
            Brick(self.canvas, i+37.5, 90)
            Brick(self.canvas, i+37.5, 50)
            Brick(self.canvas, i+37.5, 70)

        self.setup()

    def setup(self):
        self.draw_text(300, 200, text="Start")
        if self.ball is not None:
            self.ball.delete()
        paddle_pos = self.paddle.get_position()
        self.ball = Ball(self.canvas, (paddle_pos[0]+paddle_pos[2])*0.5, paddle_pos[1]-20)
        self.paddle.set_ball(self.ball)
        self.canvas.bind('<space>', lambda _: self.start_game())

    def draw_text(self, x, y, text, size=40):
        font = ('Helvetica', size)
        self.canvas.create_text(x, y, text=text, font=font)

    def start_game(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Test")
    game = Game(root)
    game.mainloop()