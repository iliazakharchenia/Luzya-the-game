import pygame
import house
import luzya
import settings

# game init and setting
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Luzya - The Game")

# game objects
bg = pygame.image.load('res/bg/house.png')
GREY = (210,210,210)
clock = pygame.time.Clock()
untouch_sprites = pygame.sprite.Group()
untouch_sprites.add(house.House())
#luzya_sprite = pygame.sprite.GroupSingle()
#luzya_sprite.add(luzya.Luzya())
luzya = luzya.Luzya()

# game loop
def main():
    game_running = True
    screen.fill(GREY)
    while game_running:

        # events handling start
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        ### events handling end

        untouch_sprites.update()
        #luzya_sprite.update()
        luzya.update()
        #untouch_sprites.draw(screen)
        for spr in untouch_sprites.sprites():
            screen.blit(spr.image, (spr.rect.centerx-luzya.x, spr.rect.centery-luzya.y-50))
        #luzya_sprite.draw(screen)
        #screen.blit(luzya.image, (luzya.x, luzya.y))
        screen.blit(luzya.image, (350, 250))
        pygame.display.update()
        screen.fill(GREY)
        clock.tick(30)

    pygame.quit()


# start game
if __name__ == '__main__': main()