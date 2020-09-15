import pygame
import random
def checkColumn(num,xVal,matx):
    vacant=1
    for i in range(0,8):
        if matx[i][xVal] == num:
            vacant=0
    if vacant:
        return True
    else:
        return False

        
def checkRow(num,yVal,matx):
    vacant=1
    for i in range(0,8):
        if matx[yVal][i] == num:
            vacant=0
    if vacant:
        return True
    else:
        return False

sudok=[[1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,89,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,85,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,88,9],
        [1,2,3,4,5,6,7,8,9]]
#checkRow(1,8,sudok)
#checkColumn(1,6,sudok)

def checkSquare(num,xVal,yVal,matx):
    #This will check the 3x3 square and see if the number attempted is fine
    #need to find which quadrant on x and y axis
    #if topleft quadrant is (0,0), the middle quadrant is (1,1)
    vacant=1
    quadrantX = (xVal//3)*3
    quadrantY = (yVal//3)*3
    for i in range(quadrantY,quadrantY+3):
        for j in range(quadrantX,quadrantX+3):
            if matx[i][j] == num:
                vacant=0
    if vacant:
        return True
    else:
        return False
checkSquare(88,8,4,sudok)

def sudoku(mtx):
    finished=0
    ind=[0,0] #Current tile being worked on, ind[0] is x value ind[1] is y value
    numTry=1    #Current number being attempted to be added in
    addedList=[]    #The list of tile coordinates added into the sudoku matrix
    while finished==0:  #Will reiterate until it reaches the bottomright tile
        if mtx[ind[1]][ind[0]] == 0:    #0 indicates a "blank" that needs to be filled in
            if checkSquare(numTry,ind[0],ind[1],mtx) and checkRow(numTry,ind[1],mtx) and checkColumn(numTry,ind[0],mtx):
                mtx[ind[1]][ind[0]] = numTry
                addedList.append([ind[0],ind[1]])
                numTry=1    #Reset numTry on success
            else:
                numTry+=1
                if(numTry==10): #If no number works, backtrack to previous edited tile and attempt different value
                    addedList.pop()
                    ind=addedList[-1]
                    numTry=mtx[ind[1]][ind[0]]+1  #Will attempt the next number higher than the previous "correct" value
                    mtx[ind[1]][ind[0]] = 0#addedList.pop()

        else:
            ind[0]+=1
            if ind[0]==9:
                ind[0]=0
                ind[1]+=1
                if ind[1]==9:
                    finished=1
                    print("complete!")
    print(mtx[0])
    print(mtx[1])
    print(mtx[2])
    print(mtx[3])
    print(mtx[4])
    print(mtx[5])
    print(mtx[6])
    print(mtx[7])
    print(mtx[8])


test = [[2,7,1,9,5,4,6,8,3],
        [5,9,3,6,2,8,1,4,7],
        [4,6,8,1,3,7,2,5,9],
        [7,3,6,4,1,5,8,9,2],
        [1,5,9,8,6,2,3,7,4],
        [8,4,2,3,7,9,5,6,1],
        [9,8,5,2,4,1,7,3,6],
        [6,1,7,5,9,3,4,2,8],
        [3,2,4,7,8,6,9,1,5]]

testSubject = [[2,7,1,9,5,4,6,8,0],
                [5,9,3,6,2,8,1,4,0],
                [4,6,0,0,0,7,2,5,0],
                [7,3,6,0,1,5,8,9,0],
                [1,5,9,0,6,2,0,7,4],
                [8,4,0,3,7,9,5,6,1],
                [9,8,5,0,4,0,7,3,6],
                [6,1,7,5,9,3,4,2,8],
                [0,2,0,7,8,6,9,1,5]]


#sudoku(testSubject)




#The following is the set of code for the graphics portion of the code
correcto=[[2,7,1,9,5,4,6,8,3],
        [5,9,3,6,2,8,1,4,7],
        [4,6,8,1,3,7,2,5,9],
        [7,3,6,4,1,5,8,9,2],
        [1,5,9,8,6,2,3,7,4],
        [8,4,2,3,7,9,5,6,1],
        [9,8,5,2,4,1,7,3,6],
        [6,1,7,5,9,3,4,2,8],
        [3,2,4,7,8,6,9,1,5]]
pygame.init()
pygame.display.init()
screen=pygame.display.set_mode([960,850])
pygame.event.get()
screen.fill((200,200,200))
pygame.display.set_icon(pygame.image.load('icon.png'))
one=pygame.image.load("1.png")
two=pygame.image.load('2.png')
three=pygame.image.load('3.png')
four=pygame.image.load('4.png')
five=pygame.image.load('5.png')
six=pygame.image.load('6.png')
seven=pygame.image.load('7.png')
eight=pygame.image.load('8.png')
nine=pygame.image.load('9.png')
tile=pygame.image.load('tile.png')
line1=pygame.Rect(389,50,6,575)
line2=pygame.Rect(581,50,6,575)
line3=pygame.Rect(200,239,575,6)
line4=pygame.Rect(200,431,575,6)
x=0
y=0
completion=0
previousValue=testSubject[0][0]
previousPos=[0,0]
correct=2
pygame.display.set_caption("Sudoku")
pressed = pygame.mouse.get_pressed()[0]
counter=0
highlight=pygame.Rect(1000,0,45,45)   #highlighter
highlightPos=[0,0] #position of the tile you're looking at
while pressed==False:
    screen.fill((200,200,200))
    mousePos=pygame.mouse.get_pos()
    #Leftmost is (210,62), (251,62), (251, 102), (212, 102)
    # tile is height and width of 40, starts at 210, 64 apart
    #208+64*((mousPos[0]-210)//64)
    #highlight.move_ip(208+64,58+64)
    if pygame.mouse.get_pressed()[0]==True:
        if (mousePos[0]-200)//64 <= 8 and (mousePos[0]-200)//64 >= 0 and (mousePos[1]-50)//64 <=8 and (mousePos[1]-50)//64 >=0:
            highlight=pygame.Rect(0,0,45,45)   #highlighter
            highlight.move_ip(208+64*((mousePos[0]-200)//64),58+64*((mousePos[1]-50)//64))
            highlightPos=[(mousePos[0]-200)//64,(mousePos[1]-50)//64]
            if previousPos!=highlightPos:
                if correct!=1:
                    testSubject[previousPos[1]][previousPos[0]]=previousValue
                previousValue=testSubject[highlightPos[1]][highlightPos[0]]
                previousPos=[highlightPos[0],highlightPos[1]]
            #print(highlightPos[1])
            #print(highlightPos[0])
            correct=2
    if correct==1:
        pygame.draw.rect(screen,[90,235,30],highlight)
    elif correct==0:
        pygame.draw.rect(screen,[255,0,0],highlight)
    else:
        pygame.draw.rect(screen,[225,225,30],highlight)
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            #print(event.key)
            if event.key==pygame.K_1:
                testSubject[highlightPos[1]][highlightPos[0]]=1
            elif event.key==pygame.K_2:
                testSubject[highlightPos[1]][highlightPos[0]]=2
            elif event.key==pygame.K_3:
                testSubject[highlightPos[1]][highlightPos[0]]=3
            elif event.key==pygame.K_4:
                testSubject[highlightPos[1]][highlightPos[0]]=4
            elif event.key==pygame.K_5:
                testSubject[highlightPos[1]][highlightPos[0]]=5
            elif event.key==pygame.K_6:
                testSubject[highlightPos[1]][highlightPos[0]]=6
            elif event.key==pygame.K_7:
                testSubject[highlightPos[1]][highlightPos[0]]=7
            elif event.key==pygame.K_8:
                testSubject[highlightPos[1]][highlightPos[0]]=8
            elif event.key==pygame.K_9:
                testSubject[highlightPos[1]][highlightPos[0]]=9
            elif event.key==pygame.K_RETURN:
                if testSubject[highlightPos[1]][highlightPos[0]] == correcto[highlightPos[1]][highlightPos[0]]:
                    correct=1
                else:
                    correct=0
            elif event.key==pygame.K_TAB:
                completion=1
    if completion > 0:
        completion+=1
        if completion >= 7:
            completion=1
            stop=0
            while testSubject[y][x]==correcto[y][x] and stop == 0:
                x+=1
                if x>8:
                    x=0
                    y+=1
                    if y>8:
                        stop=1
                        completion=0
                        x=0
                        y=0
            testSubject[y][x]=correcto[y][x]
    for i in range(0,9):
        for j in range(0,9):
            screen.blit(tile,(200+i*64,50+j*64))
            if testSubject[j][i] == 1:
                screen.blit(one,(206+i*64,56+j*64))
            elif testSubject[j][i] == 2:
                screen.blit(two,(206+i*64,56+j*64))
            elif testSubject[j][i] == 3:
                screen.blit(three,(206+i*64,56+j*64))
            elif testSubject[j][i] == 4:
                screen.blit(four,(206+i*64,56+j*64))
            elif testSubject[j][i] == 5:
                screen.blit(five,(206+i*64,56+j*64))
            elif testSubject[j][i] == 6:
                screen.blit(six,(206+i*64,56+j*64))
            elif testSubject[j][i] == 7:
                screen.blit(seven,(206+i*64,56+j*64))
            elif testSubject[j][i] == 8:
                screen.blit(eight,(206+i*64,56+j*64))
            elif testSubject[j][i] == 9:
                screen.blit(nine,(206+i*64,56+j*64))
    pygame.draw.rect(screen,[0,0,0],line1)
    pygame.draw.rect(screen,[0,0,0],line2)
    pygame.draw.rect(screen,[0,0,0],line3)
    pygame.draw.rect(screen,[0,0,0],line4)
    counter+=1
    if counter==100:
        #print(pygame.mouse.get_pos())
        counter=0
    pressed = pygame.mouse.get_pressed()[2]
    pygame.display.update()
