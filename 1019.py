#!/usr/bin/python

s1 = list(input().upper())
s2 = list(input().upper())
dt = {}



for i in range(len(s1)):
    if i >= len(s2) or  s1[i] != s2[i]:
        try:
            s2.insert(i,'#')
        except:
            s2.append('#')
        if s1[i] not in dt:
            print(s1[i],end='')
            dt[s1[i]] = 1
print()
