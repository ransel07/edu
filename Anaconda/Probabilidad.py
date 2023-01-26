# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from math import comb

n = 3
k = 2

num_comb = comb(n, k)
num_comb2 = comb(5, 2)

prob_A = comb(n, k) / comb(5, 2)

print (num_comb, num_comb2, prob_A*100,"%")

 