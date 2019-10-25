import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

picture = pygame.image.load("image.png").convert()


def save_adjusted_image(surface, name):
    """Save the received surface on the disk with the given name."""
    pygame.image.save(surface, name)


def protanopia_adjustment(surface=(1, 1)):
    """Adjust the image to reflect a very simplified version of protanopia"""
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            surface.set_at(
                (x, y),
                pygame.Color(int(pixel.r * 0.3), pixel.g, pixel.b)
            )
            name = "protanopia.png"
            save_adjusted_image(surface, name)


def deuteranopia_adjustment(surface=(1, 1)):
    """Adjust the image to reflect a very simplified version of deuteranopia"""
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            surface.set_at(
                (x, y),
                pygame.Color(pixel.r, int(pixel.g * 0.3), pixel.b)
            )
            name = "deuteranopia.png"
            save_adjusted_image(surface, name)


def tritanopia_adjustment(surface=(1, 1)):
    """Adjust the image to reflect a very simplified version of tritanopia"""
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            surface.set_at(
                (x, y),
                pygame.Color(pixel.r, pixel.g, int(pixel.b * 0.3))
            )
            name = "tritanopia.png"
            save_adjusted_image(surface, name)


protanopia_adjustment(picture.copy())
deuteranopia_adjustment(picture.copy())
tritanopia_adjustment(picture.copy())


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
