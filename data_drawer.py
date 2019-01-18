import pygame
import mn_loader as mn

d = mn.data()
d.load_f_testing()

class data_drawer:

    def __init__(self, data):
        self.data = data
        self.i = 0
        self.display = pygame.display.set_mode([320, 320])
        self.end = False

    def even_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.draw()
                    self.i += 1
            if event.type == pygame.QUIT:
                self.end = True

    def draw(self):
        image = self.data[self.i][0]
        self.display.fill((255, 255, 255))
        for y in range(28):
            for x in range(28):
                c = image[y*28+x]*255
                pygame.draw.rect(self.display, (c, c, c), [x*10+20, y*10+20, 10, 10])
        pygame.display.update()

    def start(self):
        while not self.end:
            self.even_handler()


d_draw = data_drawer(d.f_testing_data)
d_draw.start()