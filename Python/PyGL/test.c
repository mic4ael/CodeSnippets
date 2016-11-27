#include <math.h>

#include <OpenGL/gl.h>
#include <OpenGL/glu.h>
#include <GLUT/glut.h>

#define COS(x) cos(M_PI / 180 * (x))
#define SIN(x) sin(M_PI / 180 * (x))
#define DEF_D 5

void init(void);
void display(void);
void processKeys(int key, int xx, int yy);
void drawBall(void);
void drawSpring(void);
void drawSurface(void);
void drawBaseCylinder(void);
void drawSphereCylinder(void);

static int width = 860;
static int height = 640;
static float yCameraAngle = 0.0;
static float xCameraAngle = 0.0;
static int th = 0;
static int ph = 0;
static int spiralSqueeze = 0;
static GLUquadric *quadric;

void vertex(double th2, double ph2)
{
    double x = SIN(th2) * COS(ph2);
    double y = COS(th2) * COS(ph2);
    double z = SIN(ph2);
    glVertex3d(x, y, z);
}

int main (int argc, char **argv)
{
    quadric = gluNewQuadric();
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
	glutInitWindowSize(width, height);
	glutInitWindowPosition(500, 200);
	glutCreateWindow("Spring simulation");
	glutDisplayFunc(display);
    glutIdleFunc(display);
    glutKeyboardFunc(processKeys);
	glutSpecialFunc(processKeys);
    init();
	glutMainLoop();
	return 0;
}

void init(void)
{
    glEnable(GL_DEPTH_TEST);
	glClearColor(0.0, 0.0, 0.0, 0.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(0.0, 5.0, 5.0, 0, 0, 0, 0, -COS(ph), 0);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
    glViewport(0, 0, width, height);
    // gluPerspective(45.0, 1.33, 0.000000001, 10);
	glOrtho(-8, 8, -8, 8, -8.0, 8.0);
}

void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glMatrixMode(GL_MODELVIEW);
    glPushMatrix();
    glRotatef(ph, 1.0, 0.0, 0.0);
    glRotatef(th, 0.0, 0.0, 1.0);
    drawBaseCylinder();
	drawSurface();
    drawSpring();
    drawSphereCylinder();
    drawBall();
    glPopMatrix();
    glFlush();
	glutSwapBuffers();
}

void processKeys(int key, int xx, int yy)
{
    switch (key) {
        case GLUT_KEY_LEFT:
            th -= 5;
            break;
        case GLUT_KEY_RIGHT:
            th += 5;
            break;
        case GLUT_KEY_UP:
            ph += 5;
            break;
        case GLUT_KEY_DOWN:
            ph -= 5;
            break;
	}

    th %= 360;
    ph %= 360;

    glutPostRedisplay();
}

void drawBall()
{
    int th2, ph2;

    glPushMatrix();
    glTranslatef(0.0, 0.0, -1.3);
    for (ph2 = -90; ph2 < 90; ph2 += DEF_D) {
        glBegin(GL_QUAD_STRIP);
        for (th2 = 0; th2 <= 360; th2 += 2 * DEF_D) {
            glColor3f(0.5, 0.5, 0.5);
            vertex(th2, ph2);
            glColor3f(0.0, 0.5, 0.0);
            vertex(th2, ph2 + 50);
        }
        glEnd();
    }
    glPopMatrix();
}

void drawSpring()
{
    double angle;
    double x, y, z = 0.0;

    glPushMatrix();
    for (angle = 0.0; angle <= 360; angle += 0.1) {
        x = COS(6 * angle);
        y = SIN(6 * angle);
        z += 0.001;

        glPushMatrix();
        glTranslatef(x, y, z);
        glColor3f(0.2, 0.5, 1.0);
        glutSolidSphere(0.1, 20, 20);
        glPopMatrix();
    }

    while (x >= 0) {
        glPushMatrix();
        glTranslatef(x, y, z);
        glColor3f(0.2, 0.5, 1.0);
        glutSolidSphere(0.1, 20, 20);
        glPopMatrix();
        x -= 0.01;
    }

    glPopMatrix();
}

void drawSurface()
{
    int i;
    glPushMatrix();
    for (i = 0; i < 10000; ++i) {
        glBegin(GL_POLYGON);
        glColor3f(0.3, 0.2, 0.9);
        glVertex3d(-1.0, -1.0, 4.0 + i * 0.0001);
        glVertex3d(1.0, -1.0, 4.0 + i * 0.0001);
        glVertex3d(1.0, 1.0, 4.0 + i * 0.0001);
        glVertex3d(-1.0, 1.0, 4.0 + i * 0.0001);
        glEnd();
    }
    glPopMatrix();
}

void drawBaseCylinder()
{
    glPushMatrix();
    glColor3f(0.2, 0.5, 1.0);
    glTranslatef(0.0, 0.0, 3.6);
    gluCylinder(quadric, 0.1, 0.1, 0.4, 50, 50);
    glPopMatrix();
}

void drawSphereCylinder(void)
{
    float x = 1.0, y = 0.0, z = 0.0;
    while (x >= 0) {
        glPushMatrix();
        glTranslatef(x, y, z);
        glColor3f(0.2, 0.5, 1.0);
        glutSolidSphere(0.1, 20, 20);
        glPopMatrix();
        x -= 0.01;
    }

    glPushMatrix();
    glColor3f(0.2, 0.5, 1.0);
    glTranslatef(0.0, 0.0, -0.4);
    gluCylinder(quadric, 0.1, 0.1, 0.4, 50, 50);
    glPopMatrix();
}