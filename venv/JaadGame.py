import pygame

pygame.init()
window = pygame.display.set_mode((500, 480))
pygame.display.set_caption("Game of Jaad")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
screenwidth = 500
class Player:
    def __init__(self, x, y , width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.right = False
        self.left = False
        self.walkCount = 0

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            window.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            window.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            window.blit(char, (self.x, self.y))


clock = pygame.time.Clock()

def redrawGameWindow():

    window.blit(bg, (0,0))  # putting in the background
    jaad.draw(window)
    pygame.display.update()


# MAIN LOOP #

jaad = Player(300,410, 64, 64)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and jaad.x > jaad.vel:
        jaad.x -= jaad.vel
        jaad.left = True
        jaad.right = False
    elif keys[pygame.K_RIGHT] and jaad.x < 500 + jaad.width + (4 * jaad.vel):
        jaad.x += jaad.vel
        jaad.right = True
        jaad.left = False
    else:
        jaad.right = False
        jaad.left = False
        jaad.walkCount = 0

    if not jaad.isJump:
        if keys[pygame.K_SPACE]:
            jaad.isJump = True
            jaad.right = False
            jaad.left = False
            jaad.walkCount = 0
    else:
        if jaad.jumpCount >= -10:
            neg = 1
            if jaad.jumpCount < 0:
                neg = -1
            jaad.y -= (jaad.jumpCount ** 2) * 0.5 * neg
            jaad.jumpCount -= 1
        else:
            jaad.isJump = False
            jaad.jumpCount = 10

    redrawGameWindow()
pygame.quit()
