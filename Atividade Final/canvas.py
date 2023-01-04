import math

from PyQt5 import  QtGui, QtWidgets

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from utils import *
from transformacoes import *
from display_file import Object

class Canvas(QtWidgets.QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.modo_livre_points = []
        self.modo_livre = False
        self.stuff_to_draw = []
        
    
    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        wmax = self.frameGeometry().width()
        hmax = self.frameGeometry().height()
        x , y = a0.pos().x(), a0.pos().y()
        w = wmax/2
        h = hmax/2
        x = (x - w)/w
        y = -(y - h)/h
        if self.modo_livre:
            self.modo_livre_points.append((x,y))
        return super().mousePressEvent(a0)

    def initializeGL(self) -> None:
        glClearColor(0.8, 0.7, 0.2, 1.0)
        print('initialize')
        return super().initializeGL()
    

    def draw_stuff(self):
        for t in self.stuff_to_draw:
            glBegin(t['type'])
            for point in t['points']:
                glVertex3f(*point, 0)
            glEnd()

    def paintGL(self) -> None:
        self.draw_stuff()
        print('objects:',len(self.stuff_to_draw))
        return super().paintGL()
    
    def resizeGL(self, w: int, h: int) -> None:
        print('resizae')
        return super().resizeGL(w, h)
    
    def add_quad(self):
        print('add quad')
        self.stuff_to_draw.append({
            'type': GL_LINE_LOOP,
            'points': create_random_quad()
            })
        self.paintGL()
        self.update()
    
    def add_triangle(self):
        print('add tri')
        self.stuff_to_draw.append({
            'type': GL_LINE_LOOP,
            'points': create_random_triangle()
            })
        self.paintGL()
        self.update()
    
    def limpar(self):
        self.stuff_to_draw = []
        self.paintGL()
        self.update()
    
    def ativar_modo_livre(self):
        self.modo_livre = True
        self.modo_livre_points = []
    
    def desativar_modo_livre(self):
        self.modo_livre = False
        print(self.modo_livre_points)
        if self.modo_livre_points:
            self.stuff_to_draw.append({
                'type': GL_LINE_LOOP,
                'points': [i for i in self.modo_livre_points]
            })
        self.modo_livre_points = []
        self.paintGL()
        self.update()
    
    def rotate(self, angle=-5):
        rot = Rotation2D(math.radians(angle))
        for obj in self.stuff_to_draw:
            obj_2 = Object('poli', *obj['points'])
            rot(obj_2)
            obj['points'] = obj_2.points
            #print( obj_2.points)
        self.paintGL()
        self.update()
    



    