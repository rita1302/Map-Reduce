#!/usr/bin/python3

import sys
import pickle

f1 = open('all_films_big.txt')

lst = []
for line in f1:
    arr = line.strip().split('\t')
    for elem in arr:
        lst.append(elem)
        
with open(file='file_big', mode='rb') as f2:
    a = pickle.load(f2)

name = {}
f3 = open('movies.dat', encoding='cp1251')

for line in f3:
    film_id, film_name, _ = line.strip().split('::')
    name[film_id] = film_name

d = {}
val = {}
cur_user = None
for line in sys.stdin:
    user, film_id, film_rate = line.strip().split('\t')
    
    film_rate  = float(film_rate)
    
    if user == cur_user:
        d[film_id] = film_rate
    else:
        if cur_user:
            #считаем
            for f in lst:
                if f in d:
                    continue
                else:
                    metric_1 = 0
                    metric_2 = 0
                    for f_rated in d:
                        if (float(f), float(f_rated)) in a:
                            metric_1 += a[(float(f), float(f_rated))] * d[f_rated]
                            metric_2 += a[(float(f), float(f_rated))]
                        elif (float(f_rated), float(f)) in a:
                            metric_1 += a[(float(f_rated), float(f))] * d[f_rated]
                            metric_2 += a[(float(f_rated), float(f))]
                            
                    if metric_2 != 0:
                        val[f] = metric_1 / (metric_2)
                        val[f] = min(val[f], 5)

            t_d = []
            for key in val:
                t_d.append((float(val[key]),str(name[key])))

            t_d.sort(key=lambda x: (-x[0], x[1]))

            print(cur_user + '\t' + str(t_d[0][1]) + '\t' + str(t_d[0][0]) + '\t' + str(t_d[1][1]) + '\t' +str(t_d[1][0]) + '\t' +str(t_d[2][1]) + '\t' + str(t_d[2][0]))
            
            d = {}
            val = {}
            cur_user = user
            
            d[film_id] = film_rate            
            
        
        else:
            d[film_id] = film_rate
            cur_user = user
            
            
if cur_user:
    #считаем
    for f in lst:
        if f in d:
            continue
        else:
            metric_1 = 0
            metric_2 = 0
            for f_rated in d:
                if (float(f), float(f_rated)) in a:
                    metric_1 += a[(float(f), float(f_rated))] * d[f_rated]
                    metric_2 += a[(float(f), float(f_rated))]
                elif (float(f_rated), float(f)) in a:
                    metric_1 += a[(float(f_rated), float(f))] * d[f_rated]
                    metric_2 += a[(float(f_rated), float(f))]
            if metric_2 != 0:             
                val[f] = metric_1 / (metric_2)
                val[f] = min(val[f], 5)

    t_d = []
    for key in val:
        t_d.append((float(val[key]), name[key]))

    t_d.sort(key=lambda x:(-x[0], x[1]))

    print(cur_user + '\t' + str(t_d[0][1]) + '\t' + str(t_d[0][0]) + '\t' + str(t_d[1][1]) + '\t' +str(t_d[1][0]) + '\t' +str(t_d[2][1]) + '\t' + str(t_d[2][0]))
