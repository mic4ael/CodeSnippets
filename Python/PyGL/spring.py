# -*- coding: UTF-8 -*-

# 1. Pamiętaj o możliwości zmiany perspektywy
#     przy użyciu strzałek
# 2. Nałożenie tekstur
# 3. Ruch kulki według wzoru z instrukcji
# 4. Budowanie sprężyny z nachodzących na siebie kulek

import math

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image


width, height = 860, 640
spiral_squeeze = 1.0
spiral_squeeze_coeff = 1
x_camera_angle, y_camera_angle = 0.0, 0.0
th, ph = 0, 0
z_move = 0.0
x, z, lx, lz = 0.0, 5.0, 0.0, -1.0
camera_angle = 0.0

brick_im = Image.open('brick_texture.jpg').convert('RGBA')
brick_ix, brick_iy, brick_image = brick_im.size[0], brick_im.size[1], brick_im.tobytes()

water_im = Image.open('water_texture.jpg').convert('RGBA')
water_ix, water_iy, water_image = water_im.size[0], water_im.size[1], water_im.tobytes()

metal_im = Image.open('metal_texture.jpg').convert('RGBA')
metal_ix, metal_iy, metal_image = metal_im.size[0], metal_im.size[1], metal_im.tobytes()

quadric = gluNewQuadric()
spring_quadric = gluNewQuadric()


def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glViewport(0, 0, width, height)
    glOrtho(-15.0, 15.0, -15.0, 15.0, -15.0, 15.0)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(x, 1.0, z, x + lx, 10.0, z + lz, 0.0, 1.0, 0.0)

    glPushMatrix()
    glRotatef(ph, 1.0, 0.0, 0.0)
    glRotatef(th, 0.0, 0.0, 1.0)
    glTranslatef(0.0, 0.0, -4.0)

    draw_surface()
    draw_spring()
    draw_ball()

    glPopMatrix()
    glutSwapBuffers()
    glFlush()

    global spiral_squeeze, spiral_squeeze_coeff

    if spiral_squeeze <= 1.0:
        spiral_squeeze_coeff = 1;
    elif spiral_squeeze >= 1.7:
        spiral_squeeze_coeff = -1

    spiral_squeeze += spiral_squeeze_coeff * 0.05


def process_keys(key, xx, yy):
    global camera_angle, lx, lz, x, z

    if key == GLUT_KEY_LEFT:
        camera_angle -= 2.0
        lx = math.sin(math.radians(camera_angle))
        lz = -math.cos(math.radians(camera_angle))
    elif key == GLUT_KEY_RIGHT:
        camera_angle += 2.0
        lx = math.sin(math.radians(camera_angle))
        lz = -math.cos(math.radians(camera_angle))
    elif key == GLUT_KEY_UP:
        x += lx * 2.0
        z += lz * 2.0
    elif key == GLUT_KEY_DOWN:
        x -= lx * 2.0
        z -= lz * 2.0

    glutPostRedisplay()


def draw_base_cylinder():
    glPushMatrix()
    glTranslatef(0.0, 0.0, -1.5)
    gluCylinder(spring_quadric, 0.1, 0.1, 1.5, 50, 50)
    glPopMatrix()


def draw_surface():
    brick_texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, brick_texture_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, brick_ix, brick_iy, 0, GL_RGBA,
                 GL_UNSIGNED_BYTE, brick_image)
    glEnable(GL_TEXTURE_2D)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

    glPushMatrix()
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 0.0)
    glVertex3d(-1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3d(1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3d(1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3d(-1.0, 1.0, -1.0)
    glEnd()
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 0.0)
    glVertex3d(-1.0, 1.0, -2.5)
    glTexCoord2f(0.0, 0.0)
    glVertex3d(1.0, 1.0, -2.5)
    glTexCoord2f(0.0, 1.0)
    glVertex3d(1.0, 1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3d(-1.0, 1.0, -1.0)
    glEnd()
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 0.0)
    glVertex3d(-1.0, -1.0, -2.5)
    glTexCoord2f(0.0, 0.0)
    glVertex3d(1.0, -1.0, -2.5)
    glTexCoord2f(0.0, 1.0)
    glVertex3d(1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3d(-1.0, -1.0, -1.0)
    glEnd()
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 0.0)
    glVertex3d(1.0, 1.0, -2.5)
    glTexCoord2f(0.0, 0.0)
    glVertex3d(1.0, -1.0, -2.5)
    glTexCoord2f(0.0, 1.0)
    glVertex3d(1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3d(1.0, 1.0, -1.0)
    glEnd()
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 0.0)
    glVertex3d(-1.0, 1.0, -2.5)
    glTexCoord2f(0.0, 0.0)
    glVertex3d(-1.0, -1.0, -2.5)
    glTexCoord2f(0.0, 1.0)
    glVertex3d(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3d(-1.0, 1.0, -1.0)
    glEnd()
    glBegin(GL_POLYGON)
    glTexCoord2f(1.0, 0.0)
    glVertex3d(-1.0, -1.0, -2.5)
    glTexCoord2f(0.0, 0.0)
    glVertex3d(1.0, -1.0, -2.5)
    glTexCoord2f(0.0, 1.0)
    glVertex3d(1.0, 1.0, -2.5)
    glTexCoord2f(1.0, 1.0)
    glVertex3d(-1.0, 1.0, -2.5)
    glEnd()
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)


def draw_spring():
    global z_move

    angle = 0.0
    x, y, z, new_z = 0.0, 0.0, 0.0, 0.0
    metal_texture_id = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, metal_texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, metal_ix, metal_iy, 0, GL_RGBA,
                 GL_UNSIGNED_BYTE, metal_image)
    glEnable(GL_TEXTURE_2D)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    gluQuadricDrawStyle(spring_quadric, GLU_FILL)
    gluQuadricTexture(spring_quadric, GL_TRUE)
    gluQuadricNormals(spring_quadric, GLU_SMOOTH)

    draw_base_cylinder()

    glPushMatrix()

    while angle <= 360.0:
        x = math.cos(math.radians(6 * angle))
        y = math.sin(math.radians(6 * angle))
        new_z = spiral_squeeze * 0.001
        z += new_z
        z_move = new_z - z
        angle += 0.1

        glPushMatrix()
        glTranslatef(x, y, z)
        gluSphere(spring_quadric, 0.1, 20, 20)
        glPopMatrix()

    while x >= 0:
        glPushMatrix()
        glTranslatef(x, y, z)
        gluSphere(spring_quadric, 0.1, 20, 20)
        glPopMatrix()
        x -= 0.01

    glPopMatrix()

    draw_ball_cylinder()

    glDisable(GL_TEXTURE_2D)


def draw_ball_cylinder():
    x, y, z = 1.0, 0.0, 0.0
    while x >= 0:
        glPushMatrix()
        glTranslatef(x, y, z)
        gluSphere(spring_quadric, 0.1, 20, 20)
        glPopMatrix()
        x -= 0.01

    glPushMatrix()
    glTranslatef(0.0, 0.0, -z_move)
    gluCylinder(spring_quadric, 0.1, 0.1, 0.7, 50, 50)
    glPopMatrix()


def draw_ball():
    water_texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, water_texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, water_ix, water_iy, 0, GL_RGBA,
                 GL_UNSIGNED_BYTE, water_image)
    glEnable(GL_TEXTURE_2D)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    gluQuadricTexture(quadric, GL_TRUE)

    glPushMatrix()
    glTranslatef(0.0, 0.0, 1.4 - z_move)
    gluSphere(quadric, 0.8, 50, 50)
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)


if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(500, 200)
    glutCreateWindow('Spring simulation')
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutKeyboardFunc(process_keys)
    glutSpecialFunc(process_keys)
    init()
    glutMainLoop()
