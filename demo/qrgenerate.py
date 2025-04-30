class WeightedUndirectedGraph:
    def __init__(self, n):
        self.n = n
        self.adj_list = {i: [] for i in range(n)}
    
    def add_edge(self, u, v, w):
        self.adj_list[u].append((v, w))
        self.adj_list[v].append((u, w))  # Undirected edge

def compute_scc(g, W):
    d = DisjointForests(g.n)
    for i in range(g.n):
        d.make_set(i)
    
    # Process edges with weight ≤ W and union their vertices
    for u in g.adj_list:
        for v, w in g.adj_list[u]:
            if w <= W and u < v:  # u < v to avoid processing both (u,v) and (v,u)
                d.union(u, v)
    
    return d.dictionary_of_sets()


g3 = UndirectedGraph(8)
g3.add_edge(0,1,0.5)
g3.add_edge(0,2,1.0)
g3.add_edge(0,4,0.5)
g3.add_edge(2,3,1.5)
g3.add_edge(2,4,2.0)
g3.add_edge(3,4,1.5)
g3.add_edge(5,6,2.0)
g3.add_edge(5,7,2.0)
res = compute_scc(g3, 2.0)
print('SCCs with threshold 2.0 computed by your code are:')
assert len(res) == 2, f'Expected 2 SCCs but got {len(res)}'
for (k, s) in res.items():
    print(s)
    
# Let us check that your code returns what we expect.
for (k, s) in res.items():
    if (k in [0,1,2,3,4]):
        assert (s == set([0,1,2,3,4])), '{0,1,2,3,4} should be an SCC'
    if (k in [5,6,7]):
        assert (s == set([5,6,7])), '{5,6,7} should be an SCC'

        
# Let us check that the thresholding works
print('SCCs with threshold 1.5')
res2 = compute_scc(g3, 1.5) # This cutsoff edges 2,4 and 5, 6, 7
for (k, s) in res2.items():
    print(s)
assert len(res2) == 4, f'Expected 4 SCCs but got {len(res2)}'

for (k, s) in res2.items():
    if k in [0,1,2,3,4]:
        assert (s == set([0,1,2,3,4])), '{0,1,2,3,4} should be an SCC'
    if k in [5]:
        assert s == set([5]), '{5} should be an SCC with just a single node.'
    if k in [6]:
        assert s == set([6]), '{6} should be an SCC with just a single node.'
    if k in [7]:
        assert s == set([7]), '{7} should be an SCC with just a single node.'
        
print('All tests passed: 10 points')
