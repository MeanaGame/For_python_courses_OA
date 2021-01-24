import pygame as pg
num = input().split()
try:
    W = int(num[0])
    H = int(num[1])
except:
    print('Неправильный формат ввода')
pg.init()
app = pg.display.set_mode((W, H))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        
    pg.draw.line(app, (255, 255, 255), [0, 0],[W, H], 5)
    pg.draw.line(app, (255, 255, 255), [W, 0], [0, H], 5)

    pg.display.update()