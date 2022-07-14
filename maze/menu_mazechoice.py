import os, json, pygame
import maze.maze as lab



def ui_mazechoice(window, window_size):
    #$ wtf did you just put a class in a function
    #yep this is a class in a fonction, it allow to make for each files an object of mazefile with all his meta-data
    class mazefile:
        def __init__(self,jsonc) -> None:
            #convert the json format to python format
            self.dict = json.loads(jsonc)

            #? The val value can be show as unuse by your software but it's false
            #for each attribute of the file, create a parameter of the object
            for key,val in self.dict.items():
                exec("self." + str(key) + "= val")


    fileslist = []
    font = pygame.font.Font(pygame.font.get_default_font(), 50)
    loop = True

    cl = pygame.time.Clock()

    #take all files locate in the assets/mazes directory
    for files in os.listdir(os.path.join(os.getcwd(),"assets\mazes")):
        if files.endswith(".json"):

            with open(os.path.join(os.path.join(os.getcwd(),"assets\mazes"),files),"r") as file:
                fileslist.append(mazefile(file.read()))

    #show the list on the screen
    pygame.draw.rect(window, (70,15,20), [0, 0, window_size[0], window_size[1]],0)
    for i in range (len(fileslist)):
            window.blit(font.render(fileslist[i].name, True, (200,200,200)),(50, i*60 + 20))
    pygame.display.update()

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                loop = False
                pygame.quit()

            #wait until a file is chosen by the player
            elif event.type == pygame.MOUSEBUTTONUP:
                if (event.pos[1]-20) // 60 < len(fileslist):
                    loop = False
                    fi = fileslist[(event.pos[1]-20) // 60]#find the right file
                    #launch the maze
                    lab.main_function(window, window_size, fi.maze, fi.init_position, fi.end_position)
                    return

        cl.tick(60)