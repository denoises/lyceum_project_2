import pygame
import sys

animation_set = [pygame.image.load(f"image/low_settings/person/left/left00{i:02d}.png") for i in range(1, 50)]

window = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()
i = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((0, 0, 0))
    window.blit(animation_set[i], (100, 20))
    i += 1
    if i == 49:
        i = 0

    pygame.display.flip()
    clock.tick(60)
