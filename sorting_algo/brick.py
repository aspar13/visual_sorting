def brick_sort(a):
	n = len(a)
	is_sorted = False

	while not is_sorted:

		for i in range(0,n-1,2):
			yield a,i,None,[]
			if a[i] > a[i+1]:
				a[i], a[i+1] = a[i+1], a[i]
				is_sorted = False

		is_sorted = True	

		for i in range(1,n-1,2):
			yield a,None,i,[]
			if a[i] > a[i+1]:
				a[i], a[i+1] = a[i+1], a[i]
				is_sorted = False
	

