import pygame
import time
pygame.init()
pygame.mixer.init()
com = str(input('Com grandes poderes...?'))
pygame.mixer.music.load('spiderman.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
with open('spidermanText.txt','r') as file:
    for linha in file:
        print(linha.strip())
        time.sleep(0.05)


