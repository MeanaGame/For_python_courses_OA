import pygame as pg

num = int(input())

W, H, FPS = 300, 300, 15
x, y = W // 2, H // 2
pg.init()
app = pg.display.set_mode((W, H))
first_step = 0
tap = H//num

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    while num != 0:
        first_step += tap
        pg.draw.ellipse(app, (250, 250, 250),(0, y - y//3, H, first_step), 1)
        pg.draw.ellipse(app, (250, 250, 250),(x - x//3, 0, first_step, H), 1)
        num -= 1

    pg.display.update()
    pg.time.delay(FPS)
