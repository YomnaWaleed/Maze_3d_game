import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from coins import *
from math import sin, cos, radians
from pyrr import Vector3

class Grendas:
    def __init__(self, coco):
        self.coco = coco
        self.PX = self.coco.target_x
        self.PY = -0.4
        self.PZ = self.coco.target_z
        self.dirX = 0.4 * sin(self.coco.head)
        self.dirY = self.PY
        self.dirZ = - 0.4 * cos(self.coco.head)

    def draw(self, monsters, grenades):
        glPushMatrix()
        glTranslate(self.dirX, self.dirY, self.dirZ)
        glScale(0.5, 0.5, 0.5)
        self.drawGernades()
        #glutSolidCube(1)
        self.PX += 0.1 * sin(self.coco.head)
        self.PZ -= 0.1 * cos(self.coco.head)
        self.dirZ = self.PZ - cos(self.coco.head)
        self.dirX = self.PX + sin(self.coco.head)
        self.dirY -= 0.008
        if self.dirY < -1:
            grenades.remove(self)

        glPopMatrix()
        return self.collission_1(monsters, grenades)


    def collission_1(self, monsters, grenades):
        global coins_result
        for monster in monsters:
            if monster.x + 0.6 > self.dirX and monster.x - 0.6 < self.dirX:
                if monster.z + 0.6 >self.dirZ and monster.z - 0.6 < self.dirZ:
                    grenades.remove(self)
                    monsters.remove(monster)
                    return True

        return False


    def drawGernades(self):
        glBindTexture(GL_TEXTURE_2D, 17)
        glColor3f(1, 1, 1)
        glBegin(GL_POLYGON)
        # front
        # basic body of gernades
        glTexCoord2f(0.25, 0.1)
        glVertex3f(-0.1, -0.3, 0.1)

        glTexCoord2f(0.75, 0.1)
        glVertex3f(0.1, 0.3, 0.1)

        glTexCoord2f(1, 0.5)
        glVertex3f(0.2, 0, 0.1)

        glTexCoord2f(0.75, 0.75)
        glVertex3f(0.1, 0.1, 0.1)

        glTexCoord2f(0.25, 0.75)
        glVertex3f(-0.1, 0.1, 0.1)

        glTexCoord2f(0, 0.5)
        glVertex3f(-0.2, 0, 0.1)

        glEnd()
        # above quad
        glBindTexture(GL_TEXTURE_2D, 17)
        glBegin(GL_QUADS)
        glTexCoord2f(0.25, 0.75)
        glVertex3f(-0.1, 0.1, 0.1)

        glTexCoord2f(0.75, 0.75)
        glVertex3f(0.1, 0.1, 0.1)

        glTexCoord2f(0.75, 0.85)
        glVertex3f(0.1, 0.2, 0.1)

        glTexCoord2f(0.25, 0.85)
        glVertex3f(-0.1, 0.2, 0.1)

        glEnd()
        # the triangle above the quad
        glBindTexture(GL_TEXTURE_2D, 17)
        glBegin(GL_QUADS)
        glTexCoord2f(0.25, 0.85)
        glVertex3f(-0.1, 0.2, 0.1)

        glTexCoord2f(0.75, 0.85)
        glVertex3f(0.1, 0.2, 0.1)

        glTexCoord2f(0.5, 1)
        glVertex3f(0, 0.3, 0.1)

        glEnd()

        glBindTexture(GL_TEXTURE_2D, 17)
        glColor3f(1, 1, 1)
        glBegin(GL_POLYGON)
        # back
        # basic body of gernades
        glTexCoord2f(0.25, 0.1)
        glVertex3f(-0.1, -0.3, 00.05)

        glTexCoord2f(0.75, 0.1)
        glVertex3f(0.1, 0.3, 0.05)

        glTexCoord2f(1, 0.5)
        glVertex3f(0.2, 0, 0.05)

        glTexCoord2f(0.75, 0.75)
        glVertex3f(0.1, 0.1, 0.05)

        glTexCoord2f(0.25, 0.75)
        glVertex3f(-0.1, 0.1, 0.05)

        glTexCoord2f(0, 0.5)
        glVertex3f(-0.2, 0, 0.05)

        glEnd()
        # above quad
        glBindTexture(GL_TEXTURE_2D, 17)
        glBegin(GL_QUADS)
        glTexCoord2f(0.25, 0.75)
        glVertex3f(-0.1, 0.1, 0.05)

        glTexCoord2f(0.75, 0.75)
        glVertex3f(0.1, 0.1, 0.05)

        glTexCoord2f(0.75, 0.85)
        glVertex3f(0.1, 0.2, 0.05)

        glTexCoord2f(0.25, 0.85)
        glVertex3f(-0.1, 0.2, 0.05)

        glEnd()
        # the triangle above the quad
        glBindTexture(GL_TEXTURE_2D, 17)
        glBegin(GL_QUADS)
        glTexCoord2f(0.25, 0.85)
        glVertex3f(-0.1, 0.2, 0.05)

        glTexCoord2f(0.75, 0.85)
        glVertex3f(0.1, 0.2, 0.05)

        glTexCoord2f(0.5, 1)
        glVertex3f(0, 0.3, 0.05)

        glEnd()
        # side left
        # under polygon part
        glBindTexture(GL_TEXTURE_2D, 18)

        glColor3f(1, 1, 0)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-0.1, -0.3, 0.05)

        glTexCoord2f(1, 0)
        glVertex3f(-0.1, -0.3, 0.1)

        glTexCoord2f(1, 1)
        glVertex3f(-0.2, 0, 0.1)

        glTexCoord2f(0, 1)
        glVertex3f(-0.2, 0, 0.05)

        glEnd()

        # right and left for above polygon part
        glBindTexture(GL_TEXTURE_2D, 18)

        glColor3f(1, 1, 0)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-0.2, 0, 0.05)

        glTexCoord2f(1, 0)
        glVertex3f(-0.2, 0, 0.1)

        glTexCoord2f(1, 1)
        glVertex3f(-0.1, 0.1, 0.1)

        glTexCoord2f(0, 1)
        glVertex3f(-0.1, 0.1, 0.05)

        glEnd()

        # part of quad above polygon
        glBindTexture(GL_TEXTURE_2D, 18)

        glColor3f(1, 1, 0)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-0.1, 0.1, 0.05)

        glTexCoord2f(1, 0)
        glVertex3f(-0.1, 0.1, 0.1)

        glTexCoord2f(1, 1)
        glVertex3f(-0.1, 0.2, 0.1)

        glTexCoord2f(0, 1)
        glVertex3f(-0.1, 0.2, 0.05)

        glEnd()
        # part of triangle
        glBindTexture(GL_TEXTURE_2D, 18)

        glColor3f(1, 1, 0)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-0.1, 0.2, 0.05)

        glTexCoord2f(1, 0)
        glVertex3f(-0.1, 0.2, 0.1)

        glTexCoord2f(1, 1)
        glVertex3f(0.15, 0.3, 0.1)

        glTexCoord2f(0, 1)
        glVertex3f(0.15, 0.3, 0.05)

        glEnd()

        # side right
        # under polygon part
        glBindTexture(GL_TEXTURE_2D, 18)

        glColor3f(1, 1, 0)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-0.1, -0.3, 0.1)

        glTexCoord2f(1, 0)
        glVertex3f(-0.1, -0.3, 0.05)

        glTexCoord2f(1, 1)
        glVertex3f(0.2, 0, 0.05)

        glTexCoord2f(0, 1)
        glVertex3f(0.2, 0, 0.1)

        glEnd()

        # right and left for above polygon part
        glBindTexture(GL_TEXTURE_2D, 18)

        glColor3f(1, 1, 0)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(0.2, 0, 0.05)

        glTexCoord2f(1, 0)
        glVertex3f(0.2, 0, 0.1)

        glTexCoord2f(1, 1)
        glVertex3f(0.1, 0.1, 0.1)

        glTexCoord2f(0, 1)
        glVertex3f(0.1, 0.1, 0.05)

        glEnd()

        # part of quad above polygon
        glBindTexture(GL_TEXTURE_2D, 18)

        glColor3f(1, 1, 0)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(0.1, 0.1, 0.05)

        glTexCoord2f(1, 0)
        glVertex3f(0.1, 0.1, 0.1)

        glTexCoord2f(1, 1)
        glVertex3f(0.1, 0.2, 0.1)

        glTexCoord2f(0, 1)
        glVertex3f(0.1, 0.2, 0.05)

        glEnd()
        # part of triangle
        glBindTexture(GL_TEXTURE_2D, 18)

        glColor3f(1, 1, 0)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(0.1, 0.2, 0.05)

        glTexCoord2f(1, 0)
        glVertex3f(0.1, 0.2, 0.1)

        glTexCoord2f(1, 1)
        glVertex3f(0, 0.3, 0.1)

        glTexCoord2f(0, 1)
        glVertex3f(0, 0.3, 0.05)

        glEnd()


