def insertionsort(a):
	n = len(a)

	for i in range(1,n):

		current_element = a[i]

		j = i

		while current_element < a[j-1] and j>=1:
			yield a, i, j, []

			a[j] = a[j-1]

			j-=1

		a[j] = current_element
		yield a,None,j,[i]	