import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
screenWidth = screen.get_width()
screenHeight = screen.get_height()

ballInitPos = pygame.Vector2(screenWidth / 2, screenHeight / 2)
ballPos = pygame.Vector2(screenWidth / 2, screenHeight / 2)
ballRadius = 10

player1Size = pygame.Vector2(60, 40)
player1Pos = pygame.Vector2(screenWidth - player1Size.x, screenHeight / 2 - player1Size.y)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("black")
    pygame.draw.circle(screen, "white", ballPos, ballRadius)
    pygame.draw.rect(screen, "white", pygame.Rect((player1Pos), (player1Size)))


    pygame.display.update()

    dt = clock.tick(60) * 0.001

pygame.quit()