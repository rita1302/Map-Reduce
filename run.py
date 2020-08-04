#!/usr/bin/python3
import pickle
import sys

sim_matr = {}
for line in sys.stdin:
    film_1, film_2, sim = line.strip().split('\t')
    film_1, film_2, sim = float(film_1), float(film_2), float(sim)
    sim_matr[(film_1, film_2)] = sim
   
with open(file='file_big', mode='wb') as f:
    pickle.dump(sim_matr, f)
