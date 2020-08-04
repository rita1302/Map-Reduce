#!/usr/bin/python3
import sys

for line in sys.stdin:
    line = line.strip()
    
    if not line:
        continue
       
    words = line.split('::')
    
    try:
        words[0] = float(words[0])
        
    except ValueError:
        continue
        
    print(str(words[0]) + '\t' + words[1] + '\t' + words[2])
        
    
