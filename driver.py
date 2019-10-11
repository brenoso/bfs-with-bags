# Driver code
from graph import Graph

# Criar um grafo
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print ("Abaixo os nós imprimidos a partir de um vértice de inicio") 
g.BFS(2) 