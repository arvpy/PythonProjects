# display a pygame window with random dots and lines
import pygame
import random
size = (800, 600)

def get_random_coordinate():
    x = random.randint(0, 799)
    y = random.randint(0, 599)
    return x, y
def get_random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, blue, green



surface = pygame.display.set_mode(size)
pygame.display.set_caption('This is py game')
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
end = (500, 300)
for count in range(100):
    start = get_random_coordinate()
    end = get_random_coordinate()
    color = get_random_color()
    pygame.draw.line(surface, color, start, end)
dot_radius = 10
for count in range(100):
    pos = get_random_coordinate()
    color = get_random_color()
    radius = random.randint(5, 50)
    pygame.draw.circle(surface, color, pos, radius)

pygame.display.flip()
