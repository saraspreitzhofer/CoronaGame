import pygame
import os  # to define path to the images

# https://www.youtube.com/watch?v=jO6qQDNa2UY

WIDTH, HEIGHT = 900, 500
WHITE = (255, 255, 255)
FPS = 60  # frames per second
RUNNER_WIDTH, RUNNER_HEIGHT = 120, 120
VIRUS_WIDTH, VIRUS_HEIGHT = 80, 80
VELOCITY_VIRUS = 4

WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # make new window of defined width & height
pygame.display.set_caption("Corona Game")  # window title

RUNNER_IMAGE = pygame.image.load(os.path.join('assets', "runner.png"))
RUNNER = pygame.transform.scale(RUNNER_IMAGE, (RUNNER_WIDTH, RUNNER_HEIGHT))  # resize image

VIRUS_IMAGE = pygame.image.load(os.path.join('assets', "virus.png"))
VIRUS = pygame.transform.scale(VIRUS_IMAGE, (VIRUS_WIDTH, VIRUS_HEIGHT))  # resize image


def draw_window(runner, virus):
    WIN.fill(WHITE)  # RGB color for the window background, defined as constant
    # coordinate system: (0,0) is top left
    WIN.blit(RUNNER, (runner.x, runner.y))  # draw surface (pictures, text, ...) on the screen
    WIN.blit(VIRUS, (virus.x, virus.y))
    pygame.display.update()  # update changes


def main():  # code that handles main game loop in pygame
    runner = pygame.Rect(10, 370, RUNNER_WIDTH, RUNNER_HEIGHT)
    virus = pygame.Rect(810, 410, VIRUS_WIDTH, VIRUS_HEIGHT)
    clock = pygame.time.Clock()
    run = True

    while run:  # game loop: open & close the window
        clock.tick(FPS)  # controls speed of the while loop
        for event in pygame.event.get():  # loop through list of all different events
            if event.type == pygame.QUIT:
                run = False  # end while loop if user quits game (press x)
            # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            #    jump(runner)
            # https://www.youtube.com/watch?v=G8pYfkIajE8
        virus.x -= VELOCITY_VIRUS  # move image VELOCITY_VIRUS pixel to the left in each frame
        draw_window(runner, virus)
    pygame.quit()  # quits pygame & closes the window


if __name__ == "__main__":
    main()  # only run the game if we run this file directly (not if it was imported from somewhere else)

