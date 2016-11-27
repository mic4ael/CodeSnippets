#include <math.h>

#include <OpenGL/gl.h>
#include <OpenGL/glu.h>
#include <GLUT/glut.h>


void init(void);
void display(void);
void processKeys(int key, int xx, int yy);
void drawBall(void);
void drawSpring(void);

static int width = 640;
static int height = 480;
static float cameraAngle = 0.0;
static float lx = 0.0;
static float lz = -1.0;
static float x = 320.0;
static float z = -5.0;

int main (int argc, char **argv)
{
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
	glMatrixMode(GL_PROJECTION);	
	glLoadIdentity();
    gluPerspective(45.0, width / height, 1.0, 640);
	glOrtho(-width, width, -height, height, -20.0, 20.0);
}

void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(x, 240.0, z, x + lx, 0.0, z + lz, 0.0, 1.0, 0.0);
	drawBall();
    drawSpring();
	glutSwapBuffers();
}

void processKeys(int key, int xx, int yy)
{
    float fraction = 2.0;
    switch (key) {
        case GLUT_KEY_LEFT:
            cameraAngle -= 1.0;
            lx = sin(cameraAngle);
            lz = -cos(cameraAngle);
            break;
        case GLUT_KEY_RIGHT:
            cameraAngle += 1.0;
            lx = sin(cameraAngle);
            lz = -cos(cameraAngle);
           break;
        case GLUT_KEY_UP:
           x += lx * fraction;
           z += lz * fraction;
           break;
        case GLUT_KEY_DOWN:
            x -= lx * fraction;
            z -= lz * fraction;
            break;
	}
}

void drawBall()
{
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    glPushMatrix();
    glColor3f(0.5, 0.3, 0.9);
    glutSolidSphere(50.0, 20, 20);
    glPopMatrix();
}