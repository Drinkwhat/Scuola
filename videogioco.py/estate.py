import pygame
from random import randint

pygame.init()

bg = pygame.image.load('immagini/sfondo.png')
br = pygame.image.load('immagini/uccello.png')
bs = pygame.image.load('immagini/base.png')
go = pygame.image.load('immagineìi/gameover.png')
tubo_giu = pygame.image.load('immagini/tubo.png')
tubo_su = pygame.trasform.flip(tubo_giu, False, True)

schermo = pygame.display.set_mode((288, 512))

FPS = 50
vel_avanz = 3
font = pygame.font.SysFont('Comic Sans MS', 50, bold=True)

class tubi_classe:
    def __init__(self):
        self.x = 300
        self.y = randint(-75, 150)
    def avanza_e_disegna(self):
        self.x -= vel_avanz
        schermo.blit (tubo_giu, (self.x, self.y+210))
        schermo.blit (tubo_su, (self.x, self.y-210))

    def collisione(self, br, brx, bry):
        tolleranza = 5 
        br_l_dx = brx + br.get_width() - tolleranza
        br_l_sx = brx + tolleranza
        tubi_l_dx = self.x + tubo_giu.get_width()
        tubi_l_sx = self.x
        br_l_su = bry + tolleranza
        br_l_giu = bry + br.get_height() - tolleranza
        tubi_l_su = self.y + 110
        tubi_l_giu = self.y + 210
        if br_l_dx > tubi_l_sx and br_l_sx < tubi_l_dx:
            if br_l_su < tubi_l_su or br_l_giu > tubi_l_giu:
                hai_perso()

    def fra_i_tubi(self, br, brx):
        tolleranza = 5 
        br_l_dx = brx + br.get_width() - tolleranza
        br_l_sx = brx + tolleranza
        tubi_l_dx = self.x + tubo_giu.get_width()
        tubi_l_sx = self.x
        if br_l_dx > tubi_l_sx and br_l_sx < tubi_l_dx:
            return True

def disegna_oggetti():
    schermo.blint(bg, (0, 0))
    for t in tubi:
        t.avanza_e_disegna()
    schermo.blit(br, (brx, bry) )
    schermo.blit(bs, (bsx, 400) )
    punti_render = font.render(str(punti), 1, (255, 255, 255))
    schermo.blit(punti_render, (144, 0))


def inizializza():
    global brx , bry , br_vely
    global bsx
    global tubi
    global fra_i_tubi
    global punti
    brx, bry = 60, 150
    br_vely = 0
    bsx = 0
    punti = 0
    tubi = []
    tubi.append(tubi_classe ())
    fra_i_tubi = False


def hai_perso():
    disegna_oggetti()
    schermo.blit(go, (50, 180))
    aggiorna()
    restart = False
    while not restart:
        for event in pygame.event.get():
            if  event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                inizializza()
                Restart = True
            if event.type == pygame.QUIT:
                pygame.quit()



inizializza ()

while True:
    bsx -= vel_avanz
    if bsx < -45:
        bsx = 0
    br_vely += 1
    bry += br_vely
    for event in pygame.event.get():

        if ( event.type == pygame.KEYDOWN and event.key == pygame.K_UP ):
            br_vely = -10
        if event.type == pygame.QUIT:
            pygame.quit()
    if tubi [-1].x < 150:
        tubi.append(tubi_classe())
        for t in tubi:
            t.collisione(br, brx, bry)
    if not fra_i_tubi:
        for t in tubi:
            if t.fra_i_tubi(br, brx):
                fra_i_tubi = True
                break

    if fra_i_tubi:
        for t in tubi:
            if t.fra_i_tubi(br, brx):
                fra_i_tubi = True
                break
        fra_i_tubi = False
    if not fra_i_tubi:
        punti += 1
    

    if bry > 380:
        hai_perso()

    disegna_oggetti()
    aggiorna()
