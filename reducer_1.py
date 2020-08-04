#!/usr/bin/python3

import sys
import math

cur_film = None
old_1, old_2 = None, None
up = 0
down_1 = 0
down_2 = 0
for line in sys.stdin:
        if not line:
            continue
        a, b = line.strip().split('\t')
        film1, film2 = a.split(';')
        user_f_1, user_r_1, user_f_2 = b.split(';')
        user_r_2 = user_r_1
        try:
            user_r_1, user_f_1, user_r_2, user_f_2 = float(user_r_1), float(user_f_1),  float(user_r_2), float(user_f_2)
 
        except ValueError:
            continue

        if cur_film is not None:
            if film1 == old_1 and film2 == old_2:
                up +=  (user_f_1 - user_r_1) * (user_f_2 - user_r_2)

                down_1 += (user_f_1 - user_r_1) ** 2
                down_2 += (user_f_2 - user_r_2) ** 2
            else:
                sim = up / (max(math.sqrt(down_1), 1e-8) * max(math.sqrt(down_2), 1e-8))
                if sim > 0:
                    print(old_1 + '\t' + old_2 + '\t' + str(sim))

                up =  (user_f_1 - user_r_1) * (user_f_2 - user_r_2)

                down_1 = (user_f_1 - user_r_1) ** 2	
                down_2 = (user_f_2 - user_r_2) ** 2

                old_1, old_2 = film1, film2

        else:
            up +=  (user_f_1 - user_r_1) * (user_f_2 - user_r_2)

            down_1 += (user_f_1 - user_r_1) ** 2
            down_2 += (user_f_2 - user_r_2) ** 2

            old_1, old_2 = film1, film2

            cur_film = film1


if old_1 is not None and old_2 is not None:
    sim = up / (max(math.sqrt(down_1), 1e-8) * max(math.sqrt(down_2), 1e-8))
    if sim > 0:
        print(old_1 + '\t' + old_2 + '\t' + str(sim))
