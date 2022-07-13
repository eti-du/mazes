from random import randint

class lab_gen:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.maze = []
        self.main()



    def main(self):
        #create the structure of the maze full of walls
        for i in range(self.height):
            self.maze.append([i*self.width])
            self.maze.append([-1]*(self.width*2-1))

        for i in range(0,self.height*2,2):
            for j in range(2,self.width*2,2):
                self.maze[i].append(-1)
                self.maze[i].append(j//2+i//2*self.width)


        while True:
            #select a random wall to break
            rand1 = randint(0,self.height*2-2)
            rand2 = randint(0,self.width*2-2)

            #? to break a wall we need to know we are between two room,
            #? it can raise an error in case we are on the edge of the maze
            try:
                if self.maze[rand1][rand2] == -1 and self.maze[rand1][rand2+1] != -1 and self.maze[rand1][rand2-1] != -1 and self.maze[rand1][rand2+1] != self.maze[rand1][rand2-1]:
                    #break the wall
                    self.maze[rand1][rand2] = -2
                    
                    if self.maze[rand1][rand2+1] > self.maze[rand1][rand2-1]:#abracadabra un labyrinthe selmiammaimcestbon
                        self.impact(self.maze[rand1][rand2-1],self.maze[rand1][rand2+1])


                    elif self.maze[rand1][rand2+1] < self.maze[rand1][rand2-1]:
                        self.impact(self.maze[rand1][rand2+1],self.maze[rand1][rand2-1])


                elif self.maze[rand1][rand2] == -1 and self.maze[rand1+1][rand2] != -1 and self.maze[rand1-1][rand2] != -1 and self.maze[rand1+1][rand2] != self.maze[rand1-1][rand2]:
                    #break the wall
                    self.maze[rand1][rand2] = -2

                    if self.maze[rand1+1][rand2] > self.maze[rand1-1][rand2]:
                        self.impact(self.maze[rand1-1][rand2],self.maze[rand1+1][rand2])


                    elif self.maze[rand1+1][rand2] < self.maze[rand1-1][rand2]:
                        self.impact(self.maze[rand1+1][rand2],self.maze[rand1-1][rand2])
            except IndexError: 
                pass
            #check if the maze is completely generated
            #print(str(self.maze).count(' 0'))
            if str(self.maze).count('0') == self.height*self.width:
                #if so, stop the loop
                break
        self.const()


    #change all @old_num by @new_num
    def impact(self,new_num,old_num):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == old_num:
                    self.maze[i][j] = new_num


    #transforme the list maze to be understandable by the other program
    def const(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                k = self.maze[i][j]
                if k == -1:
                    self.maze[i][j] = 2
                else:
                    self.maze[i][j] = 0

        #add walls around the maze to avoid error
        self.maze = [[2]*(len(self.maze[1]))] + self.maze
        [self.maze[i].insert(0,2) for i in range(len(self.maze))]
        [self.maze[i].append(2) for i in range(len(self.maze))]

        #add a different color for the end
        self.maze[len(self.maze)-1][len(self.maze)-2] = 3
        self.maze[len(self.maze)-2][len(self.maze)-1] = 3

        self.maze = [self.maze,[0]]



"""
$ this fonction allow to see how the maze look like 
    def temp_rendu(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                k = self.maze[i][j]
                if i/2 == int(i/2):
                    if k == -1:
                        print("|",sep='',end='')
                    elif k == -2:
                        print(":",sep='',end='')
                    else:
                        print(k,sep='',end='')
                        if k < 10:
                            print(' ',sep='',end='')
                else:
                    if j/2 == int(j/2):
                        if k == -2:
                            print("..",sep='',end='')
                        elif k == -1:
                            print("__",sep='',end='')
                        else:
                            print("?",sep='',end='')
                    else:
                        if k == -2:
                            print(".",sep='',end='')
                        elif k == -1:
                            print("+",sep='',end='')
                        else:
                            print("?",sep='',end='')
            print("")
"""