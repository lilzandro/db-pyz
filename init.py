import pygame

pygame.init()


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Juego de Peleas")

#load resources
bg = pygame.image.load("assets/fondo_pyz.png")
health_body = pygame.image.load("assets/health_bars.png")
txt = pygame.font.Font('freesansbold.ttf', 32)

def health_bars(x1,x2):

    pygame.draw.rect(screen,green,(65,30,310,25))
    pygame.draw.rect(screen,red,(430,30,310,25))

    pygame.draw.rect(screen,red,(65,30,x1-310,25))
    pygame.draw.rect(screen,green,(430,30,x2,25))

def draw_bg():
    screen.blit(bg, (0, 0))


tempo = ["60"]
tempoCount = 60

green =(0,255,0)
red = (255,0,0)
black=(0,0,0)
fps = 60
timer = pygame.time.Clock()
x1=310
x2=310
run = True
sec = 0

while run:

    timer.tick(fps)

    sec += timer.tick(fps)
    tempo_bend = txt.render(tempo[0], True, black)

    # Maneja eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Eventos del teclado
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:

                x2 -= 10

            if event.key == pygame.K_o and x1 < 620:

                x1 += 10

    if sec > 1000:

        sec -= 1000
        del tempo[0]
        tempoCount -= 1
        tempo.append(str(tempoCount))

    health_bars(x1, x2)
    screen.blit(health_body, (65, 30))
    screen.blit(health_body, (430, 30))
    screen.blit(tempo_bend, (380, 50))

    pygame.display.flip()
