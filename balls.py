import pygame 

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

ELASTICITY = -.8
GRAVITY = 0.08


class Ball:
    def __init__(self, color1, color2, starting_size, starting_x, starting_y, starting_vx, starting_vy):
        self.current_color = color1

        self.color1 = color1
        self.color2 = color2

        self.num_bounces = 0

        self.size = starting_size 

        self.x = starting_x
        self.y = starting_y

        self.vx = starting_vx
        self.vy = starting_vy

balls = [
    Ball("green", "red", 50, 300, 300, 4, 7),
    Ball("green", "blue", 50, 300, 300, 1, 2),
    Ball("green", "purple", 50, 300, 300, 10, 6),
    Ball("green", "orange", 50, 300, 300, 10, -6),
    Ball("green", "pink", 50, 300, 300, 1, 6),
    Ball("green", "black", 50, 300, 300, -4, 0),
    Ball("green", "white", 50, 300, 300, -10, 6),
    Ball("green", "cyan", 50, 300, 300, 0, 12)
]

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    #TODO: update the position to move the ball if needed
    #TODO: update the speed to bounce the ball if needed
    # update position based on speed
    # ball_y = ball_y + ball_vy
    # ball_x = ball_x + ball_vx

    for ball in balls:
        ball.x = ball.x + ball.vx
        ball.y = ball.y + ball.vy

    # apply gravity
    for ball in balls:
        ball.vy = ball.vy + GRAVITY
        
    # handle collisions
    for ball in balls: 
        if ball.y + ball.vy >= SCREEN_HEIGHT - ball.size or ball.y + ball.vy <= ball.size: 
            ball.vy = ball.vy * ELASTICITY
            ball.current_color = ball.color2
            ball.num_bounces = ball.num_bounces + 1
        if ball.x + ball.vx <= ball.size or (ball.x + ball.vx) + ball.size >= SCREEN_WIDTH:
            ball.vx = ball.vx * ELASTICITY
            ball.current_color = ball.color2 
            ball.num_bounces = ball.num_bounces + 1

        if ball.num_bounces % 2 == 0:
            ball.current_color = ball.color1
        else: 
            ball.current_color = ball.color2
    
    for ball in balls:
        print(f'{ball.num_bounces}\t', end='')
    print('')

    screen.fill("white")

    #TODO: Draw the ball at its current position
    for ball in balls:
        pygame.draw.circle(screen, ball.current_color, (ball.x, ball.y), ball.size)


    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)








# ball.bounce = ball.x + ball.vx <= ball.size or (ball.x + ball.vx) + ball.size >= SCREEN_WIDTH or \
               # ball.y + ball.vy >= SCREEN_HEIGHT - ball.size or ball.y + ball.vy <= ball.size