# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:53:24 2020

@author: Julien
"""


import numpy as np
import matplotlib.pyplot as plt
import time

#test grid
grid0 = [[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,4,1,9,0,0,5],
         [0,0,0,0,8,0,0,7,9]]


grid = np.array(grid0)#we need an array


"""
changes the values on the guesses on the line,the row and the bloc
it is the interpretation of when you find a new cell, it locks out the value for the corresponding line/row/block
manipulates the global 'guess array'

input x int
intput y int
no output
"""
def discard(x,y):
    #change the value for the line
    for i in range(0,9):
        guess[i,y,grid[x,y]-1] = False
    
    #change the value for the row
    for j in range(0,9):
        guess[x,j,grid[x,y]-1] = False
    
    #change the value for the block
    a,b = x//3*3, y//3*3 #coordinates of the top left corner of the block
    for i in range(3):
        for j in range(3):
            guess[a+i,b+j,grid[x,y]-1] = False


"""
the guess array is a 9x9x9 array wich stores for each cell the authorised and unauthorised values of n in an length-9 boolean filled array
where each boolean stands for the availability of each value

example : guess[5,5] = [False, True, True, False, False, False, False, True, False]
                          1      2     3     4      5      6      7      8     9
so in the 5,5 cell we could put either 2,3 or 8
"""
guess = np.full((9,9,9), True)

#filling the guess array
for x in range(9):
    for y in range(9):
        if grid[x,y]!=0 :
            guess[x,y] = np.arange(1,10)==grid[x,y] #filling the obvious case
            discard(x,y) #discarding the values on other cells


"""
function to call for solving
doesn't find all solutions, only finds one
manipulates the 'grid' array

no input
no output
"""
def solve():
    #searching for a new empty cell
    for x in range(9):
        for y in range(9):
            if grid[x,y]==0 : #cell empty ?
                if len(np.arange(1,10)[guess[x,y]])==1 : #if there's only one value left to guess
                    grid[x,y] = np.arange(1,10)[guess[x,y]][0] #we change the value
                    discard(x,y) #and then we discard all equal values on other cells

t = time.time()
while 0 in grid or time.time()-t > 10 : #we try until the grid is filled or untill too much time passed
    solve()

"""
display of the solution hiding the numbers we already had
"""
plt.imshow(grid-grid0 != 0, cmap = 'gray')
for x in range(9):
    for y in range(9):
        plt.annotate(f'{grid[x,y]}', (x-0.1, y+0.1))

























