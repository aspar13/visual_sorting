def bubble_sort(a):

	n= len(a)
	for i in range(n-2):
		for j in range(n-1-i):

			if a[j] > a [j+1]:
				a[j], a[j+1] = a[j+1], a[j]
				yield a, None,j+1,list(range(n-i,n))
