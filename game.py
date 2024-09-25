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

playerSize = pygame.Vector2(20, 160)

player1Size = playerSize
player1Pos = pygame.Vector2(10, screenHeight / 2 - (playerSize.y / 2)) 
player1Vel = 0
player1Accel = 0

player2Size = playerSize
player2Pos = pygame.Vector2(screenWidth - playerSize.x - 10, screenHeight / 2 - (playerSize.y/2))
player2Vel = 0
player2Accel = 0

accel = 10000

def simulatePlayer(position, velocity, acceleration, deltaTime):
        damping = 10
        acceleration -= velocity * damping
        position.y += velocity * deltaTime + acceleration * (deltaTime * deltaTime / 2)
        velocity += acceleration * deltaTime

        if position.y + playerSize.y > screenHeight:
            position.y = screenHeight - playerSize.y
            velocity = 0
        elif position.y < 0:
            position.y = 0
            velocity = 0

        return velocity 


while running:
    dt = clock.tick(144) * 0.001

    screen.fill("black")
    pygame.draw.circle(screen, "white", ballPos, ballRadius)
    pygame.draw.rect(screen, "white", pygame.Rect((player1Pos), (player1Size)))
    pygame.draw.rect(screen, "white", pygame.Rect((player2Pos), (player2Size)))

    keys = pygame.key.get_pressed()

    player1Accel = 0
    if keys[pygame.K_w]:
        player1Accel -= accel
    if keys[pygame.K_s]:
        player1Accel += accel
    
    player2Accel = 0
    if keys[pygame.K_UP]:
        player2Accel -= accel
    if keys[pygame.K_DOWN]:
        player2Accel += accel
    
    
    
    player1Vel = simulatePlayer(player1Pos, player1Vel, player1Accel, dt)
    player2Vel = simulatePlayer(player2Pos, player2Vel, player2Accel, dt)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()