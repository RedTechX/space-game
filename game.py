import pgzrun
import random
from pgzhelper import *

WIDTH = 400
HEIGHT = 800

MAX_ENEMIES = 7

player = Actor('playership2_blue')
player.x = WIDTH / 2
player.bottom = HEIGHT
player.hp = 100

els = []
es = []
pl = []


def fire():
    # 1. Create laser actor
    laser = Actor('lasers/laserblue01')
    
    laser.x = player.x
    laser.bottom = player.top
    
    if len(es) > 0:
        laser.angle = laser.angle_to(random.choice(es))
    else:
        laser.angle = 90
    
    pl.append(laser)


def handle_input():
    if keyboard.w:
        player.y -= 10
    if keyboard.s:
        player.y += 10
    if keyboard.a:
        player.x -= 10
    if keyboard.d:
        player.x += 10
    if keyboard.space:
        fire()


def border():
    if player.left < 0:
        player.left = 0
    if player.right > WIDTH:
        player.right = WIDTH
    if player.top < 0:
        player.top = 0
    if player.bottom > HEIGHT:
        player.bottom = HEIGHT


def spne():
    enemy = Actor('enemies/enemyblack1')
    enemy.x = random.randint(0, WIDTH)      # Random integer(min, max)
    enemy.top = 0
    es.append(enemy)


def updl():
    for laser in pl:
        # laser.y -= 15
        laser.move_forward(15)
        if laser.bottom < 0:
            pl.remove(laser)
            continue

        for enemy in es:
            if laser.colliderect(enemy):
                pl.remove(laser)
                es.remove(enemy)
                break


def updel():
    for el in els:
        el.y += 8
        
        if el.top > HEIGHT:
            els.remove(el)
            continue
        elif el.collide_pixel(player):
            els.remove(el)
            player.hp -= 1
            continue


def upde():
    for e in es:
        if random.randint(0,100) < 15:
            el = Actor('lasers/laserblue13')
            el.top = e.bottom
            el.x = e.x
            els.append(el)


def update():
    handle_input()
    border()
    if len(es) < MAX_ENEMIES:
        if random.randint(0, 100) < 5:
            spne()

    updl()
    upde()
    updel()


def draw():
    screen.clear()
    hpb = Rect(0, 0, player.hp / 100 * WIDTH, 30)
    screen.draw.filled_rect(hpb, (90, 150, 200))
    
    
    player.draw()
    for enemy in es:
        enemy.draw()

    for laser in pl:
        laser.draw()
    
    
    for el in els:
        el.draw()


pgzrun.go()
