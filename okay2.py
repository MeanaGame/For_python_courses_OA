import pygame as pg

Wh = [255] * 3
Bl = [0] * 3
Rd =(255, 0, 0)
Blu =(0, 0, 255)
Gr = (0, 250, 0)

clock = pg.time.Clock()
W, H, FPS = 600, 600, 60
count_roll = 1  #Счетчик для хода игроков (первых, потом второй, потом опять первый и тп)
A1, A2, A3, B1, B2, B3, C1, C2, C3 = 0, 0, 0, 0, 0, 0, 0, 0, 0 #Для позиций крестиков или ноликов
time_roll = 0  #Для счетчика ходов
app = pg.display.set_mode((W, H))
app.fill(Wh)
#Сетка для игры
pg.draw.line(app, Bl, (W // 3, 0), (W // 3, H), 3)
pg.draw.line(app, Bl, (W // 3 * 2, 0), (W // 3 * 2, H), 3)
pg.draw.line(app, Bl, (0, H // 3), (W, H // 3), 3)
pg.draw.line(app, Bl, (0, H // 3 * 2), (W, H // 3 * 2), 3)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.exit()

    keys = pg.key.get_pressed()
    #обновление сетки
    if keys[pg.K_SPACE]:
        app.fill(Wh)
        pg.draw.line(app, Bl, (W // 3, 0), (W // 3, H), 3)
        pg.draw.line(app, Bl, (W // 3 * 2, 0), (W // 3 * 2, H), 3)
        pg.draw.line(app, Bl, (0, H // 3), (W, H // 3), 3)
        pg.draw.line(app, Bl, (0, H // 3 * 2), (W, H // 3 * 2), 3)
        A1, A2, A3, B1, B2, B3, C1, C2, C3 = 0, 0, 0, 0, 0, 0, 0, 0, 0
        time_roll = 0  # Обновляет счетчик
        
    if pg.mouse.get_pressed()[0]:
        x, y = pg.mouse.get_pos()
        #ход для крестика
        if count_roll == 1:
            if x < W // 3 and x > 0:
                if y > 0 and y < H // 3:
                    pg.draw.line(app, Rd, (W // 15, H // 15), \
                        (W // 15 * 4, H // 15 * 4), 7)
                    pg.draw.line(app, Rd, (W // 15 * 4, H // 15), \
                        (W // 15 , H // 15 * 4), 7)
                    A1 = 'x'
                if y > H // 3 and y < H // 3 * 2:
                    pg.draw.line(app, Rd, (W // 15, H // 15 * 6),\
                        (W // 15 * 4, H // 15 * 9), 7)
                    pg.draw.line(app, Rd, (W // 15 * 4,H // 15 * 6),\
                        (W // 15, H // 15 * 9), 7)
                    B1 = 'x'
                if y < H  and y > H // 3 * 2:
                    pg.draw.line(app, Rd, (W // 15, H // 15 * 11),\
                        (W // 15 * 4, H // 15 * 14), 7)
                    pg.draw.line(app, Rd, (W // 15 * 4,H // 15 * 11),\
                        (W // 15, H // 15 * 14), 7)
                    C1 = 'x'
            if x > W // 3 and x < W // 3 * 2:
                if y > 0 and y < H // 3:
                    pg.draw.line(app, Rd, (W // 15 * 6, H // 15), \
                        (W // 15 * 9 , H // 15 * 4), 7)
                    pg.draw.line(app, Rd, ( W // 15 * 9, H // 15 ), \
                        (W // 15 * 6, H // 15 * 4), 7)
                    A2 = 'x'
                if y > H // 3 and y < H // 3 * 2:
                    pg.draw.line(app, Rd, (W // 15 * 6, H // 15 * 6),\
                        (W // 15 * 9, H // 15 * 9), 7)
                    pg.draw.line(app, Rd, (W // 15 * 9,H // 15 * 6),\
                        (W // 15 * 6, H // 15 * 9), 7)
                    B2 = 'x'
                if y < H  and y > H // 3 * 2:
                    pg.draw.line(app, Rd, (W // 15 * 6, H // 15 * 11),\
                        (W // 15 * 9, H // 15 * 14), 7)
                    pg.draw.line(app, Rd, (W // 15 * 9,H // 15 * 11),\
                        (W // 15 * 6, H // 15 * 14), 7)
                    C2 = 'x'
            if x < W  and x > W // 3 * 2:
                if y > 0 and y < H // 3:
                    pg.draw.line(app, Rd, (W // 15 * 11, H // 15), \
                        (W // 15 * 14 , H // 15 * 4), 7)
                    pg.draw.line(app, Rd, ( W // 15 * 14, H // 15 ), \
                        (W // 15 * 11, H // 15 * 4), 7)
                    A3 = 'x'
                if y > H // 3 and y < H // 3 * 2:
                    pg.draw.line(app, Rd, (W // 15 * 11, H // 15 * 6),\
                        (W // 15 * 14, H // 15 * 9), 7)
                    pg.draw.line(app, Rd, (W // 15 * 14,H // 15 * 6),\
                        (W // 15 * 11, H // 15 * 9), 7)
                    B3 = 'x'
                if y < H  and y > H // 3 * 2:
                    pg.draw.line(app, Rd, (W // 15 * 11, H // 15 * 11),\
                        (W // 15 * 14, H // 15 * 14), 7)
                    pg.draw.line(app, Rd, (W // 15 * 14,H // 15 * 11),\
                        (W // 15 * 11, H // 15 * 14), 7)
                    C3 = 'x'
            count_roll = 2
            time_roll += 1
        #ход для нолика
        if count_roll == 2:
            if x < W // 3 and x > 0:
                if y > 0 and y < H // 3:
                    pg.draw.circle(app, Blu, (W // 15 * 2.5, H // 15 * 2.5), W // 15 * 2, 4)
                    A1 = 'o'
                if y > H // 3 and y < H // 3 * 2:
                    pg.draw.circle(app, Blu, (W // 15 * 2.5, H // 15 * 7.5), W // 15 * 2, 4)
                    B1 = 'o' 
                if y < H  and y > H // 3 * 2:
                    pg.draw.circle(app, Blu, (W // 15 * 2.5, H // 15 * 12.5), W // 15 * 2, 4)
                    C1 = 'o'
            if x > W // 3 and x < W // 3 * 2:
                if y > 0 and y < H // 3:
                    pg.draw.circle(app, Blu, (W // 15 * 7.5, H // 15 * 2.5), W // 15 * 2, 4)
                    A1 = 'o' 
                if y > H // 3 and y < H // 3 * 2:
                    pg.draw.circle(app, Blu, (W // 15 * 7.5, H // 15 * 7.5), W // 15 * 2, 4)
                    B1 = 'o'
                if y < H  and y > H // 3 * 2:
                    pg.draw.circle(app, Blu, (W // 15 * 7.5, H // 15 * 12.5), W // 15 * 2, 4)
                    C1 = 'o'      
            if x < W  and x > W // 3 * 2:
                if y > 0 and y < H // 3:
                    pg.draw.circle(app, Blu, (W // 15 * 12.5, H // 15 * 2.5), W // 15 * 2, 4)
                    A1 = 'o'
                if y > H // 3 and y < H // 3 * 2:
                    pg.draw.circle(app, Blu, (W // 15 * 12.5, H // 15 * 7.5), W // 15 * 2, 4)
                    B1 = 'o'
                if y < H  and y > H // 3 * 2:
                    pg.draw.circle(app, Blu, (W // 15 * 12.5, H // 15 * 12.5), W // 15 * 2, 4)
                    C1 = 'o'
            count_roll = 1
            time_roll += 1  

    '''Линии для отметки победителя'''
    #Для крестиков
    if time_roll > 4:
        if A1 == 'x' and A2 == 'x' and A3 == 'x':
            pg.draw.line(app, Gr, (W // 6, H // 6), (W // 6 * 5, H // 6), 8)
            #Верхняя горизонтальная
        if B1 == 'x' and B2 == 'x' and B3 == 'x':
            pg.draw.line(app, Gr, (W // 6, H // 6 * 3), (W // 6 * 5, H // 6 * 3), 8)
            #Средняя горизонтальная
        if C1 == 'x' and C2 == 'x' and C3 == 'x':
            pg.draw.line(app, Gr, (W // 6, H // 6 * 5), (W // 6 * 5, H // 6 * 5), 8)
            #Нижняя горизонтальная
        if A1 == 'x' and B1 == 'x' and C1 == 'x':
            pg.draw.line(app, Gr, (W // 6, H // 6), (W // 6 , H // 6 * 5), 8)
            #Левая вертикальная
        if A2 == 'x' and B2 == 'x' and C2 == 'x':
            pg.draw.line(app, Gr, (W // 6 * 3, H // 6), (W // 6 * 3 , H // 6 * 5), 8)
            #Средняя Вертикальная
        if A3 == 'x' and B3 == 'x' and C3 == 'x':
            pg.draw.line(app, Gr, (W // 6 * 5, H // 6), (W // 6 * 5, H // 6 * 5), 8)
            #Правая вертикальная
        if A1 == 'x' and B2 == 'x' and C3 == 'x':
            pg.draw.line(app, Gr, (W // 6, H // 6), (W // 6 * 5, H // 6 * 5), 8)
            #диагональ с левого верха вправый низ
        if A3 == 'x' and B2 == 'x' and C1 == 'x':
            pg.draw.line(app, Gr, (W // 6 * 5, H // 6), (W // 6, H // 6 * 5), 8)
            #диагональ с правого верха влевый низ
        #Для кружочков (так же)
        if A1 == 'o' and A2 == 'o' and A3 == 'o':
            pg.draw.line(app, Gr, (W // 6, H // 6), (W // 6 * 5, H // 6), 8)
        if B1 == 'o' and B2 == 'o' and B3 == 'o':
            pg.draw.line(app, Gr, (W // 6, H // 6 * 3), (W // 6 * 5, H // 6 * 3), 8)
        if C1 == 'o' and C2 == 'o' and C3 == 'o':
            pg.draw.line(app, Gr, (W // 6, H // 6 * 5), (W // 6 * 5, H // 6 * 5), 8)
        if A1 == 'o' and B1 == 'o' and C1 == 'o':
            pg.draw.line(app, Gr, (W // 6, H // 6), (W // 6 , H // 6 * 5), 8)
        if A2 == 'o' and B2 == 'o' and C2 == 'o':
            pg.draw.line(app, Gr, (W // 6 * 3, H // 6), (W // 6 * 3 , H // 6 * 5), 8)
        if A3 == 'o' and B3 == 'o' and C3 == 'o':
            pg.draw.line(app, Gr, (W // 6 * 5, H // 6), (W // 6 * 5, H // 6 * 5), 8)
        if A1 == 'o' and B2 == 'o' and C3 == 'o':
            pg.draw.line(app, Gr, (W // 6, H // 6), (W // 6 * 5, H // 6 * 5), 8)
        if A3 == 'o' and B2 == 'o' and C1 == 'o':
            pg.draw.line(app, Gr, (W // 6 * 5, H // 6), (W // 6, H // 6 * 5), 8) 

    pg.display.update()
    clock.tick(FPS)   
