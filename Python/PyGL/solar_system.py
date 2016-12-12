import math

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image


width, height = 1280, 960
x, z, lx, lz = 0.0, 0.0, 0.0, 1.0
camera_angle = 0.0
zoom_in, ph, th = 0.1, 0.0, 0.0

textures = None
sun_im = Image.open('sun_texture.png').convert('RGBA')
sun_ix, sun_iy, sun_image = sun_im.size[0], sun_im.size[1], sun_im.tobytes()
sun_quadric = gluNewQuadric()

mercury_im = Image.open('mercury_texture.png').convert('RGBA')
mercury_ix, mercury_iy, mercury_image = mercury_im.size[0], mercury_im.size[1], mercury_im.tobytes()
mercury_quadric = gluNewQuadric()

venus_im = Image.open('venus_texture.png').convert('RGBA')
venus_ix, venus_iy, venus_image = venus_im.size[0], venus_im.size[1], venus_im.tobytes()
venus_quadric = gluNewQuadric()

earth_im = Image.open('earth_texture.jpg').convert('RGBA')
earth_ix, earth_iy, earth_image = earth_im.size[0], earth_im.size[1], earth_im.tobytes()
earth_quadric = gluNewQuadric()

mars_im = Image.open('mars_texture.jpg').convert('RGBA')
mars_ix, mars_iy, mars_image = mars_im.size[0], mars_im.size[1], mars_im.tobytes()
mars_quadric = gluNewQuadric()

jupiter_im = Image.open('jupiter_texture.jpg').convert('RGBA')
jupiter_ix, jupiter_iy, jupiter_image = jupiter_im.size[0], jupiter_im.size[1], jupiter_im.tobytes()
jupiter_quadric = gluNewQuadric()

saturn_im = Image.open('saturn_texture.jpg').convert('RGBA')
saturn_ix, saturn_iy, saturn_image = saturn_im.size[0], saturn_im.size[1], saturn_im.tobytes()
saturn_quadric = gluNewQuadric()

uranus_im = Image.open('uranus_texture.png').convert('RGBA')
uranus_ix, uranus_iy, uranus_image = uranus_im.size[0], uranus_im.size[1], uranus_im.tobytes()
uranus_quadric = gluNewQuadric()

neptune_im = Image.open('neptune_texture.jpg').convert('RGBA')
neptune_ix, neptune_iy, neptune_image = neptune_im.size[0], neptune_im.size[1], neptune_im.tobytes()
neptune_quadric = gluNewQuadric()

pluto_im = Image.open('pluto_texture.jpg').convert('RGBA')
pluto_ix, pluto_iy, pluto_image = pluto_im.size[0], pluto_im.size[1], pluto_im.tobytes()
pluto_quadric = gluNewQuadric()

earth_size = 0.0006
earth_distance_from_sun = 0.150
earth_orbital_speed = 0.01
earth_rotation_speed = 0.01


def init():
    global textures

    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, 1.33, 0.00001, 100.0)
    textures = glGenTextures(11)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(x + lx, 0.5, z + lz, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0)

    glPushMatrix()
    glRotatef(ph, 1.0, 0.0, 0.0)
    glRotatef(th, 0.0, 1.0, 0.0)
    glScalef(zoom_in, zoom_in, zoom_in)
    draw_sun()
    draw_planets()

    glPopMatrix()
    glutSwapBuffers()
    glFlush()


def draw_orbit(radius):
    glPushMatrix()
    glBegin(GL_LINE_LOOP)

    for i in range(58 * 360):
        angle = 2.0 * math.pi * i / 360.0
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))

        glVertex2f(x, y)

    glEnd()
    glPopMatrix()

sun_rotation = 0.0


def draw_sun():
    global sun_rotation

    sun_texture_id = textures[0]
    glBindTexture(GL_TEXTURE_2D, sun_texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, sun_ix, sun_iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, sun_image)
    glEnable(GL_TEXTURE_2D)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    gluQuadricTexture(sun_quadric, GL_TRUE)

    glPushMatrix()
    glRotatef(sun_rotation, 0.0, 0.0, 1.0)
    gluSphere(sun_quadric, earth_size * 54, 50, 50)
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)

    sun_rotation += 30 * earth_rotation_speed
    sun_rotation %= 360


def draw_planets():
    draw_mercury()
    draw_venus()
    draw_earth()
    draw_mars()
    draw_jupiter()
    draw_saturn()
    draw_uranus()
    draw_neptune()
    draw_pluto()

mercury_rotation = 0.0


def draw_mercury():
    global mercury_rotation

    mercury_texture_id = textures[1]
    glBindTexture(GL_TEXTURE_2D, mercury_texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, mercury_ix, mercury_iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, sun_image)
    glEnable(GL_TEXTURE_2D)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    gluQuadricTexture(mercury_quadric, GL_TRUE)

    glPushMatrix()
    glRotatef(mercury_rotation, 0.0, 0.0, 1.0)
    glTranslatef(0.387 * earth_distance_from_sun, 0.0, 0.0)
    gluSphere(mercury_quadric, earth_size * 3.8, 50, 50)
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)
    draw_orbit(0.387 * earth_distance_from_sun)

    mercury_rotation += 58.8 * earth_rotation_speed
    mercury_rotation %= 360

venus_rotation = 0.0


def draw_venus():
    global venus_rotation

    venus_texture_id = textures[2]
    glBindTexture(GL_TEXTURE_2D, venus_texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, venus_ix, venus_iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, venus_image)
    glEnable(GL_TEXTURE_2D)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    gluQuadricTexture(venus_quadric, GL_TRUE)

    glPushMatrix()
    glRotatef(venus_rotation, 0.0, 0.0, 1.0)
    glTranslatef(0.723 * earth_distance_from_sun, 0.0, 0.0)
    gluSphere(venus_quadric, earth_size * 9.5, 50, 50)
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)
    draw_orbit(0.723 * earth_distance_from_sun)

    venus_rotation += -244 * earth_rotation_speed
    venus_rotation %= 360

earth_rotation = 0.0


def draw_earth():
    global earth_rotation

    earth_texture_id = textures[3]
    glBindTexture(GL_TEXTURE_2D, earth_texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, earth_ix, earth_iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, earth_image)
    glEnable(GL_TEXTURE_2D)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    gluQuadricTexture(earth_quadric, GL_TRUE)

    glPushMatrix()
    glRotatef(earth_rotation, 0.0, 0.0, 1.0)
    glTranslatef(earth_distance_from_sun, 0.0, 0.0)
    gluSphere(earth_quadric, 10 * earth_size, 50, 50)
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)
    draw_orbit(earth_distance_from_sun)

    earth_rotation += earth_rotation_speed
    earth_rotation %= 360

mars_rotation = 0.0


def draw_mars():
    global mars_rotation

    mars_texture_id = textures[4]
    glBindTexture(GL_TEXTURE_2D, mars_texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, mars_ix, mars_iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, mars_image)
    glEnable(GL_TEXTURE_2D)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    gluQuadricTexture(mars_quadric, GL_TRUE)

    glPushMatrix()
    glRotatef(mars_rotation, 0.0, 0.0, 1.0)
    glTranslatef(1.52 * earth_distance_from_sun, 0.0, 0.0)
    gluSphere(mars_quadric, earth_size * 5.2, 50, 50)
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)
    draw_orbit(1.52 * earth_distance_from_sun)

    mars_rotation += earth_rotation_speed * 11.03
    mars_rotation %= 360

jupiter_rotation = 0.0


def draw_jupiter():
    global jupiter_rotation

    jupiter_texture_id = textures[5]
    glBindTexture(GL_TEXTURE_2D, jupiter_texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, jupiter_ix, jupiter_iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, jupiter_image)
    glEnable(GL_TEXTURE_2D)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    gluQuadricTexture(jupiter_quadric, GL_TRUE)
    glPushMatrix()
    glRotatef(jupiter_rotation, 0.0, 0.0, 1.0)
    glTranslatef(5.20 * earth_distance_from_sun, 0.0, 0.0)
    gluSphere(jupiter_quadric, earth_size * 110.20, 50, 50)
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)
    draw_orbit(5.2 * earth_distance_from_sun)

    jupiter_rotation += earth_rotation_speed * 0.415
    jupiter_rotation %= 360

saturn_rotation = 0.0


def draw_saturn():
    global saturn_rotation

    saturn_texture_id = textures[6]
    glBindTexture(GL_TEXTURE_2D, saturn_texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, saturn_ix, saturn_iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, saturn_image)
    glEnable(GL_TEXTURE_2D)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    glPushMatrix()
    glRotatef(saturn_rotation, 0.0, 0.0, 1.0)
    glTranslatef(9.58 * earth_distance_from_sun, 0.0, 0.0)
    gluSphere(saturn_quadric, earth_size * 90.40, 50, 50)
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)
    draw_orbit(9.58 * earth_distance_from_sun)

    saturn_rotation += earth_rotation_speed * 0.445
    saturn_rotation %= 360


uranus_rotation = 0.0


def draw_uranus():
    global uranus_rotation

    uranus_texture_id = textures[7]
    glBindTexture(GL_TEXTURE_2D, uranus_texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, uranus_ix, uranus_iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, uranus_image)
    glEnable(GL_TEXTURE_2D)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    glPushMatrix()
    glRotatef(uranus_rotation, 0.0, 0.0, 1.0)
    glTranslatef(19.2 * earth_distance_from_sun, 0.0, 0.0)
    gluSphere(uranus_quadric, earth_size * 40.04, 50, 50)
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)
    draw_orbit(19.2 * earth_distance_from_sun)

    uranus_rotation += earth_rotation_speed * -0.72
    uranus_rotation %= 360


neptune_rotation = 0.0


def draw_neptune():
    global neptune_rotation

    neptune_texture_id = textures[8]
    glBindTexture(GL_TEXTURE_2D, neptune_texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, neptune_ix, neptune_iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, neptune_image)
    glEnable(GL_TEXTURE_2D)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    glPushMatrix()
    glRotatef(neptune_rotation, 0.0, 0.0, 1.0)
    glTranslatef(30.05 * earth_distance_from_sun, 0.0, 0.0)
    gluSphere(neptune_quadric, earth_size * 30.88, 50, 50)
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)
    draw_orbit(30.05 * earth_distance_from_sun)

    neptune_rotation += earth_rotation_speed * -0.72
    neptune_rotation %= 360

pluto_rotation = 0.0


def draw_pluto():
    global pluto_rotation

    pluto_texture_id = textures[9]
    glBindTexture(GL_TEXTURE_2D, pluto_texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, pluto_ix, pluto_iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, pluto_image)
    glEnable(GL_TEXTURE_2D)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    glPushMatrix()
    glRotatef(pluto_rotation, 0.0, 0.0, 1.0)
    glTranslatef(39.48 * earth_distance_from_sun, 0.0, 0.0)
    gluSphere(pluto_quadric, earth_size * 1.86, 50, 50)
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)
    draw_orbit(39.48 * earth_distance_from_sun)

    pluto_rotation += earth_rotation_speed * 6.41
    pluto_rotation %= 360


def process_keys(key, xx, yy):
    global th, ph, zoom_in, x, z, lx, lz, camera_angle

    if key == GLUT_KEY_LEFT:
        th -= 10.0
    elif key == GLUT_KEY_RIGHT:
        th += 10.0
    elif key == GLUT_KEY_UP:
        ph += 10.0
    elif key == GLUT_KEY_DOWN:
        ph -= 10.0
    elif key == 'i':
        zoom_in += 0.3
    elif key == 'o':
        zoom_in -= 0.3

    if zoom_in <= 0:
        zoom_in = 0.01


if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 200)
    glutCreateWindow('Solar system')
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutKeyboardFunc(process_keys)
    glutSpecialFunc(process_keys)
    init()
    glutMainLoop()