import pygame
import random

pygame.init()

BLUE = pygame.Color("blue")
BLACK = pygame.Color("black")
PINK = pygame.Color("pink")

YELLOW = pygame.Color("yellow")
WHITE = pygame.Color("white")
LIGHT_BLUE = pygame.Color("lightblue")
RED = pygame.Color("red")

SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False

        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True

        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

    def change_color(self):
        self.image.fill(random.choice([YELLOW, WHITE, LIGHT_BLUE, RED]))

def change_background_color():
    global bg_color
    bg_color = random.choice([BLUE, BLACK, PINK])

# Create sprite group and two sprites
all_sprites_list = pygame.sprite.Group()

sp1 = Sprite(WHITE, 20, 30)
sp1.rect.x = random.randint(0, 450)
sp1.rect.y = random.randint(0, 370)
all_sprites_list.add(sp1)

sp2 = Sprite(YELLOW, 20, 30)  # Second sprite with a different color
sp2.rect.x = random.randint(0, 450)
sp2.rect.y = random.randint(0, 370)
all_sprites_list.add(sp2)

screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("change sprites colour")

exit = False
clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()
            sp2.change_color()  
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color()

    all_sprites_list.update()
    screen.fill(BLACK)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(240)

pygame.quit()
