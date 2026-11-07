import pygame as pg

FPS = 60
WIDTH, HEIGHT = 1000, 600
W_HOUSE = 300
H_HOUSE = 200

# цвета выбраны с сайта: https://htmlcolorcodes.com/
BLUE=(39, 42, 245)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 247, 0)
FIRE = (245, 112, 37)
GREEN = (7, 222, 30)
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

# при рисовании буду опираться на длину и ширину экрана: WIDTH, HEIGHT
# рисунок: настенные часы
# циферблат
pg.draw.rect(screen,BLUE, (0,0,WIDTH, HEIGHT / 2))
pg.draw.rect(screen,GREEN, (0,HEIGHT / 2,WIDTH, HEIGHT / 2))
pg.draw.rect(screen,FIRE, (WIDTH-400,HEIGHT / 4,W_HOUSE,H_HOUSE))
pg.draw.circle(screen,BLUE , (750,250 ), 50)
pg.draw.polygon(screen, BLACK,
                  [[WIDTH-400,HEIGHT / 4], [750,75], [WIDTH-400+300,HEIGHT / 4]])
pg.draw.circle(screen,ORANGE , (150,150 ), 75)
pg.draw.line(screen, ORANGE, [10, 150], [290, 150], 7)
pg.draw.line(screen, ORANGE, [150, 20], [150, 280], 7)
pg.draw.line(screen, ORANGE, [290,20], [10, 280], 8)
pg.draw.line(screen, ORANGE, [10,20], [290, 280], 8)
pg.draw.line(screen, BLACK, [700,250], [800, 250], 8)
pg.draw.line(screen, BLACK, [750,200], [750, 300], 8)


# отображаем нарисованные объекты
pg.display.update()

flag_play = True
while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    pg.display.update()
