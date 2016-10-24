import random
import time

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

rotation_angle = 0.0
rotation_around_center = 0.0
translation = 0


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, 640.0, 0.0, 480.0)


def display():
    global rotation_angle
    global rotation_around_center
    global translation

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glRotate(rotation_around_center, 0.0, 0.0, 1.0)
    glTranslatef(-0.01 * translation, 0.01 * translation, 0.0)
    glTranslatef(-0.07, 0.07, 0.0)
    glRotate(rotation_angle, -0.0, 0.0, 0.1)
    glTranslatef(0.07, -0.07, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.5, 0.5, 0.2)
    glVertex3f(0.0, 0.2, 0.0)
    glVertex3f(-0.2, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation_around_center, 0.0, 0.0, 1.0)
    glTranslatef(0.01 * translation, 0.01 * translation, 0.0)
    glTranslatef(0.07, 0.07, 0.0)
    glRotate(rotation_angle, 0.0, 0.0, 1.0)
    glTranslatef(-0.07, -0.07, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.1, 0.1, 0.9)
    glVertex3f(0.2, 0.0, 0.0)
    glVertex3f(0.0, 0.2, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation_around_center, 0.0, 0.0, 1.0)
    glTranslatef(-0.01 * translation, -0.01 * translation, 0.0)
    glTranslatef(-0.07, -0.07, 0.0)
    glRotate(rotation_angle, 0.0, 0.0, 1.0)
    glTranslatef(0.07, 0.07, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.5, 0.1, 0.3)
    glVertex3f(0.0, -0.2, 0.0)
    glVertex3f(-0.2, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation_around_center, 0.0, 0.0, 1.0)
    glTranslatef(0.01 * translation, -0.01 * translation, 0.0)
    glTranslatef(0.07, -0.07, 0.0)
    glRotate(rotation_angle, 0.0, 0.0, 1.0)
    glTranslatef(-0.07, 0.07, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.25, 0.8, 0.0)
    glVertex3f(0.2, 0.0, 0.0)
    glVertex3f(0.0, -0.2, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation_around_center, 0.0, 0.0, 1.0)
    glTranslatef(-0.01 * translation, 0.01 * translation, 0.0)
    glTranslatef(-0.07, 0.27, 0.0)
    glRotate(rotation_angle, 0.0, 0.0, 1.0)
    glTranslatef(0.07, -0.27, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.91, 0.18, 0.21)
    glVertex3f(0.0, 0.4, 0.0)
    glVertex3f(-0.2, 0.2, 0.0)
    glVertex3f(0.0, 0.2, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation_around_center, 0.0, 0.0, 1.0)
    glTranslatef(0.01 * translation, 0.01 * translation, 0.0)
    glTranslatef(0.07, 0.27, 0.0)
    glRotate(rotation_angle, 0.0, 0.0, 1.0)
    glTranslatef(-0.07, -0.27, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.25, 0.15, 0.34)
    glVertex3f(0.2, 0.2, 0.0)
    glVertex3f(0.0, 0.4, 0.0)
    glVertex3f(0.0, 0.2, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation_around_center, 0.0, 0.0, 1.0)
    glTranslatef(0.01 * translation, 0.01 * translation, 0.0)
    glTranslatef(0.07, 0.47, 0.0)
    glRotate(rotation_angle, 0.0, 0.0, 1.0)
    glTranslatef(-0.07, -0.47, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.15, 0.0, 0.87)
    glVertex3f(0.0, 0.4, 0.0)
    glVertex3f(0.2, 0.4, 0.0)
    glVertex3f(0.0, 0.6, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation_around_center, 0.0, 0.0, 1.0)
    glTranslatef(-0.01 * translation, 0.01 * translation, 0.0)
    glTranslatef(-0.07, 0.47, 0.0)
    glRotate(rotation_angle, 0.0, 0.0, 1.0)
    glTranslatef(0.07, -0.47, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.9, 0.2, 0.87)
    glVertex3f(0.0, 0.4, 0.0)
    glVertex3f(-0.2, 0.4, 0.0)
    glVertex3f(0.0, 0.6, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation_around_center, 0.0, 0.0, 1.0)
    glTranslatef(-0.01 * translation, -0.01 * translation, 0.0)
    glTranslatef(-0.07, -0.27, 0.0)
    glRotate(rotation_angle, 0.0, 0.0, 1.0)
    glTranslatef(0.07, 0.27, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.9, 0.2, 0.87)
    glVertex3f(0.0, -0.2, 0.0)
    glVertex3f(-0.2, -0.2, 0.0)
    glVertex3f(0.0, -0.4, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation_around_center, 0.0, 0.0, 1.0)
    glTranslatef(0.01 * translation, -0.01 * translation, 0.0)
    glTranslatef(0.07, -0.27, 0.0)
    glRotate(rotation_angle, 0.0, 0.0, 1.0)
    glTranslatef(-0.07, 0.27, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.9, 0.9, 0.17)
    glVertex3f(0.0, -0.2, 0.0)
    glVertex3f(0.2, -0.2, 0.0)
    glVertex3f(0.0, -0.4, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation_around_center, 0.0, 0.0, 1.0)
    glTranslatef(-0.01 * translation, -0.01 * translation, 0.0)
    glTranslatef(-0.07, -0.47, 0.0)
    glRotate(rotation_angle, 0.0, 0.0, 1.0)
    glTranslatef(0.07, 0.47, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.4, 0.1, 0.9)
    glVertex3f(0.0, -0.4, 0.0)
    glVertex3f(-0.2, -0.4, 0.0)
    glVertex3f(0.0, -0.6, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation_around_center, 0.0, 0.0, 1.0)
    glTranslatef(0.01 * translation, -0.01 * translation, 0.0)
    glTranslatef(0.07, -0.47, 0.0)
    glRotate(rotation_angle, 0.0, 0.0, 1.0)
    glTranslatef(-0.07, 0.47, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.01, 0.21, 0.31)
    glVertex3f(0.0, -0.4, 0.0)
    glVertex3f(0.2, -0.4, 0.0)
    glVertex3f(0.0, -0.6, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation_around_center, 0.0, 0.0, 1.0)
    glTranslatef(0.01 * translation, 0.01 * translation, 0.0)
    glTranslatef(0.27, 0.07, 0.0)
    glRotate(rotation_angle, 0.0, 0.0, 1.0)
    glTranslatef(-0.27, -0.07, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.21, 0.78, 0.15)
    glVertex3f(0.2, 0.0, 0.0)
    glVertex3f(0.2, 0.2, 0.0)
    glVertex3f(0.4, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation_around_center, 0.0, 0.0, 1.0)
    glTranslatef(0.01 * translation, -0.01 * translation, 0.0)
    glTranslatef(0.27, -0.07, 0.0)
    glRotate(rotation_angle, 0.0, 0.0, 1.0)
    glTranslatef(-0.27, 0.07, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.33, 0.16, 0.28)
    glVertex3f(0.2, 0.0, 0.0)
    glVertex3f(0.2, -0.2, 0.0)
    glVertex3f(0.4, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation_around_center, 0.0, 0.0, 1.0)
    glTranslatef(-0.01 * translation, 0.01 * translation, 0.0)
    glTranslatef(-0.27, 0.07, 0.0)
    glRotate(rotation_angle, 0.0, 0.0, 1.0)
    glTranslatef(0.27, -0.07, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.1, 0.99, 0.41)
    glVertex3f(-0.2, 0.0, 0.0)
    glVertex3f(-0.2, 0.2, 0.0)
    glVertex3f(-0.4, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation_around_center, 0.0, 0.0, 1.0)
    glTranslatef(-0.01 * translation, -0.01 * translation, 0.0)
    glTranslatef(-0.27, -0.07, 0.0)
    glRotate(rotation_angle, 0.0, 0.0, 1.0)
    glTranslatef(0.27, 0.07, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.25, 0.87, 0.11)
    glVertex3f(-0.2, 0.0, 0.0)
    glVertex3f(-0.2, -0.2, 0.0)
    glVertex3f(-0.4, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation_around_center, 0.0, 0.0, 1.0)
    glTranslatef(-0.01 * translation, 0.01 * translation, 0.0)
    glTranslatef(-0.47, 0.07, 0.0)
    glRotate(rotation_angle, 0.0, 0.0, 1.0)
    glTranslatef(0.47, -0.07, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.9, 0.51, 0.41)
    glVertex3f(-0.4, 0.0, 0.0)
    glVertex3f(-0.4, 0.2, 0.0)
    glVertex3f(-0.6, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation_around_center, 0.0, 0.0, 1.0)
    glTranslatef(-0.01 * translation, -0.01 * translation, 0.0)
    glTranslatef(-0.47, -0.07, 0.0)
    glRotate(rotation_angle, 0.0, 0.0, 1.0)
    glTranslatef(0.47, 0.07, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.78, 0.15, 0.96)
    glVertex3f(-0.4, 0.0, 0.0)
    glVertex3f(-0.4, -0.2, 0.0)
    glVertex3f(-0.6, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation_around_center, 0.0, 0.0, 1.0)
    glTranslatef(0.01 * translation, 0.01 * translation, 0.0)
    glTranslatef(0.47, 0.07, 0.0)
    glRotate(rotation_angle, 0.0, 0.0, 1.0)
    glTranslatef(-0.47, -0.07, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.11, 0.91, 0.44)
    glVertex3f(0.4, 0.0, 0.0)
    glVertex3f(0.4, 0.2, 0.0)
    glVertex3f(0.6, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation_around_center, 0.0, 0.0, 1.0)
    glTranslatef(0.01 * translation, -0.01 * translation, 0.0)
    glTranslatef(0.47, -0.07, 0.0)
    glRotate(rotation_angle, 0.0, 0.0, 1.0)
    glTranslatef(-0.47, 0.07, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.45, 0.11, 0.24)
    glVertex3f(0.4, 0.0, 0.0)
    glVertex3f(0.4, -0.2, 0.0)
    glVertex3f(0.6, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation_around_center, 0.0, 0.0, 1.0)
    glTranslatef(0.01 * translation, 0.01 * translation, 0.0)
    glTranslatef(0.27, 0.27, 0.0)
    glRotate(rotation_angle, 0.0, 0.0, 1.0)
    glTranslatef(-0.27, -0.27, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.45, 0.65, 0.45)
    glVertex3f(0.2, 0.2, 0.0)
    glVertex3f(0.2, 0.4, 0.0)
    glVertex3f(0.4, 0.2, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation_around_center, 0.0, 0.0, 1.0)
    glTranslatef(0.01 * translation, -0.01 * translation, 0.0)
    glTranslatef(0.27, -0.27, 0.0)
    glRotate(rotation_angle, 0.0, 0.0, 1.0)
    glTranslatef(-0.27, 0.27, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.63, 0.66, 0.66)
    glVertex3f(0.2, -0.2, 0.0)
    glVertex3f(0.2, -0.4, 0.0)
    glVertex3f(0.4, -0.2, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation_around_center, 0.0, 0.0, 1.0)
    glTranslatef(-0.01 * translation, 0.01 * translation, 0.0)
    glTranslatef(-0.27, 0.27, 0.0)
    glRotate(rotation_angle, 0.0, 0.0, 1.0)
    glTranslatef(0.27, -0.27, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.91, 0.19, 0.29)
    glVertex3f(-0.2, 0.2, 0.0)
    glVertex3f(-0.2, 0.4, 0.0)
    glVertex3f(-0.4, 0.2, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glRotate(rotation_around_center, 0.0, 0.0, 1.0)
    glTranslatef(-0.01 * translation, -0.01 * translation, 0.0)
    glTranslatef(-0.27, -0.27, 0.0)
    glRotate(rotation_angle, 0.0, 0.0, 1.0)
    glTranslatef(0.27, 0.27, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.43, 0.16, 0.28)
    glVertex3f(-0.2, -0.2, 0.0)
    glVertex3f(-0.2, -0.4, 0.0)
    glVertex3f(-0.4, -0.2, 0.0)
    glEnd()
    glPopMatrix()

    rotation_angle += 5.0
    translation += 0.15
    rotation_around_center += -1.0

    rotation_angle %= 360
    rotation_around_center %= 360
    translation %= 20

    glFlush()


if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(640, 480)
    glutCreateWindow('Rotating triangles')
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutDisplayFunc(display)
    glutIdleFunc(display)
    init()
    glutMainLoop()
