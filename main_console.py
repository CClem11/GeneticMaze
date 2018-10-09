#console version 
from map import Map
from creature import Creature
from pop import Pop
from matplotlib import pyplot as plt

map = Map(width=32, height=18, prob_obstacle=0.07)
number_of_creatures = 40
pop = Pop(map, number_of_creatures)

generations = [i for i in range(50)]
scores = []
average = []

for _ in generations:
	pop.test_generation()
	pop.get_scores()
	best_score = pop.max_score
	average.append(pop.average)
	scores.append(best_score)
	pop.next_generation()
	
plt.plot(generations, scores,label="best_score")
plt.plot(generations, average, label="average_score")
plt.title('score in function of generation')
plt.legend()
plt.show()
	
	


