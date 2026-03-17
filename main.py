import pygame

pygame.init()
window = pygame.display.set_mode(size=(800, 640))
print('setup end')

print('loop start')
while True:
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # close window
            quit()  # end pygame
