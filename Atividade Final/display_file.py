from transformacoes import *

class World:
    def __init__(self, xmin, ymin, xmax, ymax):
        self.set_window(xmin, ymin, xmax, ymax)
        self.objects = []
    
    
    def set_window(self, xmin, ymin, xmax, ymax):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
    
    def add_line(self, point1, point2):
        line = Line(point1, point2)
        self.objects.append(line)
    
    def add_rect(self, p1, p2, p3, p4):
        rect = Rect(p1, p2, p3, p4)
        self.objects.append(rect)
    
    def add_obj(self, obj):
        assert isinstance(obj, Object)
        self.objects.append(obj)


class Object:
    allowed_types = ['line', 'rect', 'tri', 'poli']
    def __init__(self, obj_type, *points):
        self.type = obj_type.lower()
        assert self.type in self.allowed_types
        self.points = points
    
    def set_points(self, new_points):
        assert len(self.points) == len(new_points) # assegurar que a quantidade de pontos s'ao iguais
        self.points = new_points[..., :2]




class Line(Object):
    def __init__(self, p1, p2):
        Object.__init__(self, 'line', p1, p2)


class Rect(Object):
    def __init__(self, p1, p2, p3, p4):
        Object.__init__(self, 'rect', p1, p2, p3, p4)



class Viewport:
    def __init__(self, world, width, height):
        self.world = world
        self.width = width
        self.height = height
    
    def display(self):
        self.transformed_objects = []
        for obj in self.world.objects:
            self.transform_object(obj)

    def transform_object(self, obj):
        points = obj.points
        w = self.world
        print('\n\ntransform obj type:',obj.type)
        new_points = []
        for x,y in points:
            xp = (x - w.xmin)/(w.xmax - w.xmin)*self.width
            yp = (1 - (y- w.ymin)/(w.ymax - w.ymin))*self.height
            new_points.append((xp, yp))
            print('x:{} y: {}\t\t||\t\txp: {} yp: {}'.format(x,y,xp,yp))
        
        self.transformed_objects.append(Object(obj.type, *new_points))


if __name__ == "__main__":
    world = World(100, 100, 300, 300)
    vp = Viewport(world, 400, 400)

    line1 = Line((100, 100), (150, 150))
    world.add_obj(line1)


    vp.display()


    # instanciar transformacoes, recebe uma lista de pontos e retorna a lista de pontos transformados
    translate = Translate2D(20, 35)
    rotate = Rotation2D(0.2)
    scale = Scale2D(2)

    print('='*100)

    translate(line1)
    vp.display()




