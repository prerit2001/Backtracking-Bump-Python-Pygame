import pygame
import sys

N = int(input('Please Enter N For a Matrix of ( N x N ) '))

pygame.init()

Display = pygame.display.set_mode((800,800))

pygame.display.set_caption("Chess-Board")

Display.fill((202,202,202))
pygame.display.update()

boardLength = N
size=80
cnt=0

image = pygame.image.load('crown (2).png')


Chess = list()

for _ in range(N) :
    Chess.append(0)

for _ in range(N) :
    Chess[_] = list()
    for i in range(N) :
        Chess[_].append(0)

Left_diogonal = list ()
Right_diogonal = list ()
Coloumn_check = list ()

for _ in range(100000) :
    Left_diogonal.append(0)
    Right_diogonal.append(0)
    Coloumn_check.append(0)

def Solve(Chess_Borad,Coloumn) :

    if Coloumn >= N :
        return True


    for Current_Position in range(N) :
        if Coloumn_check[Current_Position] == 0 :
            if Right_diogonal[Current_Position + Coloumn] == 0 :
                if Left_diogonal[Current_Position - Coloumn + N - 1] == 0 :

                    Chess_Borad[Current_Position][Coloumn] = 1
                    Coloumn_check[Current_Position] = 1
                    Right_diogonal[Current_Position + Coloumn] = 1
                    Left_diogonal[Current_Position - Coloumn + N - 1] = 1




                    if Solve(Chess_Borad,Coloumn+1) :
                        return True

                    Chess_Borad[Current_Position][Coloumn] = 0
                    Coloumn_check[Current_Position] = 0
                    Right_diogonal[Current_Position + Coloumn] = 0
                    Left_diogonal[Current_Position - Coloumn + N - 1] = 0



    return False

Solve(Chess,0)

for i in range(N) :
    for j in range(N) :
        print(Chess[i][j],end=" ")
    print()

for i in range(1,boardLength+1):
    for z in range(1,boardLength+1):
        if cnt % 2 == 0:
            pygame.draw.rect(Display, (255,255,255),[size*z,size*i,size,size])
            if Chess[i-1][z-1] == 1 :
                Display.blit(image, ((size*z+5,size*i+5)))
        else:
            pygame.draw.rect(Display, (0,0,0), [size*z,size*i,size,size])
            if Chess[i-1][z-1] == 1 :
                 Display.blit(image, (( size*z +5 ,size*i +5)))
        cnt +=1
    if N % 2 == 0:
        cnt-=1


pygame.draw.rect(Display,(50,100,200),[size,size,boardLength*size,boardLength*size],1)

pygame.display.update()
gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True


pygame.quit()
quit()