import pygame, time, pickle, json

pygame.init()
import socket

player_id = input('id: ')
sock = socket.socket()
sock.connect(('192.168.43.66', 5555))

# colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# window sizes
display_width = 800
display_height = 600

paddle_width = 40
paddle_height = 100

# Lets pygame know what window to draw things too
gameDisplay = pygame.display.set_mode((display_width, display_height))
# initalize clock for FPS
clock = pygame.time.Clock()

global message


def draw_paddle(x, y, p):
    if p == "1":
        pygame.draw.rect(gameDisplay, RED, [x, y, paddle_width, paddle_height])
    if p == "2":
        pygame.draw.rect(gameDisplay, BLUE, [x, y, paddle_width, paddle_height])


def recieve_data():
    recv_data = sock.recv(1024)
    print(recv_data)
    recv_data = json.loads(recv_data.decode("utf-8"))
    return recv_data


def send_data(data):
    data_arr = json.dumps(data, ensure_ascii=False).encode("utf-8")
    sock.send(data_arr)


def waiting_for_game_started():
    data = recieve_data()
    while not data.get('game', False):
        data = recieve_data()
    send_data({"keys": [0, 1], "id": player_id})


# main game loop
def main():
    waiting_for_game_started()
    game_finished = False
    print('Game started')
    while not game_finished:
        # set FPS
        clock.tick(120)
        data = {}
        try:
            data = recieve_data()
            print('data', data)
        except Exception as eror:
            continue

        # Collect Game information. ex)Paddle position, Score, Ball position
        # draw background
        gameDisplay.fill(WHITE)
        for p_id in data['players_data'].keys():
            draw_paddle(data['players_data'][p_id]["x"], data['players_data'][p_id]["y"], p_id)

        pygame.display.update()

        # wait for key press activity from client
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                game_finished = True

        keys = pygame.key.get_pressed()

        pressed_keys = []
        if keys[pygame.K_w]:
            pressed_keys.append(0)
        elif keys[pygame.K_s]:
            pressed_keys.append(1)

        if keys[pygame.K_d]:
            pressed_keys.append(3)
        elif keys[pygame.K_a]:
            pressed_keys.append(2)
        send_data({"keys": pressed_keys, "id": player_id})


main()
