import random

class Map:
	def __init__(self, width, height, prob_obstacle=0.1):
		self.width, self.height = width, height
		self.create_map(prob_obstacle)
		
	def create_map(self, p):
		# 0 is empty and 1 is obstacle
		self.map = [[int(random.randrange(100) <= p*100) for _ in range(self.height)] for _ in range(self.width)]	#list of columns
		self.start = random.randrange(self.width//4), random.randrange(self.height//4)
		self.end = random.randrange(3*self.width//4, self.width), random.randrange(3*self.height//4, self.height)
		self.set_start_end_points(self.start, self.end)
		
	def get_start(self):
		return self.start
	def get_end(self):
		return self.end
		
	def set_end(self, pos):
		self.map[self.end[0]][self.end[1]] = 0
		self.end = pos
		self.map[pos[0]][pos[1]] = 3
	
	def set_start_end_points(self, start_point, end_point):
		x1, y1 = start_point
		x2, y2 = end_point
		#2 is the starting point and 3 the arrival
		self.map[x1][y1] = 2
		self.map[x2][y2] = 3
		
	def correct_position(self, x, y):
		"return if the position (x, y) is correct"
		# not an obstacle and in the map
		return (0 <= x < self.width) and (0 <= y < self.height) and self.map[x][y] != 1 
			
	def get_map(self):
		return self.map
