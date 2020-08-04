#!/usr/bin/python3

import sys

r = {}
for line in sys.stdin:
    user_id, rate = line.strip().split('\t', 1)

    user_id = float(user_id)
    rate = float(rate)

    r[user_id] = rate # нужно только для вывода

d = {}
f = open('ratings.dat')
for l in f:
    l = l.strip()
    if not l:
        continue

    words = l.split('::')

    try:
        words[0] = float(words[0])#id
        words[1] = float(words[1])#movie_id
    except ValueError:
        continue
            
    if not words[0] in r:# если вдруг не было такого пользователя
        continue
    a, b, c, _ = words
    
    if b not in d:#если еще нет такого фильма
        d[b] = {}        
    d[b][a] = c # присваиваем рейтинг фильму

for i, a in d.items():
    for j, b in d.items():
        if i  >= j:
            continue
        for user in a.keys():
            if user in b:
               print( str(i) + ';' + str(j) + '\t' + str(a[user]) + ';'  +str(r[user]) +';' +  str(b[user]))

