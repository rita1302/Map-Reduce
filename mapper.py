#!/usr/bin/python3

import sys

if __name__ == '__main__':

    for line in sys.stdin:
        if not line:
            continue

        words = line.strip().split('::')

        print(words[0] + '\t'+ words[2])
