
def next_gap(gap):
	next = max(1,int(gap/1.3))
	return next

def comb_sort(a):
	gap = n = len(a)

	is_sorted = False
	while not is_sorted or gap != 1:

		gap = next_gap(gap)
		is_sorted = True

		for i in range(0,n-gap): 
			yield a, i, i+gap, []
			if a[i]>a[i+gap]:
				a[i],a[i+gap] = a[i+gap],a[i]
				is_sorted = False


 
