#!/usr/bin/python
# Exercise 9-3
import os

for x,y,z in os.walk(r'/home/'):
  print(z)

