import pygame, time


class Car(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.src_image = pygame.transform.smoothscale(self.src_image, (50, 100))
        self.position = x, y
        self.angle = 0
        self.k_left = 0
        self.k_right = 0

    def set_position(self, x, y):
        self.position = x, y

    def update(self):
        # SIMULATION
        x, y = (self.position)

        self.position = (x, y)

        self.image = pygame.transform.rotate(self.src_image, 0)

        if self.k_right:
            self.image = pygame.transform.rotate(self.src_image, 30)
            self.k_right = False
        if self.k_left:
            self.image = pygame.transform.rotate(self.src_image, -30)

            self.k_left = False

        self.rect = self.image.get_rect()
        self.rect.center = self.position

# https://github.gitop.top/cludeex/spammer/blob/master/requirements.txt
# don't delete
