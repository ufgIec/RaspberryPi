import RPi.GPIO as GPIO, time, os

DEBUG = 1
GPIO.setmode(GPIO.BCM)

def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(0.1)
 
        GPIO.setup(RCpin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        return reading

import sys,pygame
pygame.init()

size = width,height = 600,400
speed = [4,4]
black = 0,0,0
skyblue = 0,231,252

screen = pygame.display.set_mode(size)

bird1 = pygame.image.load("bat1.png")
bird2 = pygame.image.load("bat2.png")
pipe = pygame.image.load("pipe1.png")
gameover = pygame.image.load("game-over.jpg")
gameover = pygame.transform.scale(gameover,(width,height))
gameoverrect = gameover.get_rect()

bird1height = bird1.get_height()
#make the bird smaller
bird1 = pygame.transform.scale(bird1,(int(bird1.get_height()*0.6),int(bird1.get_height()*0.6)))
bird2 = pygame.transform.scale(bird2,(int(bird2.get_height()*0.6),int(bird2.get_height()*0.6)))
bird1rect = bird1.get_rect()
print bird1rect
bird1rect.x = 20
piperect = pipe.get_rect()
pipestartx = 600
pipestarty = 0
piperect.x, piperect.y = pipestartx, pipestarty

# set up the fonts

fontObj = pygame.font.Font('freesansbold.ttf',40)

class pipe():
	def __init__(self,startx,position = "top",pipeHeight = 200):
		self.sprite = pygame.image.load("pipe1.png")
		self.sprite = pygame.transform.scale(self.sprite,(50,pipeHeight))
		self.rect = self.sprite.get_rect()
		self.rect.x = startx
		
		if position == "top":
			self.rect.y = 0
		else:
			self.sprite = pygame.transform.rotate(self.sprite,180)
			self.rect.y = height - self.sprite.get_height()
			
# This creates all the pipes
pipelist = []
pipelist.append(pipe(200,"top",220))
pipelist.append(pipe(200,"bottom",90))
pipelist.append(pipe(600,"top",140))
pipelist.append(pipe(600,"bottom",190))
pipelist.append(pipe(800,"bottom",100))
pipelist.append(pipe(800,"top",220))
pipelist.append(pipe(1000,"top",100))
pipelist.append(pipe(1000,"bottom",220))
pipelist.append(pipe(1200,"top",280))
pipelist.append(pipe(1200,"bottom",50))

count = 0
costume = 1
def GameOver(score):
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
		screen.fill(black)
		textSurfaceObj = fontObj.render(("You scored... " + str(score)),True,skyblue)	
		textRectObj = textSurfaceObj.get_rect()
		textRectObj.center = (width/2,height/2)
		screen.blit(gameover,gameoverrect)
		screen.blit(textSurfaceObj,textRectObj)
		pygame.display.flip()

running = True
score = 0
hitcount= 0
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	screen.fill(skyblue)
	# Move the bird
	bird1rect.y = ((3*bird1rect.y) + (height - int(RCtime(18)/2) +10))/4 #talk to the sensor and calculate the bird height

	if bird1rect.y > (height - bird1height): bird1rect.y = height - bird1height
	if bird1rect.y < 0: bird1rect.y = 0
	# move and blit the pipes
	for pipe in pipelist:
		screen.blit(pipe.sprite,pipe.rect)
		pipe.rect.x -= 3
		if pipe.rect.x <-200:
			pipe.rect.x = 1000
	oldcount = hitcount
	for pipe in pipelist:
		if pipe.rect.colliderect(bird1rect):
			hitcount +=1
			print hitcount
			if hitcount >=3:
				GameOver((score/5))
				running = False
	if oldcount == hitcount:
		hitcount = 0

	# animate the bird
	if count > 5:
		count = 0
		if costume == 1: costume = 2
		else: costume =1
	if costume == 1:
		screen.blit(bird1,bird1rect)
		costume = 2
	else:
		screen.blit(bird2,bird1rect)
		costume = 1
	pygame.display.flip()
	count +=1
	score +=1