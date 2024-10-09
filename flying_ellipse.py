import pygame, random

# thanks to 
# https://stackoverflow.com/questions/65767785/how-to-draw-a-rotated-ellipse-using-pygame

def draw_ellipse_angle(surface, color, rect, angle, width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.center))

pygame.init()

# common varables
BLACK = (0,0,0)
WHITE = (255,255,255)
GOLD = (127,127,0) 

#Set display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Ellipse On The Move")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

angle = 0
object_rect = [WINDOW_WIDTH-50, 50, 50, 75] 

star_locs, star_rads = [], []
for i in range(175):
    star_locs.append((random.randint(0,WINDOW_WIDTH),
           random.randint(0,WINDOW_HEIGHT)))
    star_rads.append(random.randint(1,2))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display_surface.fill(BLACK)

    for index, loc in enumerate(star_locs):
        if(random.random() <= 0.996):
            pygame.draw.circle(display_surface, WHITE, loc, star_rads[index])

    draw_ellipse_angle(display_surface, GOLD, object_rect, angle, width=3)
    pygame.display.update()
    clock.tick(FPS)
    angle += 3
    object_rect[0] -= 2

pygame.quit()