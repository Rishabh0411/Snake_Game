import pygame

surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Menu")
surface.fill((64, 230, 108))


start = pygame.image.load("resources/start_btn.jpeg").convert_alpha()
exit = pygame.image.load("resources/download.png").convert_alpha()
speed = pygame.image.load("resources/maxresdefault.jpg").convert_alpha()

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        surface.blit(self.image, (self.rect.x, self.rect.y))

start_btn = Button(10, 35, start)
exit_btn = Button(250, 50, exit)
speed_btn = Button(300, 350, speed)
    
running = True

while running:
    start_btn.draw()
    exit_btn.draw()
    speed_btn.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()    
pygame.quit()    
