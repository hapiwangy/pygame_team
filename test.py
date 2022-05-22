import pygame

from hungrysnake.hugnrysnake import *

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