from matplotlib import pyplot
import random
def visualize(sorting_algo,n):

	a = random.sample(range(1,n+1),n)

	#generating sorting process	
	steps = sorting_algo(a)

	while True:
		frames, h1, h2 ,h3 = next(steps, (None, None, None, None) )

		if frames == None:
			break
		else:
			print(frames)

			# visualize
			bars = pyplot.bar(x = range(1,len(a)+1), height = a)

			
			if h1 != None:
				bars[h1].set_color("red") 
			if h2 != None:
				bars[h2].set_color("orange")
			for h in h3:
				bars[h].set_color("green")

			
			pyplot.axis('off')
			pyplot.pause(0.1)
			pyplot.clf()
			
	pyplot.show()