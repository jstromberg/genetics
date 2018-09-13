import random
import datetime
import engine.chromosone as c
	
class GeneticBase():
	GENE_SET = ''
	TARGET = ''
	def __init__(self):
		super(GeneticBase, self).__init__()
		self.startTime = datetime.datetime.now()
	def getFitness():
		return false
	def _generateParent(self):
		genes = []
		targetLength = len(self.TARGET)
		while len(genes) < targetLength:
			sampleSize = min(targetLength - len(genes), len(self.GENE_SET))
			genes.extend(random.sample(self.GENE_SET, sampleSize))
		genes = ''.join(genes)
		fitness = self.getFitness(genes)
		return c.Chromosone(genes, fitness)
	def _mutate(self, chromosone):
		index = random.randrange(0, len(chromosone.genes))
		childGenes = list(chromosone.genes)
		newGene, alternate = random.sample(self.GENE_SET, 2)
		childGenes[index] = alternate if newGene == childGenes[index] else newGene
		genes = ''.join(childGenes)
		fitness = self.getFitness(genes)
		return c.Chromosone(genes, fitness)
	def _display(self, chromosone, count):
		timeDiff = datetime.datetime.now() - self.startTime
		print("{}\t{}\t{}\t{}".format(count, chromosone.genes, chromosone.fitness, timeDiff))
	def run(self):
		count = 1
		random.seed()
		bestChromosone = self._generateParent()
		self._display(bestChromosone, count)

		while True:
			count += 1
			childChromosone = self._mutate(bestChromosone)
			self._display(childChromosone, count)
			if bestChromosone.fitness >= childChromosone.fitness:
				continue
			if childChromosone.fitness >= len(self.TARGET):
				break
			bestChromosone = childChromosone
		