#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

reverse = arr[::-1]

answer = ' '.join("{}".format(n) for n in reverse)
print answer

