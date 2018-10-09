import random

class Creature:
	dna_length = 60
	
	def __init__(self,	pos=[0, 0], dna=[]):
		self.pos = pos
		self.all_positions = [pos]
		if dna:
			self.dna = dna
		else:
			#generate a random one
			self.dna = [random.randrange(4) for _ in range(Creature.dna_length)]
		self.dna_index = 0
		
	def mutation(self, p):
		for i in range(Creature.dna_length):
			if random.randrange(100) <= p*100:
				self.dna[i] = random.randrange(4)
	
	def get_move(self):
		gene = self.dna[self.dna_index]
		self.dna_index += 1
		return gene
		
	def move(self, new_pos):
		self.all_positions.append(new_pos)
		self.pos = new_pos
		
	def get_positions(self):
		return self.all_positions
				
			