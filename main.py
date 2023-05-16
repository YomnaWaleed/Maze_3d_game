from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from image_to_array import image_to_array
from cube import Cube
from camera import *
from player import *
from coins import *
from cube import Cube
from floor import Floor
from texture import Texture
from pygame import mixer
from monsters import *

#############################################
#####################################################
cubesize = 2
map = []
coins_result = 0
coco = camera()
monsters = [Monster(9,2, 90),Monster(2,5, 0),Monster(14,2,5),Monster(18,2,90),Monster(18,16,5),Monster(20,18,90),Monster(15,18,90),Monster(10,18,90),Monster(6,16,5)]
coins = [Coin(1, -0.1, 2),Coin(4,-0.1,6),Coin(4,-0.1,2),Coin(10,-0.1,5),Coin(14,-0.1,5),Coin(12,-0.1,6),Coin(18,-0.1,5),Coin(18,-0.1,8),Coin(18,-0.1,10),Coin(18,-0.1,12),Coin(18,-0.1,18),Coin(14,-0.1,18),Coin(10,-0.1,16),Coin(10,-0.1,14),Coin(8,-0.1,14),Coin(2,-0.1,18),Coin(2,-0.1,16),Coin(2,-0.1,14),Coin(2,-0.1,12)]
floortexture = None
walltexture = None
######################################################
def init():
    glClearColor(0.0, 0.1, 0.26, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(140, 1, 0.1, 100)
    glMatrixMode(GL_MODELVIEW)


##########################################################

def check_collisions(cam, coins, monsters):
    global coins_result
    #check collision between coins and player
    for coin in coins:
        if coin.collission(cam):
            coins_result += 100
            coins.remove(coin)

        # check coolision between grend and monster


    # to show if win or not
    if coins_result >= 500 and cam.target_x >= 21 and cam.target_z >= 15:
        cam.flag = "win"
    elif(coins_result < 500 and cam.target_x >= 21 and cam.target_z >= 15):
        cam.flag = "End"




    for monster in monsters:
        if monster.collission_1(cam):
            while coins_result > 0:
                coins_result -= 100
                monsters.remove(monster)
                break

            if coins_result <= 0:
                cam.flag = "End"
                return False
            else:
                return True
    return coins_result
######################################################################################################


def display():
    global coco, coins_result
    #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    locations = []
    cube = Cube()

    if coco.change_x and coco.change_z:
       coco.reposCamAbo()
    elif not coco.change_x and not coco.change_z:
        coco.reposCamBel()
    else:
        #if not coco.collission(coco.target_x, coco.target_y, coco.target_z):
        coco.reposCamera()

    for grend in coco.grenades:
        global coins_result
        # check to show if hapeend collision between grend and monster or not
        check = grend.draw(monsters, coco.grenades)
        if check:
            coins_result -= 50
        if coins_result <= 0:
            coco.flag = "End"


    #to check collision between monster and player , monster with gernades , coins with player
    check_collisions(coco, coins, monsters)
    for monster in monsters:
        monster.draw()

    for coin in coins:
        coin.draw()
        draw_text_3d_wrapper("collected coins : " + str(coins_result), -0.9, 0.8)


    # Draw Player
    player(coco)
    # ============================================================================

    # Build the maze like a printer; back to front, left to right.
    row_count = 0
    column_count = 0

    wall_x = 0.0
    wall_z = 0.0

    for i in map:

        wall_z = (row_count * (cubesize * 1))

        for j in i:

            # 1 = cube, 0 = empty space.
            if (j == 1):
                glPushMatrix()
                cube.drawcube(2, 1.0)
                wall_x = (column_count * (cubesize * 1))
                locations.append([wall_x, wall_z])
                glPopMatrix()
            else:
                glPushMatrix()
                glTranslate(0, -1, 0)
                glScale(1, 0.1, 1)
                cube.drawcube(1, -1.0)
                glPopMatrix()
            # Move from left to right one cube size.
            glTranslatef(cubesize, 0.0, 0.0)

            column_count += 1

        # Reset position before starting next row, while moving
        # one cube size towards the camera.
        glTranslatef(((cubesize * column_count) * -1), 0.0, cubesize)

        row_count += 1
        # Reset the column count; this is a new row.
        column_count = 0
        coco.locations = locations

    glutSwapBuffers()


#########################################################

def draw_win_or_lose():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    if coco.flag == "play":
        display()

    elif coco.flag == "End":
        glMatrixMode(GL_MODELVIEW)
        gluLookAt(0, 0, 0,
                  0, 0, -1,
                  0, 1, 0)
        glTranslate(0, 0, -0.7)
        glBindTexture(GL_TEXTURE_2D, 20)
        glBegin(GL_POLYGON)
        glTexCoord2f(0, 0)
        glVertex2d(-2, -2)
        glTexCoord2f(1, 0)
        glVertex2d(2, -2)
        glTexCoord2f(1, 1)
        glVertex2d(2, 2)
        glTexCoord2f(0, 1)
        glVertex2d(-2, 2)
        glEnd()
        glutSwapBuffers()


    elif coco.flag == "win":
        glMatrixMode(GL_MODELVIEW)
        gluLookAt(0, 0, 0,
                  0, 0, -1,
                  0, 1, 0)

        glTranslate(0, 0, -0.7)
        glBindTexture(GL_TEXTURE_2D, 19)
        glBegin(GL_POLYGON)
        glTexCoord2f(0, 0)
        glVertex2d(-2, -2)
        glTexCoord2f(1, 0)
        glVertex2d(2, -2)
        glTexCoord2f(1, 1)
        glVertex2d(2, 2)
        glTexCoord2f(0, 1)
        glVertex2d(-2, 2)
        glEnd()
        glutSwapBuffers()

    elif coco.flag == "start":
        glMatrixMode(GL_MODELVIEW)
        gluLookAt(0, 0, 0,
                  0, 0, -1,
                  0, 1, 0)

        glTranslate(0, 0, -0.7)
        glBindTexture(GL_TEXTURE_2D, 21)
        glBegin(GL_POLYGON)
        glTexCoord2f(0, 0)
        glVertex2d(-2, -2)
        glTexCoord2f(1, 0)
        glVertex2d(2, -2)
        glTexCoord2f(1, 1)
        glVertex2d(2, 2)
        glTexCoord2f(0, 1)
        glVertex2d(-2, 2)
        glEnd()

        glutSwapBuffers()







########################################################



######################################################################

if __name__ =="__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(900, 800)
    glutInitWindowPosition(0, 0)

    window = glutCreateWindow('Experimental Maze')
    # Generate map.
    generator = image_to_array()
    map = generator.generateMap("textures/maze_12.png")




    # Load texture.


    glutDisplayFunc(draw_win_or_lose)
    #glutTimerFunc(time_interval, Timer, 1)
    glutIdleFunc(draw_win_or_lose)
    Texture().load_textures()

    glutKeyboardFunc(coco.keyboard)
    glutKeyboardUpFunc(coco.throw)
    init()
    glutSetCursor(GLUT_CURSOR_NONE)
    mixer.init()
    mixer.music.set_volume(0.2)
    mixer.music.load('background2.ogg')
    mixer.music.play(-1)
    glutMainLoop()






