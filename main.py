import pygame
pygame.init()
from map import Map
from creature import Creature
from pop import Pop

def show_map_creatures(window, map, creatures):
	width, height = int(window[0]/len(map)), int(window[1]/len(map[0]))
	#show the creatures
	for c in creatures:
		show_creature(map, c.pos)
	#show the map
	show_map(window, map)
	
def show_map(window, map):
	width, height = int(window[0]/len(map)), int(window[1]/len(map[0]))
	for x, column in enumerate(map):
		for y, value in enumerate(column):
			colors = [(0, 0, 0), (100, 100, 100), (0, 255, 0), (255, 0, 0)]		# for each type of bloc
			if value != 0:
				pygame.draw.rect(game_display, colors[value], (x*width, y*height, width, height))

def show_creature(map, pos):	
	width, height = int(window[0]/len(map)), int(window[1]/len(map[0]))
	r = int(1/2*width*0.9)	#radius
	color = (0, 0, 255)
	x, y = pos
	pygame.draw.circle(game_display, color, (x*width+r, y*height+r), r)
	
window = (1600, 900)
if window == (1600, 900):
	game_display = pygame.display.set_mode(window, pygame.FULLSCREEN)
else:
	game_display = pygame.display.set_mode(window)

#Initilization of some classes
width, height = 32, 18
map = Map(width=width, height=height, prob_obstacle=0.07)
number_of_creatures = 30
pop = Pop(map, number_of_creatures)

# 	Main Loop
clock = pygame.time.Clock()
fps = 50
show_all_creatures = True
loop_state = True
while loop_state:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loop_state = False
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			loop_state = False
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				show_all_creatures = not show_all_creatures
				print("you changed the view mode")
				
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				p = event.pos
				x, y = int(p[0]*width/window[0]), int(p[1]*height/window[1])
				map.set_end((x, y))
				# print("new end location : ", x, y)
	
	if not show_all_creatures:
		pop.test_generation()
		best_creature = pop.get_best_creature()
		pop.next_generation()
		
		if loop_state:
			#show the best creature of that generation
			for pos in best_creature.get_positions():	
				show_creature(map.get_map(), pos)
				show_map(window, map.get_map())
				clock.tick(fps)
				pygame.display.update()
				game_display.fill((0, 0, 0))
	
	else:
		# show all creatures:
		if not pop.move():
			pop.get_scores()
			print("best score : ", pop.max_score)
			pop.next_generation()
		show_map_creatures(window, map.get_map(), pop.get_creatures())
		clock.tick(fps)
		pygame.display.update()
		game_display.fill((0, 0, 0))
	
#to close properly pygame
pygame.quit()
