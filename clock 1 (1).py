from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *

"""from datetime import datetime
now = datetime.now()
T = now.strftime("%H:%M:%S")
T = T.split(":")
T = [eval(x) for x in T]
print(T)
if int(T[0])>12:
	T[0] = T[0] % 12
print(T)
"""

sec = 0
mint = 0
hour = 0
time = 1000   # 1 second

def Timer(v):
    draw()
    glutTimerFunc(time, Timer, 1)


def draw_circle(r):
    glLoadIdentity()
    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    glColor3d(0, 0, 0)

    for theta in range(0, 360, 1):
        x = r * cos(theta * pi / 180)
        y = r * sin(theta * pi / 180)
        glVertex2d(x, y)
    glEnd()

def Draw_divisions(num, line_width, theta, r, g, b, R1=.8, R2=.75):
    glLineWidth(line_width)
    glColor3d(r, g, b)
    glBegin(GL_LINES)
    glVertex2d(R1 * cos(num * theta * pi / 180), R1 * sin(num * theta * pi / 180))
    glVertex2d(R2 * cos(num * theta * pi / 180), R2 * sin(num * theta * pi / 180))
    glEnd()


def drawText(string, x, y):
    glLineWidth(2)
    glColor(0, 0, 1)
    glLoadIdentity()
    glTranslate(x, y, 0)
    glScale(0.0004, 0.0004, 1)
    string = string.encode()
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)

def animation_s():
    global sec
    glLoadIdentity()
    # second haand
    glLineWidth(1.5)
    glColor3d(.88, 0, 0)
    glRotate(sec, 0, 0, 1)
    glBegin(GL_LINES)
    glVertex2d(0, 0)
    glVertex2d(0, .78)
    glEnd()
    sec -= (360/60)


def animation_m():
    global mint

    glLoadIdentity()
    # minute hand
    glLineWidth(2.7)
    glColor3d(.34, .45, .555)
    glRotate(mint, 0, 0, 1)
    glBegin(GL_LINES)
    glVertex2d(0, 0)
    glVertex2d(0, -.7)
    glEnd()

    mint -= (6/60)

def animation_h():
    global hour

    # hour hand

    glLineWidth(4)
    glColor3d(0, 0, 1)
    glLoadIdentity()
    glRotate(hour, 0, 0, 1)
    glBegin(GL_LINES)
    glVertex2d(0, 0)
    glVertex2d(0, .55)
    glEnd()
    hour -= (.1/12)

def draw():
    glClearColor(.9, .9, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)

    animation_s()
    animation_m()
    animation_h()

    draw_circle(.83)
    # ############################################################
    for i in range(0, 12, 1):     # Hours
        Draw_divisions(i, 3, 30, 0, 0, 1, .8, .73)

    for i in range(0, 60, 1):     # minute
        Draw_divisions(i, 2.5, 6, .3, .3, 0, .8, .76)

    for i in range(0, 360, 1):    # second
        Draw_divisions(i, 2, 1, 1, 0, 0, .8, .78)

    # ###############################  Number
    theta = 90
    for i in range(1, 13, 1):

        theta = theta - 30
        x = .69 * cos(theta * pi / 180) -.02
        y = .69 * sin(theta * pi / 180) -.02
        drawText(str(i), x, y)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(900, 900)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"clock")
glutDisplayFunc(draw)
glutTimerFunc(time, Timer, 1)
glutMainLoop()
