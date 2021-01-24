import pygame as pg

W, H, FPS = 500, 500, 15
x, y, rad, rad1 = W // 2, H // 2, 75, 45
pg.init()
app = pg.display.set_mode((W, H))


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        
    pg.draw.ellipse(app, (250, 250, 250),(50, 100, 400, 300))
    pg.draw.ellipse(app, (0, 0, 0),(50, 100, 380, 280))

    pg.display.update()
    pg.time.delay(FPS)
