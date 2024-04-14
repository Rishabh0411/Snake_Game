import pygame
pygame.font.init()

surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("DIFFICULTY")
surface.fill((64, 230, 108))


start = pygame.image.load("resources/button.png").convert_alpha()
start = pygame.transform.scale(start, (250, 100))
exit = pygame.image.load("resources/button.png").convert_alpha()
exit = pygame.transform.scale(start, (250, 100))
speed = pygame.image.load("resources/button.png").convert_alpha()
speed = pygame.transform.scale(start, (250, 100))
main_font = pygame.font.SysFont("arial", 30)


class Button():
    def __init__(self, x, y, image, text):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.text = text
        self.text = main_font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        surface.blit(self.image, (self.rect.x, self.rect.y))
        surface.blit(self.text, (self.text_rect.x, self.text_rect.y))

        return action
        

start_btn = Button(400, 150, start, "EASY")
speed_btn = Button(400, 300, speed, "STANDARD")
exit_btn = Button(400, 450, exit, "HARDCORE")
    
running = True

while running:
    if start_btn.draw():
        print("EASY")
                
    if exit_btn.draw():
        print("HARDCORE")

    if speed_btn.draw():
        print("STANDARD")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()    
pygame.quit() 