import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# pygame.init()

screen_width = 1000
screen_height = 800
background_color = (0.0, 0.0, 0.0, 1.0)
drawing_color = (1, 0.5, 0.5, 0.1)

# screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
# pygame.display.set_caption('OpenGL in Python')

angle = 45


def init():

    luz_ambiente = (0.2,0.2,0.2,1.0)
    luz_difusa = (0.7,0.7,0.7,1.0)
    luz_especular = (1.0, 1.0, 1.0, 1.0)
    posicao_luz = (0.0, 50.0, 50.0, 1.0)

    especularidade = (1.0, 1.0, 1.0, 1.0)
    especMaterial = 60

    glClearColor(*background_color)

    glShadeModel(GL_SMOOTH)

    glMaterialfv(GL_FRONT, GL_SPECULAR, especularidade)
    glMateriali(GL_FRONT,GL_SHININESS, especMaterial)

    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luz_ambiente)

    glLightfv(GL_LIGHT0, GL_AMBIENT, luz_ambiente)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luz_difusa)
    glLightfv(GL_LIGHT0, GL_SPECULAR, luz_especular)
    glLightfv(GL_LIGHT0, GL_POSITION, posicao_luz)

    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)

    visual_params()



def visual_params():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(angle, (screen_width / screen_height), 0.4, 500.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,80,200, 0,0,0, 0,1,0)




def display_callback():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    glutSolidTeapot(50.0)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800,600)
glutCreateWindow("Visualizacao 3D")
glutDisplayFunc(display_callback)

init()
glutMainLoop()
