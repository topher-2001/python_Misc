import time
import sys

width = 40

sys.stdout.write("[%s]" %(" " * width))
sys.stdout.flush()
sys.stdout.write("\b" * (width + 1))

for i in xrange(width):
	time.sleep(0.1)
	sys.stdout.write("-")
	sys.stdout.flush()

sys.stdout.write("]\n")
