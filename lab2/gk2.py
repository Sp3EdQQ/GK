import pygame
import sys
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rysowanie figur geometrycznych")
class BlackCircleWithYellowSquare:
    def __init__(self, circle_radius, square_side_length):
        self.x = width // 2
        self.y = height // 2
        self.circle_radius = circle_radius
        self.square_side_length = square_side_length
    def draw(self):
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.circle_radius)
        square_x = self.x - self.square_side_length / 2
        square_y = self.y - self.square_side_length / 2
        pygame.draw.rect(screen, (255, 255, 0), (square_x, square_y, self.square_side_length, self.square_side_length))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    figure = BlackCircleWithYellowSquare(100, 80)
    figure.draw()
    pygame.display.flip()