import pygame as pg

W, H, FPS = 1000, 700, 15
x, y, rad, rad1 = W // 2, H // 2, 75, 45
pg.init()
app = pg.display.set_mode((W, H))
TAP = 5
jump = 0
up_jump = -15
blue, black = (120, 120, 200), (0, 0, 0)
colnow = blue
x_start, y_start = 80, 620 
walk = 5 #Перемещение
x1, x2, x3, x4 = x, x, x, x
y1, y2, y3, y4 = y, y, y, y
walk1, walk2, walk3, walk4 = walk, walk, walk, walk


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    keys = pg.key.get_pressed()
    if keys[pg.K_DOWN]:
        y_start += TAP
    if keys[pg.K_RIGHT] and x_start < 925:
        x_start += TAP
    if keys[pg.K_LEFT] and x_start > 75 :
        x_start -= TAP
    if keys[pg.K_SPACE] and jump == 0:
        jump = 1
    #Основной прыжок, параболы
    if jump == 1:
        if up_jump <= 15:
            #Из физики при броске снизу вверх, вначале отрицательное ускоренее и v > 0 , затем v = 0,
            if up_jump > 0:
                y_start += (up_jump ** 2) / 3
            else:
                # далее v < 0 и положительное ускорение из-за силы притяжения
                y_start -= (up_jump ** 2) / 3
            up_jump += 1
            colnow = black
        else:
            jump = 2
            up_jump = -8
    #После отскока
    if jump == 2:
        if up_jump <= 8:
            if up_jump > 0:
                y_start += (up_jump ** 2) / 3
            else: 
                y_start -= (up_jump ** 2) / 3
            up_jump += 1
        else:
            jump = 3
            up_jump = -4
    #Смягчение при приземлении :3
    if jump == 3:
        if up_jump <= 4:
            if up_jump > 0:
                y_start += (up_jump ** 2) / 4
            else: 
                y_start -= (up_jump ** 2) / 4
            up_jump += 1
        else:
            jump = 0
            up_jump = -15
            colnow = blue
    #Движение влево вправо
    if x1 > W + rad1 - 90:
        walk1 = -5
    if x1 < - rad1 + 90:
        walk1 = 5
    x1 += 1 * walk1
    #Движение по левой диагонали
    if x2 > W - rad1 - 90 and y2 > H + rad1 - 90:
        walk2 = -5
    if x2 < rad1 + 90 and y2 < H - rad1 + 90:
        walk2 = 5
    x2 += 1 * walk2
    y2 += 1 * walk2
    #Движение по правой диагонали
    if x3 > W - rad1 - 90 and y3 < H - rad1 + 90:
        walk3 = -4
    if x3 < rad1 + 90 and y3 > H + rad1 - 90:
        walk3 = 4
    x3 += 1 * walk3
    y3 -= 1 * walk3
    #Движение вверх вниз
    if y4 > W + rad1 - 400:
        walk4 = -6
    if y4 < - rad1 + 90:
        walk4 = 6
    y4 += 1 * walk4

    app.fill((205,245,250))
    pg.draw.circle(app, colnow, (x_start, y_start), rad)


    pg.draw.circle(app, (100, 200, 50), (x1, y1), rad1)
    pg.draw.circle(app, (200, 100, 50), (x2, y2), rad1)
    pg.draw.circle(app, (200, 50, 100), (x3, y3), rad1)
    pg.draw.circle(app, (50, 200, 100), (x4, y4), rad1)


    pg.display.update()
    pg.time.delay(FPS)
