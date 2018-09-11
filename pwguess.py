import random
import datetime

class PasswordGuesser():
	GENE_SET = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
	TARGET = "Hello World!"
	"""docstring for passwordGuesser"""

	def __init__(self):
		super(PasswordGuesser, self).__init__()
		self.startTime = datetime.datetime.now()

	def generateParent(self):
		genes = []
		count = 0
		length = len(self.TARGET)
		while len(genes) < length:
			count += 1
			sampleSize = min(length - len(genes), len(self.GENE_SET))
			sub = random.sample(self.GENE_SET, sampleSize)
			genes.extend(sub)
		return ''.join(genes)
	
	def getFitness(self, guess):
		return sum(1 for expected, actual in zip(self.TARGET, guess)
			if expected == actual)

	def mutate(self, parent):
		index = random.randrange(0, len(parent))
		childGenes = list(parent)
		newGene, alternate = random.sample(self.GENE_SET, 2)
		childGenes[index] = alternate if newGene == childGenes[index] else newGene
		return ''.join(childGenes)

	def display(self, guess, fitness, count):
		timeDiff = datetime.datetime.now() - self.startTime
		print("{}\t{}\t{}\t{}".format(count, guess, fitness, timeDiff))

	def run(self):
		count = 1
		random.seed()
		bestParent = self.generateParent()
		bestFitness = self.getFitness(bestParent)
		self.display(bestParent, bestFitness, count)

		while True:
			count += 1
			child = self.mutate(bestParent)
			childFitness = self.getFitness(child)
			if bestFitness >= childFitness:
				self.display(child, childFitness, count)
				continue
			if childFitness >= len(self.TARGET):
				break
			bestFitness = childFitness
			bestParent = child
		self.display(child, childFitness, count)

pg = PasswordGuesser()
pg.run()
