# -*- coding: UTF-8 -*-

# 1. Pamiętaj o możliwości zmiany perspektywy
#     przy użyciu strzałek
# 2. Nałożenie tekstur
# 3. Ruch kulki według wzoru z instrukcji
# 4. Budowanie sprężyny z nachodzących na siebie kulek

import math

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


sphere_radius = 50
width, height = 640, 480
camera_angle = 0.0
camera_direction_x = 0.0
camera_direction_z = -1.0
camera = [0, 0, 10]
up = [0, 1, 0]


def set_up_camera():
    gluLookAt(camera[0], camera[1], camera[2],
              camera[0] + camera_direction_x, 1.0, camera[2] + camera_direction_z,
              up[0], up[1], up[2])


def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gl_ortho()


def gl_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-width, width, -height, height, 1.0, 0.0)
    # gluPerspective(45, width / float(height), 0.01, 100)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glViewport(0, 0, width, height)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # set_up_camera()

    glPushMatrix()
    glColor3f(123, 123, 125)
    glTranslatef(150.0, 150.0, 1.0)
    glutSolidSphere(50, 100, 100)
    glPopMatrix()

    glutSwapBuffers()


def handle_keyboard(key, x, y):
    global camera_angle, camera_direction_x, camera_direction_z

    fraction = 0.1
    if key == GLUT_KEY_LEFT:
        camera_angle -= 0.1
        camera_direction_x = math.sin(math.radians(camera_angle))
        camera_direction_z = -math.cos(math.radians(camera_angle))
    elif key == GLUT_KEY_RIGHT:
        camera_angle += 0.1
        camera_direction_x = math.sin(math.radians(camera_angle))
        camera_direction_z = -math.cos(math.radians(camera_angle))
    elif key == GLUT_KEY_UP:
        camera[0] += camera_direction_x * fraction
        camera[2] += camera_direction_z * fraction
    elif key == GLUT_KEY_DOWN:
        camera[0] -= camera_direction_x * fraction
        camera[2] -= camera_direction_z * fraction


if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(width, height)
    glutCreateWindow('Spring')
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutSpecialFunc(handle_keyboard)
    glutKeyboardFunc(handle_keyboard)
    glutDisplayFunc(display)
    glutIdleFunc(display)
    init()
    glutMainLoop()
