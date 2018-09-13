import time
import statistics
import sys

class Benchmark:
	"""docstring for Benchmark"""
	@staticmethod
	def run(function):
		timings = []
		stdout = sys.stdout
		for i in range(100):
			startTime = time.time()
			sys.stdout = None
			function()
			sys.stdout = stdout
			seconds = time.time() - startTime
			timings.append(seconds)
			mean = statistics.mean(timings)
			print("{} {:3.2f} {:3.2f}".format(1 + i, mean, statistics.stdev(timings, mean) if i > 1 else 0))