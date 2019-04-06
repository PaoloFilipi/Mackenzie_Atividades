import pygame
import math

pygame.init()

def linha(corLinha,xi,yi,xf,yf,width):
  
  colorRect = corLinha
  pygame.draw.line(screen,colorRect,[xi,yi],[xf,yf],width )
  pygame.display.flip()

def Segmentolinha(corLinha,xi,yi,xin,yin,xf,yf,width):
  
  colorRect = corLinha
  pygame.draw.lines(screen,colorRect,True,([xi,yi],[xin,yin],[xf,yf]),width)
  pygame.display.flip()

def retangulo(corLinha,xi,yi,tam,larg,xf,yf,width):
  
  colorRect = corLinha
  pygame.draw.rect(screen,colorRect,(xi,yf,tam,larg), width)
  pygame.display.flip()

def poligono(corLinha,a,b,c,d,e,f,width):

  colorRect = corLinha
  pygame.draw.polygon(screen, colorRect,( [a, b],[b, c],[c, d], [d, e], [e, f],[f, a]),width )
  pygame.display.flip()

def circulo(corLinha,xcentral,ycentral,raio,width):

    colorRect = corLinha
    pygame.draw.circle(screen, colorRect, (xcentral,ycentral),(raio),width)
    pygame.display.flip()

def elipse(corLinha,xi,yi,xf,yf,width):
    
    colorRect = corLinha
    pygame.draw.ellipse(screen, colorRect, ([xi,yi],[xf,yf]),width)
    pygame.display.flip()

def corDaFigura(escolhaCor):
    
    if( escolhaCor == 1):
        cor = (255,0,0)
        pygame.display.flip()
    if(escolhaCor == 2):
        cor = (0,255,0)
        pygame.display.flip()
    if(escolhaCor == 3):
        cor = (0,0,255)
        pygame.display.flip()
    if(escolhaCor == 4):
        cor = (0,0,0)
        pygame.display.flip() 
    return cor

size = [400, 300]
screen = pygame.display.set_mode(size)
#define um título na janela.
pygame.display.set_caption("Paint")
#troca a cor da janela para branco
screen.fill((255,255,255))
status = True
while True: 
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:                    
      if event.key == pygame.K_q:
        retangulo(corDaFigura(3),40,50,60,80,80,100,9)
      if event.key == pygame.K_w:
        retangulo(corDaFigura(3),60,80,60,80,100,120,9)
      if event.key == pygame.K_e:
        elipse(corDaFigura(1),90,110,130,180,9)
      if event.key == pygame.K_r:
        elipse(corDaFigura(1),110,160,90,110,9)
      if event.key == pygame.K_t:
        poligono(corDaFigura(2),45,55,65,75,85,95,9)
      if event.key == pygame.K_y:
        circulo(corDaFigura(2),80,70,90,9)  
      if event.key == pygame.K_ESCAPE:
        pygame.quit()
         
  pygame.display.update()

pygame.display.flip()
