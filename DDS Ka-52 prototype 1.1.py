#This code is open source, and originaly written by 449977, you are free to share it
import pygame
import math
import time
import os
import random
import importlib
import numpy
import sys
import matplotlib.pyplot
import socket

#function to write the user's IP address
def WriteIP():
  heure_local=time.localtime()
  f = open("user_IP_log.txt", "w")
  print('localtime= ',heure_local, file=f)
  print('IP= ', socket.gethostbyname(socket.gethostname()), file=f)
  print('****************************************',file=f)
  f.close()
  

#function to get the user's IP address
def GetIP():
  f = open('user_IP_log.txt', 'r')
  userIP = (f.read())
  print(userIP)
  f.close()

WriteIP()
IP = GetIP()
print(IP)

#screen size
HAUTEUR = 600 #height
LONGEUR =600 #length
SCORE = 2


# we define the RGB colors
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
YELLOW = [255,255,0]
RED = [255, 0, 0]
BLUE = [0 , 0 , 255]
GRAY = (150, 150, 150)


#variables:
APU=0 #1=on, 0=off
GEARS=2 #0=retracted, 1=moving, and 2=extanded


# Initialise la fenêtre de jeu
TailleEcran = [HAUTEUR, LONGEUR]
screen = pygame.display.set_mode(TailleEcran)
pygame.display.set_caption("prototype 1")

# Gestion du rafraichissement de l'écran
clock = pygame.time.Clock()


def draw_window():#on peint sur la fenètre
  screen.fill(WHITE)
  screen.blit(img)
  pygame.display.update()
  return

if __name__ == "__main__":

# The game continues while the user doesn't close the window
	Done = False
	comptage = 0

#load the image(helicopter)
img = pygame.image.load('ka-52.png')
img.convert()

############################################
# Main game loop
while not Done:
  comptage += 1
  SCORE += 1
  event = pygame.event.Event(pygame.USEREVENT)  # recupère la liste des évènements du joueur

  # EVENEMENTS
  # détecte le clic sur le bouton close de la fenêtre
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      Done = True

   # récupère la liste des touches claviers appuyeées sous la forme d'une liste de booléens
  KeysPressed = pygame.key.get_pressed()



    # LOGIQUE
  # movements
  if KeysPressed[pygame.K_LEFT]:
      dirS1 = [-1,0]
      print('left')
  if KeysPressed[pygame.K_RIGHT]:
      dirS1 = [1,0]
      print('right')
  if KeysPressed[pygame.K_UP]:
      dirS1 = [0,-1]
      print('up')
  if KeysPressed[pygame.K_DOWN]:
      dirS1 = [0,1]
      print('down')

  if KeysPressed[pygame.K_p]:
    pygame.display.quit()
    sys.exit()
  
  #helicopter startup:
  if KeysPressed[pygame.K_t]:
    #0=off, 1= on
    if APU==0:
      APU=1 
    else:
      APU=0
#######################################







#collectif, it doesn't have any use right now...

sensivité_du_collectif = 0.5
acceleration_du_joueur = 0
collective_position = 0
thrust = collective_position
# collective_position est positif quand l'helico monte, et negatif quand il descent

def collectif():
  if KeysPressed[pygame.K_z]:
    print('collective up')
    collective_position = collective_position + sensivité_du_collectif

  if KeysPressed[pygame.K_s]:
    print('collective down')
    collective_position = collective_position - sensivité_du_collectif
  return()


