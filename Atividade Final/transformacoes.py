import numpy as np


class Transform2D:
    def __call__(self, obj):
        points = obj.points
        assert hasattr(self, 'matrix') and self.matrix.shape == (3, 3)
        w_points = self.with_w(points)
        new_points = np.matmul(self.matrix, w_points.T)
        obj.set_points(new_points.T)
        return obj

    def with_w(self, points):
        if len(points[0]) == 3: return points
        return np.array([(*point, 1) for point in points])

class Translate2D(Transform2D):
    def __init__(self, dx, dy):
        self.matrix = np.array([
            [1, 0, dx],
            [0, 1, dy],
            [0, 0,  1]
            ])


class Rotation2D(Transform2D):
    def __init__(self, angle):
        cos = np.cos(angle)
        sin = np.sin(angle)
        self.matrix = np.array([
            [cos, -sin,  0],
            [sin,  cos,  0],
            [  0,    0,  1]
            ])
    
    def obter_centro(self, obj):
        xs = [i[0] for i in list(obj.points)]
        ys = [i[1] for i in list(obj.points)]
        print(xs, ys)
        gx = sum(xs)/len(xs)
        gy = sum(ys)/len(ys)
        return gx, gy
    
    def __call__(self, obj):
        gx, gy = self.obter_centro(obj)
        obj.points = [(x-gx, y-gy) for x,y in obj.points]
        obj = super().__call__(obj)
        obj.points = [(x+gx, y+gy) for x,y in obj.points]
        return obj
    
class Scale2D(Transform2D):
    def __init__(self, sx, sy=None):
        if sy is None: sy = sx

        self.matrix = np.array([
            [sx, 0, 0],
            [0, sy, 0],
            [0, 0,  1]
            ])


