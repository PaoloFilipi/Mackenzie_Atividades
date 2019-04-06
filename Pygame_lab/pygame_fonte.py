import pygame


pygame.init()

size = [640, 480]
screen = pygame.display.set_mode(size)
#define um título na janela.
pygame.display.set_caption("Paint")
#troca a cor da janela para branco
screen.fill((0,0,0))
laranja = ( 255,165,0)
fonteTexto = pygame.font.SysFont('Times New Toman ', 50)

fraseTexto = fonteTexto.render("Nintendo Apresenta",True,(255,165,0))
screen.blit(fraseTexto, [200, 200])
pygame.display.flip()
