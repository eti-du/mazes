import os, json, pygame
import maze.maze as lab



def ui_mazechoice(window, window_size):
    #$ wtf did you just put a class in a function
    class mazefile:
        def __init__(self,jsonc) -> None:
            self.dict = json.loads(jsonc)

            for key,val in self.dict.items():
                exec("self." + str(key) + "= val")


    fileslist = []
    font = pygame.font.Font(pygame.font.get_default_font(), 50)
    loop = True

    cl = pygame.time.Clock()


    for files in os.listdir(os.path.join(os.getcwd(),"asset\mazes")):
        if files.endswith(".json"):

            with open(os.path.join(os.path.join(os.getcwd(),"asset\mazes"),files),"r") as file:
                fileslist.append(mazefile(file.read()))


    for i in range (len(fileslist)):
            window.blit(font.render(fileslist[i].name, True, (200,200,200)),(50, i*60 + 20))

    pygame.display.update()


    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                loop = False
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONUP:
                if (event.pos[1]-20) // 60 < len(fileslist):
                    loop = False
                    lab.main_function(window, window_size, fileslist[(event.pos[1]-20) // 60].maze, fileslist[(event.pos[1]-20) // 60].init_position)

        cl.tick(60)
    pygame.quit()
