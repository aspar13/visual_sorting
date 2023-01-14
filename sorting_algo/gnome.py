def gnome_sort(a):
	n = len(a)
	i = 1

	while i < n:

		#right

		if a[i] > a[i-1] or i == 0:
			yield a, i,None,[]
			i+=1

		#left
		else:
			yield a,None,i,[]
			a[i], a[i-1] = a[i-1], a[i]
			i -= 1

