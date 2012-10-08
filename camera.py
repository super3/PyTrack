#Webcam IR mouse control 1.0
#K.B. Carte Aug. 10, 2009
#Works only with an IR filter on the webcam.
#To do this simply cut out the black part of a film
#negitave, and place two or three layers over the lens
#of the webcam.
######################################################
#----------imports and global variabl assignment------
######################################################
from VideoCapture import Device
import Image, sys, pygame
from ctypes import *
import ImageOps
from PIL import ImageEnhance
from pygame.locals import *
cam = Device()
user = windll.user32
res = (1440,900) #set to the resolution of the screen
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('IR Mouse Control')
font = pygame.font.SysFont("Curier",26)
#---------------functions-----------------------
################################################

#Returns the xy cordinets of the ir dot.
#Doesn't return exact dot, only the first TRUE pixel value
def xy(im):
  imxy = im.getprojection()
  imx = imxy[0]
  imy = imxy[1]
  x = imx.index(1)
  y = imy.index(1)
  return (x,y)
#Decides if a 'click' was called.
#Returns 1 or 0 and size in pixels of the ir dot
#Still in testing stage =/
def irclk(im):
  yn = 0
  xi = 0
  yi = 0
  irxy = im.getprojection()
  irx = irxy[0]
  iry = irxy[1]
  for i in irx:
    if i == 1:
      xi +=1
  for i in iry:
    if i == 1:
      yi += 1
  xyi = xi + yi
  if xyi >= 100:#***
    yn = 1
  else: yn = 0
  return (yn,xyi)
#-----------Main loop--------------------
#########################################
while 1:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
    
  try:
    imt = cam.getImage()
    im = imt.resize(res)
    im = ImageOps.mirror(im)
    im1 = ImageEnhance.Contrast(imt).enhance(1.0)
    im1 = ImageEnhance.Brightness(imt).enhance(1.5)
    x,y = xy(im)
    user.SetCursorPos(x,y)
    name = font.render('By K.B. Carte', True, (250,250,250))
    web = font.render('Webcam IR mouse control : 1.0.1', True, (250,250,250))
    fil = font.render('Works only with an IR filter on the webcam lens', True, (250,250,250))
    yn = irclk(im1)
    xyi = yn[1]
    num = font.render("IR intensity:" + str(xyi), True, (250,250,250))
    if yn[0] ==1:
      cl = 'click'
    else: cl = '' 
    clik = font.render(cl, True, (250,250,250))
    im1 = pygame.image.frombuffer(im1.tostring(), (640,480), "RGB")
    
    screen.blit(im1, (0,0))
    screen.blit(name,(0,26))
    screen.blit(web,(0,0))
    screen.blit(fil,(0,52))
    screen.blit(clik,(0,104))
    screen.blit(num, (0,78))
    pygame.display.flip()
                      
  except ValueError:   #A value error is raised when it can't see the IRLED.
    pass               #So we ignor it.
                       #I'm trying to maybe control the 'click' with the except
                       #So the click will be a lack of the ir light
                       #Still testing...