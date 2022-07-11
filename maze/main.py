#coding:utf-8
"""
Project : Maze

This is the main file of the project
It allow to show the menu and run the others files

"""

"""
$ NBRET : 2022-07-11 ; 03:08AM
$ GOOD GOD HOW DO YOU EVEN BEGIN TO READ THIS
TODO: CLEANUP!

? anyway I'll be using naming conventions from here https://namingconvention.org/python/
? so if you want to use a different hit me up
"""


class main():
    #modules
    import pygame
    from maze.maze_gen import lab_gen
    import maze.maze as lab
    import maze.menu_mazechoice as ui_choice



    #PyGame init ; window loading
    print("Loading...")
    pygame.init()


    window_size = pygame.display.get_desktop_sizes()[0] #grab the size of the screen
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("| Labyrinth |")

    #geez that one's a lineful (=ｘェｘ=)
    window.blit(pygame.font.Font('freesansbold.ttf', 20).render("... CHARGEMENT ...", True, (245, 215, 20)), (500,370))
    pygame.display.flip()


    #Initialisation
    loop = True
    cl = pygame.time.Clock()
    font = pygame.font.Font(pygame.font.get_default_font(), 150)
    font1 = pygame.font.Font(pygame.font.get_default_font(), 50)



    #menu creation
    #draws the background (solid color)
    pygame.draw.rect(window, (70,15,20), [0, 0, window_size[0], window_size[1]],0)

    #buttons backgrounds/boxes
    pygame.draw.rect(window, (40,30,100), [window_size[0]//2-200, window_size[1]*0.65, 400, 70],0)#"Play" button box
    pygame.draw.rect(window, (40,30,100), [window_size[0]//2-200, window_size[1]*0.75, 400, 70],0)#maze selection button box
    pygame.draw.rect(window, (40,30,100), [window_size[0]//2-200, window_size[1]*0.85, 400, 70],0)#maze randomize button box

    #Title
    window.blit(font.render("Mazes ???",
                            True,
                            (85,100,240)),
                (window_size[0]//2 - 75*5,
                window_size[1]//4))

    #buttons labels
    #"Play" button label
    window.blit(font1.render("Play",
                            True,
                            (85,100,240)),
                (window_size[0]//2 - 60,
                window_size[1]*0.65 + 10))

    #maze selection button label
    window.blit(font1.render("Choose maze",
                            True,
                            (85,100,240)),
                (window_size[0]//2 - 170,
                window_size[1]*0.75 + 10))

    #maze randomizer button label
    window.blit(font1.render("Random maze",
                            True,
                            (85,100,240)),
                (window_size[0]//2 - 170,
                window_size[1]*0.85 + 10))


    pygame.display.update()#what does this exactly do?


    #wait until the player clicks on a button
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                loop = False
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONUP:
                """
                Tests if the player clicked on "Play"
                µ couldn't we use a simpler measure to get the mouse's position as a tuple?
                µ e.g. (140,202)
                
                µ better yet, couldn't we use some sort of ID for each button,
                µ to automatically know which button was pressed?
                µ i think it'd help because right now the conditions are nothing short of a
                µ nightmare to read and comprehend
                """
                if (window_size[0]//2 - 200) < event.pos[0] < (window_size[0]//2 + 400) and (window_size[1]*0.65) < event.pos[1] < (window_size[1]*0.65 + 70):
                    pygame.draw.rect(window, (100,130,140), [0, 0, window_size[0], window_size[1]],0)
                    loop = False

                    with open("asset\mazes\_default_maze_.json","r") as file:
                        content = eval(file.read())

                    lab.main_function(window,window_size, content['maze'], content['init_position'])


                #Same for "Choose maze"
                elif (window_size[0]//2 - 200) < event.pos[0] < (window_size[0]//2 + 400) and (window_size[1]*0.75) < event.pos[1] < (window_size[1]*0.75 + 70):
                    pygame.draw.rect(window, (70,15,20), [0, 0, window_size[0], window_size[1]],0)
                    loop = False
                    ui_choice.ui_mazechoice(window,window_size)#launches the maze selection menu


                #Same for "Random maze"
                elif (window_size[0]//2 - 200) < event.pos[0] < (window_size[0]//2 + 400) and (window_size[1]*0.85) < event.pos[1] < (window_size[1]*0.85 + 70):
                    loop = False

                    #generates a random maze and then launches it
                    lab.main_function(window, window_size, lab_gen(10,10).maze, {"x":3,"y":3,"z":0})


        #µ is this useful? i thought we used fps instead?
        #µ i might be wrong on this one so don't hesitate to tell me
        cl.tick(60)
    pygame.quit()
