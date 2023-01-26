# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from math import comb
from itertools import combinations
from itertools import product
from matplotlib_venn import venn2
#import matplotlib.pyplot as plt

d = 2
nd = 3

num_comb = comb(nd, d)
num_comb2 = comb(5, 3)
d_comb = list(combinations(range(1,6), 2))


#prob_A = com

#for i in d_comb:
#   print (i)

list_blood = ["A", "B", "AB", "O"]
Ph = ["+", "-"]

d_comb_blood = list(product(list_blood, Ph))

comb_dic = dict()

for s in d_comb_blood:
    comb_dic[s[0]] = s[1]


venn2(comb_dic, ("Tipo de sangre","Rh"))











