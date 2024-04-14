import pygame
pygame.font.init()

surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Menu")
surface.fill((64, 230, 108))


start = pygame.image.load("resources/button.png").convert_alpha()
start = pygame.transform.scale(start, (250, 100))
exit = pygame.image.load("resources/button.png").convert_alpha()
exit = pygame.transform.scale(start, (250, 100))
speed = pygame.image.load("resources/button.png").convert_alpha()
speed = pygame.transform.scale(start, (250, 100))
main_font = pygame.font.SysFont("arial", 50)


class Button():
    def __init__(self, x, y, image, text):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.text = text
        self.text = main_font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (x, y)

    def draw(self):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        surface.blit(self.text, (self.text_rect.x, self.text_rect.y))
        

start_btn = Button(400, 150, start, "START")
exit_btn = Button(400, 300, exit, "EXIT")
speed_btn = Button(400, 450, speed, "SPEED")
    
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
