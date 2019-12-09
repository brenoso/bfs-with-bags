# -*- coding: utf-8 -*-

from vertice import Vertice

class Grafo:
    def __getitem__(self, key):
            vertices = list(self.vertices.values())
            return vertices[key]

    
    def __init__(self, path):
        self.qtd_vertices = 0
        self.qtd_arestas = 0
        self.tipo = "" # directed or undirected
        self.vertices = {} # dicionario de vertices do grafo
        self.adj = {}  # lista de adjacencias (um dicionario)
        with open(path, 'r') as arq_entrada:
            linha = arq_entrada.readline() 
            linha = arq_entrada.readline()
            self.qtd_vertices = int(linha)
            linha = arq_entrada.readline()
            self.qtd_arestas = int(linha)
            linha = arq_entrada.readline()
            self.tipo = linha
            linha = arq_entrada.readline()
            linha = arq_entrada.readline()

            while linha:
                linha = linha.split()
                v1, v2 = linha[0], linha[1]
                if v1 not in self.vertices:
                    self.vertices[v1] = Vertice(v1)
                    self.adj[self.vertices[v1]] = []
                if v2 not in self.vertices:
                    self.vertices[v2] = Vertice(v2)
                    self.adj[self.vertices[v2]] = []

                self.adj[self.vertices[v1]].append(self.vertices[v2])
                if self.tipo == 'undirected':
                    self.adj[self.vertices[v2]].append(self.vertices[v1])

                linha = arq_entrada.readline()
        


    def get_vertices(self):
        return list(self.vertices.values())