import random

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()


translation = 0.0
translation_speed = 0.001
rotation = 0.0

def draw_triangle(x, y, z, color):
    glBegin(GL_TRIANGLES)
    glColor3f(*color)
    glVertex3f(*x)
    glVertex3f(*y)
    glVertex3f(*z)
    glEnd()


def display():
    global translation
    global translation_speed
    global rotation

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)

    glPushMatrix()
    glRotate(rotation, 0.0, 0.0, 1.0)
    glTranslatef(translation, translation, 0.0)
    draw_triangle([0.0, 0.1, 0.0], [0.1, 0.0, 0.0], [0.0, 0.0, 0.0], [0.1, 0.2, 0.3])
    glPopMatrix()

    glPushMatrix()
    glRotate(360 - rotation, 0.0, 0.0, 1.0)
    glTranslatef(translation, translation, 0.0)
    draw_triangle([0.0, 0.2, 0.0], [0.1, 0.1, 0.0], [0.0, 0.1, 0.0], [0.4, 0.5, 0.6])
    draw_triangle([0.1, 0.0, 0.0], [0.1, 0.1, 0.0], [0.2, 0.0, 0.0], [0.9, 0.8, 0.7])
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation, 0.0, 0.0, 1.0)
    glTranslatef(1.2 * translation, 1.2 * translation, 0.0)
    draw_triangle([0.0, 0.3, 0.0], [0.1, 0.2, 0.0], [0.0, 0.2, 0.0], [0.7, 0.8, 0.9])
    glPopMatrix()
    glPushMatrix()
    glRotate(rotation, 0.0, 0.0, 1.0)
    glTranslatef(2.0 * translation, 2.0 * translation, 0.0)
    draw_triangle([0.1, 0.1, 0.0], [0.1, 0.2, 0.0], [0.2, 0.1, 0.0], [0.6, 0.5, 0.4])
    glPopMatrix()
    glPushMatrix()
    glRotate(rotation, 0.0, 0.0, 1.0)
    glTranslatef(1.2 * translation, 1.2 * translation, 0.0)
    draw_triangle([0.2, 0.0, 0.0], [0.2, 0.1, 0.0], [0.3, 0.0, 0.0], [0.3, 0.2, 0.1])
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation, 0.0, 0.0, 1.0)
    glTranslatef(-translation, translation, 0.0)
    draw_triangle([0.0, 0.1, 0.0], [-0.1, 0.0, 0.0], [0.0, 0.0, 0.0], [0.2, 0.3, 0.9])
    glPopMatrix()

    glPushMatrix()
    glRotate(360 - rotation, 0.0, 0.0, 1.0)
    glTranslatef(-translation, translation, 0.0)
    draw_triangle([0.0, 0.2, 0.0], [-0.1, 0.1, 0.0], [0.0, 0.1, 0.0], [0.9, 0.3, 0.2])
    draw_triangle([-0.1, 0.0, 0.0], [-0.1, 0.1, 0.0], [-0.2, 0.0, 0.0], [0.9, 0.2, 0.3])
    glPopMatrix()
    glPushMatrix()
    glRotate(rotation, 0.0, 0.0, 1.0)
    glTranslatef(-1.2 * translation, 1.2 * translation, 0.0)
    draw_triangle([0.0, 0.3, 0.0], [-0.1, 0.2, 0.0], [0.0, 0.2, 0.0], [0.1, 0.1, 0.1])
    glPopMatrix()
    glPushMatrix()
    glRotate(rotation, 0.0, 0.0, 1.0)
    glTranslatef(-2.0 * translation, 2.0 * translation, 0.0)
    draw_triangle([-0.1, 0.1, 0.0], [-0.1, 0.2, 0.0], [-0.2, 0.1, 0.0], [0.2, 0.2, 0.2])
    glPopMatrix()
    glPushMatrix()
    glRotate(rotation, 0.0, 0.0, 1.0)
    glTranslatef(-1.2 * translation, 1.2 * translation, 0.0)
    draw_triangle([-0.2, 0.0, 0.0], [-0.2, 0.1, 0.0], [-0.3, 0.0, 0.0], [0.1, 0.0, 0.5])
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation, 0.0, 0.0, 1.0)
    glTranslatef(translation, -translation, 0.0)
    draw_triangle([0.0, -0.1, 0.0], [0.1, 0.0, 0.0], [0.0, 0.0, 0.0], [0.11, 0.1, 0.7])
    glPopMatrix()

    glPushMatrix()
    glRotate(360 - rotation, 0.0, 0.0, 1.0)
    glTranslatef(translation, -translation, 0.0)
    draw_triangle([0.0, -0.2, 0.0], [0.1, -0.1, 0.0], [0.0, -0.1, 0.0], [0.21, 0.12, 0.7])
    draw_triangle([0.1, 0.0, 0.0], [0.1, -0.1, 0.0], [0.2, 0.0, 0.0], [0.41, 0.43, 0.7])
    glPopMatrix()
    glPushMatrix()
    glRotate(rotation, 0.0, 0.0, 1.0)
    glTranslatef(1.2 * translation, -1.2 * translation, 0.0)
    draw_triangle([0.0, -0.3, 0.0], [0.1, -0.2, 0.0], [0.0, -0.2, 0.0], [0.31, 0.23, 0.7])
    glPopMatrix()
    glPushMatrix()
    glRotate(rotation, 0.0, 0.0, 1.0)
    glTranslatef(2.0 * translation, -2.0 * translation, 0.0)
    draw_triangle([0.1, -0.1, 0.0], [0.1, -0.2, 0.0], [0.2, -0.1, 0.0], [0.51, 0.54, 0.7])
    glPopMatrix()
    glPushMatrix()
    glRotate(rotation, 0.0, 0.0, 1.0)
    glTranslatef(1.2 * translation, -1.2 * translation, 0.0)
    draw_triangle([0.2, 0.0, 0.0], [0.2, -0.1, 0.0], [0.3, 0.0, 0.0], [0.61, 0.89, 0.7])
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation, 0.0, 0.0, 1.0)
    glTranslatef(-translation, -translation, 0.0)
    draw_triangle([0.0, -0.1, 0.0], [-0.1, 0.0, 0.0], [0.0, 0.0, 0.0], [0.1, 0.1, 0.5])
    glPopMatrix()

    glPushMatrix()
    glRotate(360 - rotation, 0.0, 0.0, 1.0)
    glTranslatef(-translation, -translation, 0.0)
    draw_triangle([0.0, -0.2, 0.0], [-0.1, -0.1, 0.0], [0.0, -0.1, 0.0], [0.0, 0.5, 0.5])
    draw_triangle([-0.1, 0.0, 0.0], [-0.1, -0.1, 0.0], [-0.2, 0.0, 0.0], [0.9, 0.9, 0.5])
    glPopMatrix()
    glPushMatrix()
    glRotate(rotation, 0.0, 0.0, 1.0)
    glTranslatef(-1.2 * translation, -1.2 * translation, 0.0)
    draw_triangle([0.0, -0.3, 0.0], [-0.1, -0.2, 0.0], [0.0, -0.2, 0.0], [0.2, 0.7, 0.5])
    glPopMatrix()
    glPushMatrix()
    glRotate(rotation, 0.0, 0.0, 1.0)
    glTranslatef(-2.0 * translation, -2.0 * translation, 0.0)
    draw_triangle([-0.1, -0.1, 0.0], [-0.1, -0.2, 0.0], [-0.2, -0.1, 0.0], [0.5, 0.9, 0.5])
    glPopMatrix()
    glPushMatrix()
    glRotate(rotation, 0.0, 0.0, 1.0)
    glTranslatef(-1.2 * translation, -1.2 * translation, 0.0)
    draw_triangle([-0.2, 0.0, 0.0], [-0.2, -0.1, 0.0], [-0.3, 0.0, 0.0], [0.1, 0.9, 0.5])
    glPopMatrix()
    glFlush()

    translation += translation_speed
    if translation >= 0.2 or translation <= 0:
        translation_speed *= -1
    rotation += 1.0


if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(640, 480)
    glutCreateWindow('Rotating triangles')
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutDisplayFunc(display)
    glutIdleFunc(display)
    init()
    glutMainLoop()
