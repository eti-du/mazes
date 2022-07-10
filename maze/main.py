#coding:utf-8
"""
Project : Maze
"""

class main():
    import os,pygame
    from random import randint
    from maze.maze_gen import lab_gen
    import maze.maze as lab
    import maze.menu_mazechoice as uichoice
    #Load the window
    print("Loading...")
    pygame.init()
    window_size = pygame.display.get_desktop_sizes()[0]
    window = pygame.display.set_mode(window_size)#, flags=pygame.FULLSCREEN)
    pygame.display.set_caption("| Labyrinth |")
    window.blit(pygame.font.Font('freesansbold.ttf', 20).render("... CHARGEMENT ...", True, (245, 215, 20)),(500,370))
    pygame.display.flip()
    #Initialisation
    loop = True
    cl = pygame.time.Clock()
    font = pygame.font.Font(pygame.font.get_default_font(), 150)
    font1 = pygame.font.Font(pygame.font.get_default_font(), 50)
    #Create of the menu
    pygame.draw.rect(window, (70,15,20), [0, 0, window_size[0], window_size[1]],0)
    pygame.draw.rect(window, (40,30,100), [window_size[0]//2-200, window_size[1]*0.65, 400, 70],0)
    pygame.draw.rect(window, (40,30,100), [window_size[0]//2-200, window_size[1]*0.75, 400, 70],0)
    pygame.draw.rect(window, (40,30,100), [window_size[0]//2-200, window_size[1]*0.85, 400, 70],0)
    window.blit(font1.render("Play", True, (85,100,240)),(window_size[0]//2-60,window_size[1]*0.65+10))
    window.blit(font1.render("Choose maze", True, (85,100,240)),(window_size[0]//2-170,window_size[1]*0.75+10))
    window.blit(font1.render("Random maze", True, (85,100,240)),(window_size[0]//2-170,window_size[1]*0.85+10))
    window.blit(font.render("Mazes ???", True, (85,100,240)),(window_size[0]//2-75*5,window_size[1]//4))
    pygame.display.update()
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                loop = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if window_size[0]//2-200<event.pos[0]<window_size[0]//2+400 and window_size[1]*0.65<event.pos[1]<window_size[1]*0.65+70 :
                    pygame.draw.rect(window, (100,130,140), [0, 0, window_size[0], window_size[1]],0)
                    loop = False
                    with open("asset\mazes\_default_maze_.json","r") as file:
                        content = eval(file.read())
                    lab.main_function(window,window_size,content['maze'],content['init_position'])
                elif window_size[0]//2-200<event.pos[0]<window_size[0]//2+400 and window_size[1]*0.75<event.pos[1]<window_size[1]*0.75+70 :
                    pygame.draw.rect(window, (70,15,20), [0, 0, window_size[0], window_size[1]],0)
                    loop = False
                    uichoice.ui_mazechoice(window,window_size)
                elif window_size[0]//2-200<event.pos[0]<window_size[0]//2+400 and window_size[1]*0.85<event.pos[1]<window_size[1]*0.85+70 :
                    loop = False
                    lab.main_function(window,window_size,lab_gen(10,10).maze,{"x":3,"y":3,"z":0})
        cl.tick(60)
    pygame.quit()
