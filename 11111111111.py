import pygame
import sys

animation_set = [pygame.image.load('image/low_settings/fire/fire0018.png'),
                 pygame.image.load('image/low_settings/fire/fire0019.png'),
                 pygame.image.load('image/low_settings/fire/fire0020.png'),
                 pygame.image.load('image/low_settings/fire/fire0021.png'),
                 pygame.image.load('image/low_settings/fire/fire0022.png'),
                 pygame.image.load('image/low_settings/fire/fire0023.png'),
                 pygame.image.load('image/low_settings/fire/fire0024.png'),
                 pygame.image.load('image/low_settings/fire/fire0025.png'),
                 pygame.image.load('image/low_settings/fire/fire0026.png'),
                 pygame.image.load('image/low_settings/fire/fire0027.png'),
                 pygame.image.load('image/low_settings/fire/fire0028.png'),
                 pygame.image.load('image/low_settings/fire/fire0029.png'),
                 pygame.image.load('image/low_settings/fire/fire0030.png'),
                 pygame.image.load('image/low_settings/fire/fire0031.png'),
                 pygame.image.load('image/low_settings/fire/fire0032.png'),
                 pygame.image.load('image/low_settings/fire/fire0033.png'),
                 pygame.image.load('image/low_settings/fire/fire0034.png'),
                 pygame.image.load('image/low_settings/fire/fire0035.png'),
                 pygame.image.load('image/low_settings/fire/fire0036.png'),
                 pygame.image.load('image/low_settings/fire/fire0037.png'),
                 pygame.image.load('image/low_settings/fire/fire0038.png'),
                 pygame.image.load('image/low_settings/fire/fire0039.png'),
                 pygame.image.load('image/low_settings/fire/fire0040.png'),
                 pygame.image.load('image/low_settings/fire/fire0041.png'),
                 pygame.image.load('image/low_settings/fire/fire0042.png'),
                 pygame.image.load('image/low_settings/fire/fire0043.png'),
                 pygame.image.load('image/low_settings/fire/fire0044.png'),
                 pygame.image.load('image/low_settings/fire/fire0045.png'),
                 pygame.image.load('image/low_settings/fire/fire0046.png'),
                 pygame.image.load('image/low_settings/fire/fire0047.png'),
                 pygame.image.load('image/low_settings/fire/fire0048.png'),
                 pygame.image.load('image/low_settings/fire/fire0049.png'),
                 pygame.image.load('image/low_settings/fire/fire0050.png'),
                 pygame.image.load('image/low_settings/fire/fire0061.png'),
                 pygame.image.load('image/low_settings/fire/fire0062.png'),
                 pygame.image.load('image/low_settings/fire/fire0063.png'),
                 pygame.image.load('image/low_settings/fire/fire0064.png'),
                 pygame.image.load('image/low_settings/fire/fire0065.png'),
                 pygame.image.load('image/low_settings/fire/fire0066.png'),
                 pygame.image.load('image/low_settings/fire/fire0067.png'),
                 pygame.image.load('image/low_settings/fire/fire0068.png'),
                 pygame.image.load('image/low_settings/fire/fire0069.png'),
                 pygame.image.load('image/low_settings/fire/fire0070.png')

                 ]
# animation_set = [pygame.image.load(f"image/low_settings/person/left/left00{i:02d}.png") for i in range(1, 50)]


window = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()
i = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((255, 255, 255))
    window.blit(animation_set[i], (100, 20))
    i += 1
    if i == len(animation_set):
        i = 0

    pygame.display.flip()
    clock.tick(60)
