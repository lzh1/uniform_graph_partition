import random

vertice = 100

def init_graph(g):
	for i in xrange(vertice):
		tmp = []
		for j in xrange(vertice):
			tmp.append(0)
		g.append(tmp)

	for i in xrange(vertice):
		for j in xrange(i):
			g[i][j] = random.randint(1,99)
			g[j][i] = g[i][j]

def init_partition():
	ret = []
	left = []
	right = []
	for i in xrange(vertice):
		if i%2 == 0:
			left.append(i)
		else:
			right.append(i)
	ret.append(left)
	ret.append(right)
	return ret

def calc(g,p):
	ret = 0
	left = p[0]
	right = p[1]
	for i in left:
		for j in right:
			ret += g[i][j]

	return ret

def try_exchange(g,p,i,j):
	left = p[0]
	lv = left[i]
	right = p[1]	
	rv = right[j]

	delta = 0
	for ii in left:
		delta += g[lv][ii]
		delta -= g[rv][ii]

	for ii in right:
		delta -= g[lv][ii]
		delta += g[rv][ii]

	delta += 2 * g[lv][rv]

	if delta<0:
		return 1
	else:
		return 0

def exchange(p,i,j):
	left = p[0]
	lv = left[i]
	right = p[1]	
	rv = right[j]	

	ret = []
	left[i] = rv
	right[j] = lv
	ret.append(left)
	ret.append(right)
	return ret		

def print_g(g):
	for i in g:
		s = ''
		for j in i:
			s += "%2d " % j
		print s

def print_p(p):
	print p[0],p[1]

def main():
	g = []
	init_graph(g)
	partition = init_partition()

	print "initial weight: %d" % calc(g,partition)
	stop = 0
	it = 0
	while stop == 0:
		it += 1
		print "iteration: %d" % it
		find = 0
		for i in xrange(vertice/2):
			for j in xrange(vertice/2):
				ex = try_exchange(g,partition,i,j)
				if ex == 1:
					find = 1
					print "exchanging %d %d" % (partition[0][i],partition[1][j])
					partition = exchange(partition,i,j)
					break
			if find == 1:
				break

		if find == 0:
			stop = 1

	print partition
	print "weight: %d" % calc(g,partition)


main()
