import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Grenades import *

class camera:
    def __init__(self):
        self.speed = 0.1
        self. head = 0
        self.move_x = 0  # the x pos of eye player in intialize
        self.move_y = 0.7  # the y pos of eye player in intialize
        self.move_z = 2.5  # the z pos of eye player in intialize
        self.throw_avaliable = True
        self.target_x = self.move_x + self.speed * np.sin(self.head)
        self.target_y = self.move_y - 1
        self.target_z = self.move_z - self.speed * np.cos(self.head)
        self.xabove = self.move_x
        self.yabove = self.move_y
        self.zabove = self.move_z
        self.change_x = True
        self.change_z = False
        self.Front = True
        self.Behind = False
        self.Right = False
        self.Left = False
        self.step = 0.0
        self.flag = "start"
        self.locations = []
        self.grenades = []


    def keyboard(self,key, x, y):
        if key == b"w":
            move_x = self.move_x + self.speed * np.sin(self.head)
            move_z = self.move_z - self.speed * np.cos(self.head)
            newx = move_x + np.sin(self.head)
            newy = self.move_y - 1
            newz = move_z - np.cos(self.head)
            if not self.collission(newx, newy, newz):
                self.move_x += self.speed * np.sin(self.head)
                self.move_z -= self.speed * np.cos(self.head)
                self.xabove = self.move_x
                self.zabove = self.move_z
                self.change_x = True
                self.change_z = False
                self.Left = True
                self.Right = False
                self.Front = False
                self.target_z = self.move_z - np.cos(self.head)
                self.target_x = self.move_x + np.sin(self.head)
                self.target_y = self.move_y - 1
                self.step += 0.1




        if key == b"s":
            #if  self.collission(self.target_x, self.target_y, self.target_z):
            move_x = self.move_x - self.speed * np.sin(self.head)
            move_z = self.move_z + self.speed * np.cos(self.head)

            newx = move_x + np.sin(self.head)
            newy = self.move_y - 1
            newz = move_z - np.cos(self.head)
            if not self.collission(newx, newy, newz):
                self.move_x -= self.speed * np.sin(self.head)
                self.move_z += self.speed * np.cos(self.head)
                self.xabove = self.move_x
                self.zabove = self.move_z
                self.change_x = False
                self.change_z = True
                self.Left = True
                self.Right = False
                self.Front = False
                self.target_z = self.move_z - np.cos(self.head)
                self.target_x = self.move_x + np.sin(self.head)
                self.target_y = self.move_y - 1
                self.step -= 0.1






        if key == b"a":
            #if not self.collission(self.target_x, self.target_y, self.target_z):
            head = self.head - 0.05
            newx = self.move_x + np.sin(head)
            newy = self.move_y - 1
            newz = self.move_z - np.cos(head)
            if not self.collission(newx, newy, newz):
                self.head = head
                self.xabove = self.move_x
                self.zabove = self.move_z
                self.change_x = True
                self.change_z = False
                self.Left = True
                self.Right = False
                self.Front = False
                self.target_z = self.move_z - np.cos(self.head)
                self.target_x = self.move_x + np.sin(self.head)
                self.target_y = self.move_y - 1
                self.step += 0.1



        if key == b"d":
            head = self.head + 0.05
            newx = self.move_x + np.sin(head)
            newy = self.move_y - 1
            newz = self.move_z - np.cos(head)
            if not self.collission(newx, newy, newz):
                self.head += 0.05
                self.xabove = self.move_x
                self.zabove = self.move_z
                self.change_x = True
                self.change_z = False
                self.Right = True
                self.Front = False
                self.Left = False
                self.target_z = self.move_z - np.cos(self.head)
                self.target_x = self.move_x + np.sin(self.head)
                self.target_y = self.move_y - 1
                self.step -= 0.1







        if key == b"f":
            self.xabove += 0.2
            self.yabove += 0.2
            self.zabove -= 0.1
            self.change_x = True
            self.change_z = True


        if key == b"v":
            self.xabove -= 0.2
            self.yabove -= 0.2
            self.zabove += 0.1
            self.change_x = False
            self.change_z = False

        if key == b"o":
            self.xabove = self.move_x
            self.yabove = self.move_y
            self.zabove = self.move_z
            self.change_x = True
            self.change_z = False

        if key == b'q':
            os._exit(0)

        if key == b'p':
            self.flag = "play"

        if key == b' ':
           if self.throw_avaliable == True:
               self.grenades.append(Grendas(self))
               self.throw_avaliable = False


        if self.step >= 0.7 or self.step <= -0.7:
           self.step -= self.step


    def reposCamera(self):
        glLoadIdentity()
        gluLookAt(self.move_x, self.move_y, self.move_z,  # Camera position (eye)
                  self.target_x, self.move_y, self.target_z,  # Camera target (center)
                  0.0, 1.0, 0.0)  # Up vector (pointing down)


    def reposCamAbo(self):
        glLoadIdentity()
        gluLookAt(self.xabove, self.yabove, self.zabove,
                  self.target_x, self.target_y, self.target_z,
                  0, 1, 0)

    def reposCamBel(self):

        glLoadIdentity()

        gluLookAt(self.xabove, self.yabove, self.zabove,
                  self.target_x, self.target_y, self.target_z,
                  0, 1, 0)



    def collission(self, target_x, target_y, target_z):
        for walls in self.locations:
            if walls[0] - 1.15 < target_x and walls[0] + 1.15  > target_x:
                if walls[1] - 1.15 < target_z and walls[1] + 1.15 > target_z:
                    return True
        return False

    def throw(self, key, x, y):
        if key == b' ':
            self.throw_avaliable = True


