import pygame
import os
print(os.getcwd())
pygame.init()
size = (525, 450) # (wid, hei)
W = (255, 255, 255)
B = (0, 0, 0)
score = 0
# 建構視窗，以tuple為設定的單位
window = pygame.display.set_mode(size)
# 視窗塞顏色(以(R, G, B))
window.fill(W)
# 設置標題
pygame.display.set_caption("POPCAT")

# 設定字體
font = pygame.font.SysFont(None, 48)
score_surface = font.render(str(score), True, B)
title_surface = font.render("POPCAT", True, B)

# 建立畫布
sur = (525, 450)
surface = pygame.Surface(sur)
# .convert可以加速 
surface.convert()
surface.fill(W)

# 印入圖片
cat_close_image = pygame.image.load("popcat\\cat_close.jpg").convert()
cat_open_image = pygame.image.load("popcat\\cat_open.jpg").convert()

# 匯入聲音
pop_sound = pygame.mixer.Sound("popcat\\pop.mp3")

# 將畫布投射到視窗上面
# 視窗.blit(畫布, 座標)
window.blit(cat_close_image, (0, 0))
window.blit(title_surface, (10, 10))
window.blit(score_surface, (20, 60))

# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            window.fill(W) # 注意!!!! 刷新畫面!!!! 你可以試試看不刷新會怎樣!
            ## 更新分數/產生新的記分板
            score += 1
            score_surface = font.render(str(score), True, B)
            ## 播放聲音
            pop_sound.play()
            ## 更新貓貓圖片
            window.blit(cat_open_image, (0, 0))  
            print(score)
        ## 事件:放開滑鼠
        if event.type == pygame.MOUSEBUTTONUP:
            window.blit(cat_close_image, (0, 0))
    ## 顯示記分板 
    window.blit(title_surface, (10, 10))
    window.blit(score_surface, (20, 60))
    ## 更新畫面
    pygame.display.update()
pygame.quit()
