import random
def bogo_sort(a):
	n = len(a)
	sorted_switch = True
	while sorted_switch:

		#swapping   
		i = random.randint(0,n-1)
		j = random.randint(0,n-1)
		a[i],a[j] = a[j],a[i]
		
		yield a,i,j,[]

		#check
		sorted_switch = False
		for i in range(n-1):
			if a[i] > a[i+1]:
				sorted_switch = True
				break
