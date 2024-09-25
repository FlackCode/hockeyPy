import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
screenWidth = screen.get_width()
screenHeight = screen.get_height()

screenCenter = pygame.Vector2(screenWidth / 2, screenHeight / 2)
playerSize = pygame.Vector2(20, 160)
accel = 10000

ballPos = pygame.Vector2(screenWidth / 2, screenHeight / 2)
ballRadius = 10
ballVel = 300
ballAccel = 0

player1Size = playerSize
player1Pos = pygame.Vector2(10, screenHeight / 2 - (playerSize.y / 2)) 
player1Vel = 0
player1Accel = 0

player2Size = playerSize
player2Pos = pygame.Vector2(screenWidth - playerSize.x - 10, screenHeight / 2 - (playerSize.y/2))
player2Vel = 0
player2Accel = 0



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

def BallIsColliding(playerPosition, playerSize, ballRadius, ballPosition):
    collisionX = max(playerPosition.x, min(ballPosition.x, playerPosition.x + playerSize.x))
    collisionY = max(playerPosition.y, min(ballPosition.y, playerPosition.y + playerSize.y))

    distanceX = ballPosition.x - collisionX
    distanceY = ballPosition.y - collisionY

    return (distanceX ** 2 + distanceY ** 2) <= (ballRadius ** 2)


while running:
    dt = clock.tick(144) * 0.001

    ballPos.x += ballVel * dt

    screen.fill("black")
    pygame.draw.circle(screen, "white", ballPos, ballRadius)
    pygame.draw.rect(screen, "white", pygame.Rect((player1Pos), (player1Size)))
    pygame.draw.rect(screen, "white", pygame.Rect((player2Pos), (player2Size)))

    pygame.draw.circle(screen, "white", screenCenter, 150, 1)
    pygame.draw.circle(screen, "black", screenCenter, 125, 1)
    pygame.draw.line(screen, "white", (screenWidth / 2, 0), (screenWidth / 2, screenHeight), 1)
    

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

    if BallIsColliding(player1Pos, playerSize, ballRadius, ballPos):
        ballPos.x = player1Pos.x + playerSize.x + ballRadius
        ballVel = -ballVel
    if BallIsColliding(player2Pos, playerSize, ballRadius, ballPos):
        ballPos.x = player2Pos.x - ballRadius
        ballVel = -ballVel

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()