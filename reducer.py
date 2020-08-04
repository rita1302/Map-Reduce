#!/usr/bin/python3

import sys

if __name__ == '__main__':
	current_user = None
	current_count = 0
	user = None
	k = 0

	for line in sys.stdin:
		line = line.strip()

		user, rate = line.split('\t', 1)
		try:
			rate = float(rate)
		except ValueError:
			continue

		if current_user == user:
			current_count += rate
			k += 1
		else:
			if current_user:
				print(str(current_user) + '\t' + str(current_count / k))

			current_count = rate
			current_user = user
			k = 1

	if current_user == user:
		print(str(current_user) + '\t' + str(float(current_count) / k))

