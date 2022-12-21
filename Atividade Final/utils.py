import random


rand = lambda a,b: random.uniform(a,b)
clip = lambda x: max(-0.99, min(0.99, x))

def create_random_quad():
    # obter um ponto aleatorio para ser o centro do quadrilatero
    x,y = (rand(-1, 1) for i in range(2))

    # definir a altura/2 e largura/2 do quad
    w, h = (rand(0.1, 1)/2 for i in range(2))

    #calcular xmin,xmax,ymin,ymax
    xmin = clip(x - w)
    xmax = clip(x + w)
    ymin = clip(y - h)
    ymax = clip(y + h)

    #calcular os 4 pontos referente ao quad
    a = (xmin, ymin)
    b = (xmax, ymin)
    c = (xmax, ymax)
    d = (xmin, ymax)

    return a, b, c, d

def create_random_triangle():
    # obter um ponto aleatorio para ser a referencia do triangulo (quase)
    x,y = (rand(-1, 1) for i in range(2))

    l_min = 0.2
    l_max = 0.6
    a = (x-rand(l_min, l_max), y)
    b = (x+rand(l_min, l_max), y+rand(-l_min, l_min))
    c = (x + rand(-l_min*2, l_min*2), y+rand(l_min*3, l_max))
    a,b,c = ([clip(i) for i in k] for k in (a,b,c))
    return a, b, c