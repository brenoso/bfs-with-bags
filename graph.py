from collections import defaultdict 
  
# Representacao de um grafo direcionado
# usando representaç~~ao de lista de adjacencias
class Graph: 
  
    # Construtor
    def __init__(self): 
  
        # dicionario default para armazenar o grafo
        self.graph = defaultdict(list) 
  
    # função que adiciona um vértice no grafo
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    #Funcao de busca em largura que imprime os nós visitados
    def BFS(self, s): 
  
        # marcar todos os vértices como não visitados
        visited = [False] * (len(self.graph)) 
  
        # Criar uma fila para a busca em largura
        queue = [] 
  
        #Marca o primeiro nó como visitado e o enfilera 
        queue.append(s) 
        visited[s] = True
  
        while queue: 
  
            #Desenfileira um nó e imprime o mesmo
            s = queue.pop(0) 
            print (s)

            ##pegar todas as vizinhaças do vertice que foi desinfileirado. Se algum vizinho não foi visitado
            # marque como visitado e enfileira o mesmo
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True