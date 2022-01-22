import pygame, time, pickle
import pyganim
import socket
import caar

pygame.init()


# player_id = input('id: ')
# sock = socket.socket()
# sock.connect(('172.20.10.5', 5555))
# data = sock.recv(1024)
# sock.close()

# data = pickle.loads(data)

# Lets pygame know what window to draw things too
gameDisplay = pygame.display.set_mode((600, 800))
# initalize clock for FPS
clock = pygame.time.Clock()

global message


# main game loop
def main():
    car = caar.Car('red_car.png', (10, 20))
    car_group = pygame.sprite.RenderPlain(car)

    game_finished = False

    while not game_finished:
        # set FPS
        clock.tick(120)
        # Collect Game information. ex)Paddle position, Score, Ball position
        # draw background
        gameDisplay.fill((0, 0, 0))
        car_group.update()
        car_group.draw(gameDisplay)

        pygame.display.update()

        # wait for key press activity from client
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                game_finished = True

        keys = pygame.key.get_pressed()

        # if keys[pygame.K_w]:
        #     car.position[1] -= 3
        # elif keys[pygame.K_s]:
        #     car.position[0] += 3
        #
        # if keys[pygame.K_d]:
        #     car.position[1] += 3
        # elif keys[pygame.K_a]:
        #     car.position[0] -= 3


while True:
    main()
