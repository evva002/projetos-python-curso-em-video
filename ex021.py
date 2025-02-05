import pygame

texto = 'Desafio 021'
print('{:=^30}'.format(texto))

pygame.mixer.init()
pygame.mixer.music.load("caminho do arquivo")
pygame.mixer.music.play()

input("Pressione Enter para parar...")
pygame.mixer.music.stop()

input("Pressione <enter> para encerrar!")