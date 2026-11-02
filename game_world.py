world = [ [], [] ]

# 잔디 - 플레이어 - 잔디 순으로 출력되어야함. -> 뒷 잔디와 플레이어는 0번 레이어에, 앞 잔디는 1번 레이어에

def add_object(o, layer=0): 
    world[layer].append(o)

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return 

# game logic
def update():
    for layer in world:
        for o in layer:
            o.update()

# game rendering
def render():
    for layer in world:
        for o in layer:
            o.draw()
