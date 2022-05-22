import pygame
import random
from sys import exit

class color:
    color = {
        'black' : (0, 0, 0), 
        'grey' : (85, 85, 85), 
        'white' : (255, 255, 255),
        'red' : (229, 46, 8),
        'darkRed' : (157, 31, 6),
        'green' : (64, 201, 73),
        'darkGreen' : (36, 127, 42),
        'blue' : (78, 124, 246),
        'darkBlue' : (9, 53, 174),
        'purple' : (182, 72, 242),
        'darkPurple' : (116, 12, 172)
        }
    @classmethod
    def rc(self, name):
        return color.color[name]


class Text:
    def __init__(self, txt, size, color, font):
        font = pygame.font.SysFont(font, size)
        self.surface = font.render(txt, True, color)
        self.rect = self.surface.get_rect()

    def midleft(self, x, y, windows):
        self.rect.midleft = (x, y)
        windows.blit(self.surface, self.rect)


class Snake(color):
    def __init__(self, c1, c2, head):
        self.color1 = super().rc(c1)
        self.color2 = super().rc(c2)
        self.head = head
        self.body = [head]
        self.direction = 'RIGHT'
        self.new_direction = 'RIGHT'
        length = 4
        for i in range(length - 1):
            self.head[0] += unit
            self.body.insert(0, list(self.head))
    def set_snake_dir(self):
        if event.key == pygame.K_d:
            self.new_direction = 'RIGHT'
        elif event.key == pygame.K_a:
            self.new_direction = 'LEFT'
        elif event.key == pygame.K_s:
            self.new_direction = 'DOWN'
        elif event.key == pygame.K_w:
            self.new_direction = 'UP'
    def change_snake_dir(self):
        if self.new_direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'
        elif self.new_direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        elif self.new_direction == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        elif self.new_direction == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
    def move_snake(self):
        if snake.direction == 'RIGHT':
            snake.head[0] += unit
        elif snake.direction == 'LEFT':
            snake.head[0] -= unit
        elif snake.direction == 'DOWN':
            snake.head[1] += unit
        elif snake.direction == 'UP':
            snake.head[1] -= unit
    def game_over(self, canvas):
        if not (0 <= self.head[0] < canvas.canvas_x) or not(0 <= self.head[1] < canvas.canvas_y) or not(0 <= self.head[1] < canvas.canvas_y):
            return 1
        return 0
    def fruit_eaten(self, fruit, canvas):
        if self.head == fruit.pos:
            fruit_sfx.play()
            fruit.spawn(canvas)
            window.score += 1
        else:
            self.body.pop()
    
class game_setting:
    def __init__(self, canvas_x, canvas_y):
        self.canvas_x = canvas_x
        self.canvas_y = canvas_y
        self.canvas = pygame.Surface((canvas_x, canvas_y))
    def refresh(self):
        self.canvas.blit(background, (0, 0))
    @staticmethod
    def set_game_speed():
        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < 1000 // game_speed:
            pygame.event.pump()
    def draw_things(self, snake):
        pygame.draw.rect(self.canvas, color.rc('grey'), (snake.head[0], snake.head[1], unit + 2, unit + 2))
        for body in snake.body[1:]:
            pygame.draw.rect(self.canvas, color.rc('grey'), (body[0] + 1, body[1] + 1, unit, unit))

        pygame.draw.rect(self.canvas, snake.color1, (snake.head[0] - 1, snake.head[1] - 1, unit + 2, unit + 2))
        pygame.draw.rect(self.canvas, snake.color2, (snake.head[0] - 1, snake.head[1] - 1, unit + 2, unit + 2), 2)

        for body in snake.body[1:]:
            pygame.draw.rect(self.canvas, snake.color1, (body[0], body[1], unit, unit))
            pygame.draw.rect(self.canvas, snake.color2, (body[0], body[1], unit, unit), 2)

        self.canvas.blit(face, snake.head)

        pygame.draw.rect(self.canvas, color.rc('grey'), (fruit.pos[0] + 3, fruit.pos[1] + 3, unit - 4, unit - 4), 0, 3)
        pygame.draw.rect(self.canvas, color.rc('red'), (fruit.pos[0] + 2, fruit.pos[1] + 2, unit - 4, unit - 4), 0, 3)
        pygame.draw.rect(self.canvas, color.rc('darkRed'), (fruit.pos[0] + 2, fruit.pos[1] + 2, unit - 4, unit - 4), 2, 3)


class Fruit:
    def __init__(self, canvas):
        self.pos = [0, 0]
        self.spawn(canvas)

    def spawn(self, canvas):
        self.pos = [random.randrange(0, canvas.canvas_x, unit),
                    random.randrange(0, canvas.canvas_y, unit)]
        if self.pos in snake.body:
            self.spawn()

class window:
    score = 0
    def __init__ (self, width, height, text="視窗名稱"):
        self.sizes = (width,height)
        self.text = text
        self.window = pygame.display.set_mode(self.sizes)
    def start_window(self):
        pygame.display.set_caption(self.text)
    def refresh(self, border, canvas):
        self.window.blit(border, (0, 0))
        self.window.blit(canvas.canvas, (30, 120))
        Text(str(window.score), 45, color.rc('white'), "impact").midleft(90, 45, self.window)
    def game_over(self, game_over, game_over_sfx):
        game_over_sfx.play()
        self.window.blit(game_over, (0, 0))
pygame.init()
windows = window(780,780,"hungry_snake")
windows.start_window()


background = pygame.image.load("hungrysnake/background.png").convert()
border = pygame.image.load("hungrysnake/border.png").convert()
face = pygame.image.load("hungrysnake/face.png").convert_alpha()
game_over = pygame.image.load("hungrysnake/game_over.png").convert_alpha()

pygame.mixer.init()
bgm = pygame.mixer.Sound("hungrysnake/bgm.wav")
fruit_sfx = pygame.mixer.Sound("hungrysnake/fruit.wav")
game_over_sfx = pygame.mixer.Sound("hungrysnake/game_over.wav")
bgm.play(-1)

game_speed = 10
unit = 30
canvas = game_setting(720, 630)

while True:

    snake = Snake('green', 'darkGreen', [0, 0])
    fruit = Fruit(canvas)

    while True:
        game_setting.set_game_speed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                snake.set_snake_dir()
        snake.change_snake_dir()
        snake.move_snake()
        snake.body.insert(0, list(snake.head))
        snake.fruit_eaten(fruit, canvas)
        # 判斷遊戲結束
        if snake.game_over(canvas):
            break
        
        canvas.refresh()
        canvas.draw_things(snake)
        
        windows.refresh(border, canvas)


        pygame.display.update()

    windows.game_over(game_over, game_over_sfx)
    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False