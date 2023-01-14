def cocktail_sort(a):
	n = len(a)
	is_sorted = False
	start, end = 0,n-1
	while not is_sorted:

		is_sorted = True
		for i in range(end):
			if a[i] > a[i+1]:
				a[i],a[i+1] = a[i+1], a[i]
				is_sorted = False
				yield a,i+1,None,[]
		
		end -=1

		if is_sorted:
			break

		for i in range(end-1,start-1,-1):
			if a[i] > a[i+1]:
				a[i],a[i+1] = a[i+1], a[i]
				is_sorted = False
				yield a,None,i,[]
		
		start +=1

