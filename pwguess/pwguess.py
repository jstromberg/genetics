from engine.benchmark import Benchmark as b
from engine.genetic import GeneticBase as g

class PasswordGuesser(g):
	GENE_SET = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
	TARGET = "slkdjfhaslkejfhELKFJHASELFKJASEFLKJsheFLKJSHFEKJSDFSD"
	"""docstring for passwordGuesser"""

	def __init__(self):
		super(PasswordGuesser, self).__init__()

	
	def getFitness(self, guess):
		return sum(1 for expected, actual in zip(self.TARGET, guess)
			if expected == actual)



pg = PasswordGuesser()
b.run(pg.run)
