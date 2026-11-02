from pico2d import load_image


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(x, y):
        Grass.image.draw(x, y)

    def update(self):
        pass
