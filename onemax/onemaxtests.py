import unittest
import datetime
from engine.genetic import GeneticBase as g

class OneMaxTests(unittest.TestCase):
	def test(self, length=100):
		geneset = [0,1]		