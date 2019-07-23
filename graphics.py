import pygame

SCREEN_WIDTH = 400
SCREEN_HEIGHT= 400


gameDisplay = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

gameOver = False
clock = pygame.time.Clock()
natureImage = pygame.image.load('nature.jpg')

def natureImg(x,y):
	gameDisplay.blit(natureImage, (x,y))

x = 0
y = 0

while not gameOver:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameOver = True

	gameDisplay.fill((255,255,255))
	natureImg(x,y)

	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()
