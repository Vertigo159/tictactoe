import pygame as pg
from game.colors import Colorr


pg.init()
game_screen = pg.display.set_mode(
    (400, 400)
)
pg.display.set_caption("tic-tac-toe")
size_block = 113
marg = 15
width = heigth = size_block*3 + marg*4
mas = [[0]*3 for i in range(3)]
set = 0

work = True
while work:
    keys = pg.key.get_pressed()
    work = not keys[pg.K_ESCAPE]
    events = pg.event.get()
    for ev in events:
        print(ev)
        if ev.type == pg.WINDOWCLOSE:
            work = False
        elif ev.type == pg.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pg.mouse.get_pos()
            col = x_mouse // (size_block+marg)
            row = y_mouse // (size_block + marg)
            if mas[row][col] == 0:
                if set%2==0:
                    mas[row][col] = "x"
                else:
                    mas[row][col] = "O"
                set+=1


    for row in range(3):
        for col in range(3):
            if mas[row][col]=="x":
                color = Colorr.WHITE
            elif mas[row][col]=="O":
                color = Colorr.SILVER
            else:
                color = Colorr.GREEN
            x = col * size_block + (col+1) * marg
            y = row * size_block + (row + 1) * marg
            pg.draw.rect(game_screen, color, (x,y,size_block,size_block))
            if color == Colorr.WHITE:
                pg.draw.line(game_screen, Colorr.BLACK, (x,y), (x + size_block,y + size_block), 7)
                pg.draw.line(game_screen, Colorr.BLACK, (x + size_block, y), (x, y + size_block), 7)
            if color == Colorr.SILVER:
                pg.draw.circle(game_screen, Colorr.BLACK,(x + size_block // 2, y + size_block // 2), 55, 3)


    pg.display.update()