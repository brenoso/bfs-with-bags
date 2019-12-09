# -*- coding: utf-8 -*-

from grafo import Grafo
from vertice import Vertice
from bag import Bag
from pennant import Pennant
from bfs import bfs_com_bags, bfs_sem_bags
import time
from os import listdir
from os import path 
isfile, join = path.isfile, path.join

# Testa todas as instâncias do diretório instancias
files = [f for f in listdir("./instancias") if isfile(join("./instancias", f))]
exec_times, exec_times_bags = [], []
for file in files:
    g = Grafo("./instancias/" + file)
    ini_time = time.time()
    bfs_sem_bags(g, g[0])
    fin_time = time.time()
    exec_times.append(fin_time - ini_time)
    
    ini_time = time.time()
    bfs_com_bags(g, g[0])
    fin_time = time.time()
    exec_times_bags.append(fin_time - ini_time)

print(exec_times)
print(exec_times_bags)




