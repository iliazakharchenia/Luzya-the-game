import pygame
import settings

class Luzya(pygame.sprite.Sprite):
    x: int
    y: int
    x_speed: int
    y_acc: int
    y_speed: int
    injump: bool
    right_images: list
    left_images: list
    ground_images: list
    timer: int
    itr: int

    def __init__(self):
        super().__init__()
        self.itr = 0
        self.image = pygame.image.load('res/luzya/luzya-walk-left-1.png')
        self.right_images = list()
        self.left_images = list()
        self.ground_images = list()
        self.left_images.append(pygame.image.load('res/luzya/luzya-walk-left-1.png'))
        self.left_images.append(pygame.image.load('res/luzya/luzya-walk-left-2.png'))
        self.right_images.append(pygame.image.load('res/luzya/luzya-walk-right-1.png'))
        self.right_images.append(pygame.image.load('res/luzya/luzya-walk-right-2.png'))
        self.ground_images.append(pygame.image.load('res/luzya/luzya-ground-left-1.png'))
        self.ground_images.append(pygame.image.load('res/luzya/luzya-ground-left-2.png'))
        self.ground_images.append(pygame.image.load('res/luzya/luzya-ground-left-3.png'))
        self.rect = self.image.get_rect()
        self.gravity = 0
        self.x = settings.luzya_start_x
        self.y = settings.luzya_start_y
        self.x_speed = 0
        self.y_acc = 0
        self.y_speed = 0
        self.injump = False
        self.timer = settings.timeout

    def costume(self):
        if self.x_speed == 0 and self.y_speed == 0 and self.timer == 0:
            if self.itr >= self.ground_images.__len__():
                self.itr = 0
            self.image = self.ground_images[self.itr]
            self.itr += 1
        elif self.x_speed > 0 and self.y_speed == 0 and self.timer == 0:
            if self.itr >= self.right_images.__len__():
                self.itr = 0
            self.image = self.right_images[self.itr]
            self.itr += 1
        elif self.x_speed < 0 and self.y_speed == 0 and self.timer == 0:
            if self.itr >= self.left_images.__len__():
                self.itr = 0
            self.image = self.left_images[self.itr]
            self.itr += 1
        
        if self.injump == True and self.x_speed > 0:
            self.itr = 0
            self.image = self.right_images[self.itr]
        elif self.injump == True and self.x_speed < 0:
            self.itr = 0
            self.image = self.left_images[self.itr]
        elif self.injump == True and self.x_speed == 0:
            self.itr = 0
            self.image = self.right_images[self.itr]

    def inp(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.x_speed = -settings.luzya_hor_speed
        if keys[pygame.K_RIGHT]: self.x_speed = settings.luzya_hor_speed
        if keys[pygame.K_SPACE] and self.injump == False: 
            self.y_speed = settings.luzya_jumpspeed
            self.injump = True

    def update(self):
        self.inp()

        self.costume()

        self.x += self.x_speed
        self.y += self.y_speed

        #
        if self.y < settings.luzya_start_y:
            self.y_speed += settings.GRAVITY
        else: 
            self.y_speed = 0
            self.injump = False
        
        self.rect.bottomleft = (self.x, self.y)
        self.x_speed = 0

        if self.timer>0: 
            self.timer -= 1
        else:  
            self.timer = settings.timeout