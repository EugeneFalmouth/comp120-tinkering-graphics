import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

image = pygame.image.load("test.png").convert()


def protanopia_adjustment(surface=(1, 1)):
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            surface.set_at(
                (x, y),
                pygame.Color(int(pixel.r * 0.3), pixel.g, pixel.b)
            )


def deuteranopia_adjustment(surface=(1, 1)):
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            surface.set_at(
                (x, y),
                pygame.Color(pixel.r, int(pixel.g * 0.3), pixel.b)
            )


def tritanopia_adjustment(surface=(1, 1)):
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            surface.set_at(
                (x, y),
                pygame.Color(pixel.r, pixel.g, int(pixel.b * 0.3))
            )


protanopia_adjustment(image)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    screen.blit(image, (0, 0))
    pygame.display.update()

pygame.quit()