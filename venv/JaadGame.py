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

x = 50
y = 400
width = 64
height = 64
vel = 5
run = True
screenWidth = 480
left = False
right = False
walkCount = 0

isJump = False
jumpCount = 10

clock = pygame.time.Clock()

def redrawGameWindow():
    global walkCount

    window.blit(bg, (0,0))  # putting in the background

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        window.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        window.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        window.blit(char, (x,y))

    pygame.display.update()


# MAIN LOOP #
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screenWidth + width + (4 * vel):
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()
pygame.quit()
