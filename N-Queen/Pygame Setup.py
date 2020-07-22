import pygame

pygame.init()

Display = pygame.display.set_mode((800,800))

pygame.display.set_caption("Chess-Board")

Display.fill((202,202,202))
pygame.display.update()

boardLength = 8
size=80
cnt=0

image = pygame.image.load('crown (2).png')

for i in range(1,boardLength+1):
    for z in range(1,boardLength+1):
        if cnt % 2 == 0:
            pygame.draw.rect(Display, (255,255,255),[size*z,size*i,size,size])
            print(size*z,size*i,size,size)
            Display.blit(image, ((size*z+5,size*i+5)))
        else:
            pygame.draw.rect(Display, (0,0,0), [size*z,size*i,size,size])
            Display.blit(image, (( size*z +5 ,size*i +5)))
            print(size * z, size * i, size, size)
        cnt +=1
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

