import median

# data structure for a binary tree (from Stack Overflow)
class Tree(object):
	def __init__(self):
		self.left = None
		self.right = None
		self.value = None

# selects element of A with kth greatest value (not the value itself)
def select(A, k):
	value = median.quick_select(A, k)
	for i in range(len(A)):
		if value == A[i]:
			return i

# creates Huffman coding tree for an array A with values 0, 1, ..., m-1
def get_tree(A, m):
	final_t = None
	freq = [0] * m
	for i in A:
		freq[i] = freq[i] + 1
	max_freq = median.quick_select(freq, 4)

	trees = [None] * m
	for i in range(m):
		t = Tree()
		t.value = i
		trees[i] = t

	for i in range(m-1):
		first = select(freq, 1)
		second = select(freq, 2)
		freq[first] = freq[first] + freq[second]
		freq[second] = max_freq * m + 1
		t = Tree()
		t.left = trees[first]
		t.right = trees[second]
		trees[first] = t
		if i == m-2:
			final_t = t

	return final_t

# get codes from a tree
def get_codes(t, codes, prefix):
	if t.value == None:
		get_codes(t.left, codes, prefix + "0")
		get_codes(t.right, codes, prefix + "1")
	else:
		codes[t.value] = prefix

def compress_file(A, m):
	codes = [None] * m
	get_codes(get_tree(A, m), codes, "")
	f = open('outfile', 'w')
	for i in A:
		f.write(codes[i])

def compress_rgb(rgb_tuples):
	A = []
	for i in range(len(rgb_tuples)):
		(r, g, b) = rgb_tuples[i]
		A.append(r)
		A.append(g)
		A.append(b)
	compress_file(A, 256)
