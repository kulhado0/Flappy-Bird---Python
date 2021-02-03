import pygame
import random

clock = pygame.time.Clock()

class enemy:
    def __init__(self):
        self.pipeGreen = pygame.image.load(r'C:\Users\joaop\PycharmProjects\GamePython\Images\pipe-green.png').convert()
        self.pipeGreenRotated = pygame.transform.rotate(self.pipeGreen, 180)
        self.x = random.randint(150, 350)
        self.y = random.randint(190, 350)
        self.pipex = 0
        self.distancia = -(random.randint(200, 380))

    def add(self): #200
        self.y = random.randint(310, 390)
        self.distancia = -(random.randint(100, 220)) #-(random.randint(250, 400))#(self.y + 100))) #-(random.randint(200, 380))
        print(self.distancia)

    def start(self):
        if (self.pipex <= 1):
            self.add()
        self.show()

    def show(self):
        win.blit(self.pipeGreen, (self.pipex, self.y))
        win.blit(self.pipeGreenRotated, (self.pipex, self.distancia))

class background:
    def __init__(self):
        self.base = pygame.image.load(r'C:\Users\joaop\PycharmProjects\GamePython\Images\base.png').convert()
        self.background = pygame.image.load(r'C:\Users\joaop\PycharmProjects\GamePython\Images\background-night.png').convert()
        self.basex = 0
        self.basey = 0
        self.backgroundx = 0
        self.backgroundy = 0
        self.x = 0

class player:
    def __init__(self):
        self.animation = [pygame.image.load(r'C:\Users\joaop\PycharmProjects\GamePython\Images\bluebird-1.png'), pygame.image.load(r'C:\Users\joaop\PycharmProjects\GamePython\Images\bluebird-2.png'), pygame.image.load(r'C:\Users\joaop\PycharmProjects\GamePython\Images\bluebird-3.png')]
        self.x = 50
        self.y = self.x
        self.width = 50
        self.height = 50
        self.counter = 0
        self.angle = 40

    def move(self):
        self.counter += 1
        self.y += 1
        self.angle += 1


#Função para renderizar o jogo
def redrawWindow(player, bg, en):
    ''' Background View'''
    bg.backgroundx = bg.x % bg.background.get_rect().width
    win.blit(bg.background, (bg.backgroundx - bg.background.get_rect().width, 0))
    bg.basex = bg.x % bg.background.get_rect().width
    win.blit(bg.base, (bg.basex - bg.base.get_rect().width, 405))
    if bg.x < 280:
        win.blit(bg.background, (bg.backgroundx, 0))
        win.blit(bg.base, (bg.basex, 405))
    bg.x -= 1

    ''' Bird View'''
    if (player.angle > 40):
        player.angle = 40
    if(player.y > 385):
        player.y = 385
        player.angle = 0
    bird_rotated, bird_rotated_rect = rotate(player.animation[player.counter%3], player.angle)
    win.blit(bird_rotated, (player.x, player.y))

    ''' Enemy View '''
    en.pipex = bg.x % bg.background.get_rect().width
    en.start()

    pygame.display.flip()
    pygame.display.update()


#Função para controlar a saída do jogo
def quit(event):
    if event.type == pygame.QUIT:
        return False
    else:
        return True


#Função para controlar a movimentação do game
def movimentation(player, background, en):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        for x in range(0,70):
            player.y -= 0.5
            player.angle = -40
            background.x += 0.8
            redrawWindow(player, background, en)


#Função para rotacionar o player
def rotate(image, angle):
    rotated_surface = pygame.transform.rotozoom(image,-angle,1)
    rotated_rect = rotated_surface.get_rect(center=(10,10))
    return rotated_surface, rotated_rect


#Função para detectar a colisão de objetos
def colisao(player, enemy):
                    # Cano em baixo                                     #Cano cima
    #print( player.y, " | ", -(enemy.distancia-43))# '''menor mais em cima, maior mais em baixo '''
    #if ((enemy.pipex <= player.x+30 and (enemy.y <= player.y +30 or -(enemy.distancia-43) <= player.y) and enemy.pipex >= 10)) :
    if (enemy.pipex <= player.x + 30 and (enemy.y <= player.y + 30 and enemy.pipex >= 10)):
        return False
    else:
        return True


#Controla toda execução do jogo
def game():
    current = True
    bird = player()
    bg = background()
    en = enemy()
    clock.tick(27)
    bg.x = 0
    while current:
        pygame.time.delay(6) #6
        bird.move()

        for event in pygame.event.get():        #Controla os eventos
            movimentation(bird, bg, en)
            current = quit(event)               #Controla a saída do jogo

        current = colisao(bird, en)
        redrawWindow(bird, bg, en)
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((288, 512))
    pygame.display.set_caption("Flappy Bird")
    game()