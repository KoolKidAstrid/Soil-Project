from data import samples, functions
import pygame

#init stuff
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Soil Project")
pygame.init()
running = True

# colors of each polygon
colors = [(255, 128, 0), (255, 200, 128), (200, 128, 255), (255, 100, 50), (128, 100, 0), (50, 128, 0), (0, 255, 128), (255, 0, 0), (200, 255, 128), (0, 100, 100), (255, 255, 200), (0, 200, 200)]

# "fixes" each point to be displayed as an equilateral triangle rather than an upside down right triangle
tex = functions.fixValues(functions)
sam = functions.fixPoints(functions)

# prints lab report to the log
for s in samples.all:
    print(functions.numToLabel(functions, samples.all.index(s)) + " : " + functions.isInside(functions, s))

# draws each polygon of the soil triangle
count = 0
for t in tex:
    pygame.draw.polygon(screen, colors[count], t)
    count += 1
count = 0

# labels each sample
for s in sam:
    font = pygame.font.SysFont(None, 16)
    img = font.render(functions.numToLabel(functions, sam.index(s)), True, (0, 0, 0))
    screen.blit(img, (s[0]-4, s[1]-12))
    pygame.draw.circle(screen, (0, 0, 0), s, 1)
    count += 1
pygame.display.update()

# waits until you quit the program
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.delay(100)

pygame.quit()