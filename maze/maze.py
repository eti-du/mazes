import pygame
from math import cos, sin



def main_function(window, window_size, maze, init_pos, end_pos):
    pygame.draw.rect(window, (125,255,129), [0, 0, window_size[0], window_size[1]], 0)
    pygame.display.update()

    loop = True
    cl = pygame.time.Clock()

    x_ply,y_ply,z_ply = init_pos['x'],init_pos['y'],init_pos['z']# repectively the position x,y,z of the player
    x_direc,y_direc = -1,0#(x_direc,y_direc) is the direction vectors of the direction of the player
    x_plane,y_plane = 0,0.66#the straight line normal to (x_direc,y_direc)

    #time,oldtime = 0,0 #? defunt, use FPS instead

    speed_mov = 0.03
    speed_turn = 0.002

    #? HOLY MAGIC POWERS, DO NOT TEMPER WITH UNLESS PROPERLY TRAINED
    dev_mod = False

    draw(window,x_ply,y_ply,x_direc,y_direc,x_plane,y_plane,maze,window_size[1],window_size[0])

    #play the musics
    pygame.mixer.music.load("asset\music\\ambient_1.ogg")
    pygame.mixer.music.play(loops=1, start=0.0, fade_ms=10000)

    pygame.mouse.set_pos([window_size[0]//2,window_size[1]//2])
    pygame.mouse.set_visible(False)

    pygame.key.set_repeat(10)
    pygame.time.delay(1000)

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                #remove a wall if dev_mod == True and left click
                if dev_mod:
                    i = 1
                    while i<10 and maze[0][int(y_ply + y_direc * i)][int(x_ply + x_direc * i)] == 0:
                        i += 0.1

                    if 0<int(y_ply + y_direc * i)<len(maze[0])-1 and 0<int(x_ply + x_direc * i)<len(maze[0][int(y_ply + y_direc * i)])-1:
                        maze[0][int(y_ply + y_direc * i)][int(x_ply + x_direc * i)] = 0



            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                #place a wall if dev_mod == True and right click
                if dev_mod:
                    i = 0.5
                    while i<10 and maze[0][int(y_ply + y_direc * i)][int(x_ply + x_direc * i)] == 0:
                        i += 0.1
                    i -= 0.1
                    maze[0][int(y_ply + y_direc * i)][int(x_ply + x_direc * i)] = 5


            #move the player when 'z','q','s' or 'd' is pressed
            elif event.type == pygame.KEYDOWN:  #pygame methode event.type only give one key
                if event.key == pygame.K_UP or  event.key == pygame.K_z:
                    if maze[0][int(y_ply)][int(x_ply + x_direc * speed_mov)]  == 0:
                        x_ply += x_direc * speed_mov

                    if maze[0][int(y_ply + y_direc * speed_mov)][int(x_ply)]  == 0:
                        y_ply += y_direc * speed_mov


                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if maze[0][int(y_ply)][int(x_ply + y_direc * speed_mov)]  == 0:
                        x_ply += y_direc * (speed_mov * 0.5)

                    if maze[0][int(y_ply - x_direc * speed_mov)][int(x_ply)]  == 0:
                        y_ply -= x_direc * (speed_mov * 0.5)



                elif event.key == pygame.K_LEFT or event.key == pygame.K_q:
                    if maze[0][int(y_ply)][int(x_ply - y_direc * speed_mov)]  == 0:
                        x_ply -= y_direc * (speed_mov * 0.5)

                    if maze[0][int(y_ply + x_direc * speed_mov)][int(x_ply)]  == 0:
                        y_ply += x_direc * (speed_mov * 0.5)


                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if maze[0][int(y_ply)][int(x_ply - x_direc * speed_mov)]  == 0:
                        x_ply -= x_direc * speed_mov

                    if maze[0][int(y_ply - y_direc * speed_mov)][int(x_ply)]  == 0:
                        y_ply -= y_direc * speed_mov


                if event.key == pygame.K_ESCAPE:
                    loop = False


                if not dev_mod and event.key == pygame.K_F7:
                    dev_mod = True
                    print("dev mod activate")



        pygame.display.update()

        mouse_mov = pygame.mouse.get_pos()
        x_mouse_mov = mouse_mov[0]-window_size[0]//2

        #turn the direction of the player when the mouse is moved
        temp = x_direc
        x_direc = x_direc * cos(-speed_turn*x_mouse_mov)-y_direc*sin(-speed_turn*x_mouse_mov)
        y_direc = temp * sin(-speed_turn*x_mouse_mov) + y_direc * cos(-speed_turn*x_mouse_mov)
        #turn the 'plane' vector
        temp = x_plane
        x_plane = x_plane * cos(-speed_turn*x_mouse_mov) - y_plane * sin(-speed_turn*x_mouse_mov)
        y_plane = temp * sin(-speed_turn*x_mouse_mov) + y_plane * cos(-speed_turn*x_mouse_mov)

        pygame.mouse.set_pos([window_size[0]//2,window_size[1]//2])

        draw(window,x_ply,y_ply,x_direc,y_direc,x_plane,y_plane,maze,window_size[1],window_size[0])

        #check if the player found the end
        if int(x_ply) == end_pos['x'] and int(y_ply) == end_pos['y']:
            pygame.mixer.music.stop()       #stop the music
            pygame.mouse.set_visible(True)  #show the cursor
            loop = False
            return True
        cl.tick(30)



#$ good god it's with this kind of parameters quantity that i miss static typing....
#This fonction aim to draw the ray to the screen
#window {pygame object}
#x_ply, y_ply {float},{float} the position of the player
#x_direc, y_direc {float},{float} the direction of the player
#x_plane, y_plane {float},{float} the 'plane' vector
#maze {list} the "map" of the maze
#window_height, window_width {int},{int} the dimension of the screen
def draw(window, x_ply, y_ply, x_direc, y_direc, x_plane, y_plane, maze, window_height, window_width):
    from maze.color import color_list

    #draw the floor and the ceiling
    pygame.Surface.fill(window,(0,0,0))
    pygame.draw.rect(window,(25,45,125),(0,0,window_width,window_height//2))

    #for every pixel this loop will draw a line. The lengh of the line match the distance from the player of the wall
    for i in range(window_width):
        camera_x = 2*i / window_width-1

        #? parentheses added for ease of reading
        raydirec_x, raydirec_y = (x_direc + x_plane * camera_x), (y_direc + y_plane * camera_x)

        map_x, map_y = int(x_ply), int(y_ply)
        side_dist_x, side_dist_y = 0,0

        #ddista_x is the inverse of raydirec_x; avoid the division by zero in case of raydirec_x is nul
        if raydirec_x != 0:
            ddista_x = abs(1/raydirec_x)
        else:
            ddista_x = 10**10

        if raydirec_y != 0:
            ddista_y = abs(1/raydirec_y)
        else:
            ddista_x = 10**10

        pas_x, pas_y = 0,0

        walltouch = False
        side = 0

        if raydirec_x < 0:
            pas_x, side_dist_x = -1,(x_ply - map_x) * ddista_x
        else:
            pas_x, side_dist_x = 1,(1 + map_x - x_ply) * ddista_x

        if raydirec_y < 0:
            pas_y, side_dist_y = -1,(y_ply - map_y) * ddista_y
        else:
            pas_y, side_dist_y = 1,(1 + map_y - y_ply) * ddista_y

        #a ray is launch from the player and stop when it hit a wall
        while not(walltouch):
            if side_dist_x < side_dist_y:
                side_dist_x += ddista_x
                map_x += pas_x
                side = 0
            else:
                side_dist_y += ddista_y
                map_y += pas_y
                side = 1

            if maze[0][map_y][map_x]>0:
                walltouch = True


        if side == 0:
            wall_distance = side_dist_x - ddista_x
        else:
            wall_distance = side_dist_y - ddista_y

        #if the wall is right before the player, it must be as big as possible
        if wall_distance == 0:
            height_line = window_height
        else:
            height_line = window_height / wall_distance
        
        #calcul where the wall should begin on the screen
        start_point = -height_line / 2 + window_height / 2
        if start_point < 1:
            start_point = 1
        end_point = height_line / 2 + window_height / 2

        #the line to draw must not be longer than the screen
        if end_point >= window_height:
            end_point = window_height - 1
        #select the color according to the number on the maze list
        color = color_list[maze[0][map_y][map_x]-1]

        #add a fake shadow effect
        if side == 1:
            color = (color[0] // 2, color[1] // 2, color[2] // 2)


        pygame.draw.line(window, color, (i,start_point), (i,end_point), width=1)
    #draw the small circle at the center of the screen
    pygame.draw.circle(window, (200,200,200), (window_width // 2, window_height // 2), 3)
    pygame.display.update()

    '''
This is the first try and without raycasting !
It doesn't work but look good so I keep it.
Maybe it will be used for the start menu.

def draw(window,window_size,x_plus,y_plus,x_rect_size,y_rect_size,x_ply):
    dr = pygame.draw
    x_mdl = window_size[0]//2
    y_mdl = window_size[1]//2
    x_max = window_size[0]
    y_max = window_size[1]
    pygame.Surface.fill(window,(100,130,140))
    dr.line(window,(0,0,0),(0,0),(x_mdl-(x_rect_size)+x_plus,y_mdl-(y_rect_size-y_plus)))
    dr.line(window,(0,0,0),(x_max,0),(x_mdl+x_rect_size+x_plus,y_mdl-y_rect_size+y_plus))
    dr.line(window,(0,0,0),(0,y_max),(x_mdl-x_rect_size+x_plus,y_mdl+y_rect_size+y_plus))
    dr.line(window,(0,0,0),(x_max,y_max),(x_mdl+x_rect_size+x_plus,y_mdl+y_rect_size+y_plus))
    dr.rect(window,(45,45,45),(x_mdl-x_rect_size+x_plus,y_mdl-y_rect_size+y_plus,2*x_rect_size,2*y_rect_size))
    a = (y_mdl-(y_rect_size-y_plus)) / (x_mdl-x_rect_size+x_plus)
    f_x = 50-x_ply*4
    f_y = 25
    g_x = 50-x_ply
    g_y = y_max-25
    ad = ((x_mdl-(x_rect_size)+x_plus-0)**2+(y_mdl-(y_rect_size-y_plus)-0)**2)**0.5
    ab = y_max * ad / y_rect_size
    dr.line(window,(0,0,0),(f_x,f_x*a),(g_x,window_size[1]-g_x*a))
    pygame.display.update()

    '''
