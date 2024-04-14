import pygame
from pygame.locals import *
import random
pygame.font.init()
import menu

SIZE = 40
BG_color = (64, 230, 108)
difficulty = 6
fps_controller = pygame.time.Clock()
frame_size_x = 800
frame_size_y = 600
# snake_pos = [SIZE]*length


class Apple:
    def __init__(self, screen):
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.screen = screen
        self.x = SIZE*3
        self.y = SIZE*3

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0, 18)*SIZE
        self.y = random.randint(0, 13)*SIZE


class Snake:
    def __init__(self, screen, length):
        self.length = length
        self.screen = screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = 'down'

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        self.draw()

    def draw(self):
        self.screen.fill(BG_color)
        for i in range(self.length):
            self.screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def bound_out(self, length):
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        if self.x[0] < 0 or self.x[0] > frame_size_x:
            Game.game_over_mess()
        elif self.y[0] < 0 or self.y[0] > frame_size_y:
            Game.game_over_mess()
        else:
            return False
        


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Game")
        self.surface = pygame.display.set_mode((frame_size_x, frame_size_y))
        self.surface.fill((64, 230, 108))
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2,):
        if x2 <= x1 < x2 + SIZE:
            if y2 <= y1 < y2 + SIZE:
                return True

        return False

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()

        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Game Over"

    def display_score(self):
        font = pygame.font.SysFont('arial', 34)
        score = font.render(f"Score: {self.snake.length}", True, (255, 0, 0))
        self.surface.blit(score, (670, 10))

    def game_over_mess(self):
        self.surface.fill(BG_color)
        font = pygame.font.SysFont('arial', 34)
        line1 = font.render(f"Game Over!! Your score is : {self.snake.length}", True, (255, 0, 0))
        self.surface.blit(line1, (100, 250))
        line2 = font.render(f"To play again press Enter, To exit press Escape!", True, (255, 0, 0))
        self.surface.blit(line2, (100, 300))
        pygame.display.flip()

    def reset(self):
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)

    def run(self):
        running = True
        pause = False

        while running:

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False

                    if not pause:
                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                elif event.type == QUIT:
                    running = False

            try:
                if not pause:
                    self.play()
            except Exception as o:
                self.game_over_mess()
                pause = True
                self.reset()
            fps_controller.tick(difficulty)



if __name__ == "__main__":
    game = Game()
    game.run()



