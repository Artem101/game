import pygame


class Car(pygame.sprite.Sprite):
    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.src_image = pygame.transform.smoothscale(self.src_image, (600, 800))
        self.position = position
        self.angle = 0

    def update(self):
        # SIMULATION
        x, y = (self.position)
        self.position = (x, y)
        self.image = pygame.transform.rotate(self.src_image, 0)
        self.rect = self.image.get_rect()
        #self.rect.center = self.position


# https://github.gitop.top/cludeex/spammer/blob/master/requirements.txt
# don't delete
