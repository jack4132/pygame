import pygame
import sys
import random
import time

class Snake():
    def __init__(self):
        self.length = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (255, 255, 0)
        # Special thanks to YouTubers Mini - Cafetos and Knivens Beast for raising this issue!
        # Code adjustment courtesy of YouTuber Elija de Hoog
        self.level = 0
        self.score = 0
        self.fps = 5
        self.pause=False

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x,y = self.direction
        new = (((cur[0]+(x*gridsize))%screen_width), (cur[1]+(y*gridsize))%screen_height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def next_level(self):
        self.level += 1
        self.fps += 2
        self.reset()

    def win(self):
        self.restart()

    def restart(self):
        self.level = 0
        self.fps = 5
        self.reset()


    def reset(self):
        self.length = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def draw(self,surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93,216, 228), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_f:
                        screen = pygame.display.set_mode((480, 480), pygame.FULLSCREEN, 32)
                elif event.key == pygame.K_g:
                    screen = pygame.display.set_mode((480, 480), 0, 32)
                elif event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)


class Food():
    def __init__(self):
        self.position = (0,0)
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, grid_width-1)*gridsize, random.randint(0, grid_height-1)*gridsize)

    def draw(self,surface):
            r = pygame.Rect((self.position[0], self.position[1]), (gridsize,gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)

class Venom():
    def __init__(self):
        self.positions = [(random.randint(0, grid_width-1)*gridsize, random.randint(0, grid_height-1)*gridsize)]
        self.color = (255, 0, 0)

    def randomize_position(self):
            new = (random.randint(0, grid_width-1)*gridsize, random.randint(0, grid_height-1)*gridsize)
            self.positions.append(new)
            if len(self.positions)>3:
                self.positions.pop(0)
    def reset(self):
        self.positions = [(random.randint(0, grid_width-1)*gridsize, random.randint(0, grid_height-1)*gridsize)]
        self.color = (255, 0, 0)

    def draw(self,surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)

def drawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x+y)%2 == 0:
                r = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface,(0,100,0), r)
            else:
                rr = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface, (0,128,0), rr)

def next(screen):
    bonus_end = pygame.time.get_ticks() + 4000
    deathScreen = True
    while deathScreen:
        #screen.fill(0,0,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        myfont1 = pygame.font.SysFont("Inconsolata", 100)
        text1 = myfont1.render("NEXT LEVEL", 1, (0, 0, 0))
        screen.blit(text1, (20,screen_height/2))
        pygame.time.delay(500)
        #screen.fill(0,0,0)
        pygame.display.flip()
        #clock = pygame.time.Clock()
        print(bonus_end)
        print(pygame.time.get_ticks())
        if pygame.time.get_ticks() > bonus_end:
            break

def congrats(screen):
    bonus_end = pygame.time.get_ticks() + 2000
    deathScreen = True
    while deathScreen:
        #screen.fill(0,0,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        myfont1 = pygame.font.SysFont("Inconsolata", 100)
        text1 = myfont1.render("WIN", 1, (0, 0, 0))
        screen.blit(text1, (screen_width/4,screen_height/2))
        pygame.time.delay(500)
        #screen.fill(0,0,0)
        pygame.display.flip()
        #clock = pygame.time.Clock()
        print(bonus_end)
        print(pygame.time.get_ticks())
        if pygame.time.get_ticks() > bonus_end:
            break


screen_width = 480
screen_height = 480

gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize

up = (0,-1)
down = (0,1)
left = (-1,0)
right = (1,0)

def main():
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
    pygame.display.set_caption("LINDU")
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)
    clock = pygame.time.Clock()


    snake = Snake()
    food = Food()
    venom = Venom()
    myfont = pygame.font.SysFont("Arial",16)

    while (True):
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()
        if snake.get_head_position() in venom.positions:
            snake.restart()
            venom.reset()

        if random.randint(1, 50) == 1: #create venom
            venom.randomize_position()

        if snake.score == 5:
            #pygame.time.delay(5000)

            if snake.level  < 5:
                next(screen)
            snake.next_level()
            venom.reset()

        if snake.level > 5:
            congrats(screen)
            snake.win()

        clock.tick(snake.fps)

        food.draw(surface)
        snake.draw(surface)
        venom.draw(surface)

        screen.blit(surface, (0,0))
        text = myfont.render("Score {0}".format(snake.score), 1, (0,0,0))
        screen.blit(text, (5,10))
        text1 = myfont.render("LEVEL {0}".format(snake.level), 1, (0, 0, 0))
        screen.blit(text1, (screen_width/2, 10))
        pygame.display.update()

main()