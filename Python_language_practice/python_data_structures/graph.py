from graphs.generators import random_graph

G = random_graph([2, 3, 1, 3, 2, 1, 2, 4])

print(G.num_vertices())
print(G.num_edges())

G.symmetrize(method='max')
X = G.isomap(num_dims=2)

G.plot(X, title='Graph embedding')()
