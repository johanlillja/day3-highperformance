# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 08:54:35 2022

@author: johan
"""

import numpy as np


#a
null_vector_size_10 = np.zeros(10)
null_vector_size_10[4]=1

#b
vector_10_to_49 = np.arange(10,50)

#c
vector49_to_10 = vector_10_to_49[::-1]

#d
mat_3_3 = np.arange(9).reshape((3,3))


#e
e_vector = np.zeros(6)
e_vector[[0,1,4]]=[1,2,4]
zero_index = e_vector==0

#f
rand_30 = np.random.random(30)
mean = np.mean(rand_30)

#e
two_vector = np.zeros((10,2))
two_vector[0] = 1
two_vector[-1]=1

#h

mat_8_8 = np.zeros((8,8))
mat_8_8[1::2,::2] = 1
mat_8_8[::2,1::2] = 1

#i

tile = np.array([[0,1],[1,0]])
tile_mat = np.tile(tile,[4,4])

#j
#arr = arr[ (arr >= 6) & (arr <= 10) ]
Z = np.arange(11)
lt_3 = Z<3
gt_8 = Z>8

Z = Z[lt_3+gt_8]


#k


Z2 = np.random.random(10) #Z2 = np.random.random(10).sort did not work, sad
Z2 = np.sort(Z2)

#i

A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)

true_or_false = A ==B
print(true_or_false)

#m

Z3 = np.arange(10, dtype=np.int32)
print(Z3.dtype)
Z3 = Z3.astype(np.float32)
print(Z3.dtype)

#n

A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diagonal(C)
print(D)

