from creature import Creature
import numpy as np
import random

def distance(pos1, pos2):
	return np.linalg.norm( np.array(pos1) - np.array(pos2) )

class Pop:
	def __init__(self, map, number=50):
		self.nb = number
		self.map = map
		start_point = map.get_start()
		self.creatures = [Creature(pos=start_point) for _ in range(self.nb)]
		
		#gene = 0, 1, 2 or 3 -> up, down , right, left
		#move x axis and y axis
		self.move_x = [0, 0, 1, -1]
		self.move_y = [-1, 1, 0, 0]
		
	def get_creatures(self):
		return self.creatures
		
	def move(self): 
		index = self.creatures[0].dna_index
		if index == Creature.dna_length:
			# print("you should create new creatures as those ones are dead (not enough genes)")
			return False
		else:
			for c in self.creatures:
				x, y = c.pos
				gene = c.get_move()
				x, y = x+self.move_x[gene], y+self.move_y[gene]
				# print(self.map.correct_position(x, y))
				if self.map.correct_position(x, y):
					c.move((x, y))
				#else we don't move the creature
				
			return True
				
	def get_scores(self):
		"return an array of selected creatures (matching index)"
		#let's evaluate our creatures
		goal = self.map.get_end()
		# print("score function : end pos : ", goal)
		max_distance = distance(goal, self.map.get_start())
		scores = []
		mini = 9999
		best_index = 0
		for i, c in enumerate(self.creatures):
			positions = c.get_positions()
			distances_list = [distance(goal, p) for p in positions]
			min_d = min(distances_list)
			if min_d < mini:
				mini = min_d
				best_index = i
			mean_distance = np.mean(distances_list)
			scores.append(mean_distance)
			# score *= (len(positions) - distances_list.index(min_d))	#amplification
			# scores.append(min_d)
		
		# print("min distance achieved :", mini)
		self.max_score = scores[best_index]
		self.best_index = best_index
		self.average = np.mean(scores)
		#fitness function
		scores = [1/(1+s-min(scores)) for s in scores]
		# scores = [np.exp(max(0, 1 - 1/max_distance*s)) for s in scores]
		#normalization
		scores = np.array(scores)
		scores = scores/sum(scores)
		return scores
		
	def pick_parent(self, scores):
		r = random.random() #between 0 and 1
		index = 0
		while r > scores[index]:
			r -= scores[index]
			index += 1
		return self.creatures[index]
			
	def child_dna(self, parent1, parent2):
		dna = []
		for i in range(len(parent1.dna)):
			if random.randrange(2):
				dna.append(parent1.dna[i])
			else:
				dna.append(parent2.dna[i])
		return dna
		
	def next_generation(self):
		start_point = self.map.get_start()
		nb_random_creatures = 3
		scores = self.get_scores()
		new_creatures = [Creature(pos=start_point) for _ in range(nb_random_creatures)]
		for _ in range(self.nb-nb_random_creatures):
			dna = self.child_dna(self.pick_parent(scores), self.pick_parent(scores))
			child = Creature(pos=start_point, dna=dna)
			child.mutation(0.02)
			new_creatures.append( child )
		self.creatures = new_creatures
		
	def test_generation(self):
		for _ in range(Creature.dna_length):
			self.move()
			
	def get_best_creature(self):
		self.get_scores()
		return self.creatures[self.best_index]
		
			
			