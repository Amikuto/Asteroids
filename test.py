import pygame as pg
import sys

pg.init()
sc = pg.display.set_mode((400, 300))

pg.mixer.init()
# pg.mixer.music.load(b'MenuThemeMusic.mp3')
# pg.mixer.music.play()


sound1 = pg.mixer.Sound('TIEfire.mp3')
# sound2 = pg.mixer.Sound('one.ogg')

while 1:
    # for i in pg.event.get():
    #     if i.type == pg.QUIT:
    #         sys.exit()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            if event.key == pg.K_SPACE:
                sound1.play()
                # player.shoot()

        # elif i.type == pg.KEYUP:
        #     if i.key == pg.K_1:
        #         pg.mixer.music.pause()
                # pygame.mixer.music.stop()
            # elif i.key == pg.K_2:
            #     pg.mixer.music.unpause()
            #     # pygame.mixer.music.play()
            #     pg.mixer.music.set_volume(0.5)
            # elif i.key == pg.K_3:
            #     pg.mixer.music.unpause()
            #     # pygame.mixer.music.play()
            #     pg.mixer.music.set_volume(1)

        # elif i.type == pg.MOUSEBUTTONUP:
            # if i.button == 1:
                # sound1.play()
            # elif i.button == 3:
            #     sound2.play()

    # pg.time.delay(20)
