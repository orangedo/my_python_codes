import myfirsgame, os

os.environ["SDL_VIDEO_CENTERED"] = "1"
myfirsgame.init()

win = myfirsgame.display
d = win.set_mode((1200, 600))

class player:
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = 2

    def draw(self):
        myfirsgame.draw.rect(d, (0, 0, 0), (self.x, self.y, self.width, self.height))

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed


class bullet:
    def __init__(self):
        self.radius = 10
        self.speed = 20


    def shoot(self):
        x = p.x
        y = p.y
        self.shooting = True
        while self.shooting:
            d.fill((98, 98, 98))
            for event in myfirsgame.event.get():
                if event.type == myfirsgame.QUIT:
                    myfirsgame.quit()
                    quit()

            y -= self.speed
            myfirsgame.draw.circle(d, (255, 0, 0), (x, y), self.radius)
            myfirsgame.time.Clock().tick(100)
            win.update()

            if y <= 0:
                self.shooting = False


b = bullet()
p = player(600, 500, 50, 30) 
while True:
    d.fill((98, 98, 98))
    p.draw()
    for event in myfirsgame.event.get():
        pass

    if event.type ==  myfirsgame.KEYDOWN:
        if event.key == myfirsgame.K_SPACE:
            b.shoot()
        if event.key == myfirsgame.K_LEFT:
            p.move_left()
        if event.key == myfirsgame.K_RIGHT:
            p.move_right()



    win.update()
