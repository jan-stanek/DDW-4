import csv
import networkx as nx
import operator

graph = {}

with open('casts.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')

    for row in reader:
        movie = row[1]

        if movie not in graph:
            graph[movie] = []

        graph[movie].append(row[2])

G = nx.Graph()

for movie in graph:
    if movie is '':
        continue

    for actor1 in graph[movie]:
        if actor1 is '':
            continue
        G.add_node(actor1)

        for actor2 in graph[movie]:
            if actor2 is '':
                continue
            G.add_node(actor2)

            if (actor1 is not actor2):
                G.add_edge(actor1, actor2)

dist = {}

sum = 0
count = 0

for u in G:
    if (nx.has_path(G, u, 'Kevin Bacon')):
        d = nx.shortest_path_length(G, u, 'Kevin Bacon')
        dist[u] = d
        sum += d
        count += 1

print(sum / count)

sorted_dist = sorted(dist.items(), key=operator.itemgetter(1))
print(sorted_dist)

sorted_dist.reverse()
print(sorted_dist)

nx.write_gexf(G, "export.gexf")