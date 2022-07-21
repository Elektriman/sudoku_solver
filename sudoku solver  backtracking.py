# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:16:44 2020

@author: Julien
"""

import numpy as np
import matplotlib.pyplot as plt

#test grid
grid= [[7,3,6,1,0,9,8,0,0],
       [0,9,0,0,8,0,0,0,7],
       [0,4,0,7,3,0,9,0,0],
       [3,2,4,6,1,7,5,8,9],
       [6,7,0,0,0,0,0,0,1],
       [0,8,1,0,0,0,4,7,6],
       [0,1,7,0,9,0,6,0,0],
       [2,6,0,0,7,0,0,9,0],
       [0,5,0,2,6,0,7,0,8]]

grid = np.array(grid)#we need a numpy array
res = [] #store multiple possibles result grids in a List

"""
returns if the element n can be placed at the position (x,y)

input x int
input y int
input n int
return boolean
"""
def is_possible(x,y,n):
    
    #verify the line
    for a in grid[:,y] :
        if a==n :
            return False
    
    #verify the column
    for b in grid[x,:]:
        if b==n : 
            return False
    
    #verify the bloc
    a,b = x//3*3,y//3*3 #coordinates of the top left corner of the block
    for i in range(3):
        for j in range(3):
            if grid[a+i,b+j]==n :
                return False
    
    #if all tests passed then n is possible
    return True

"""
procedure to call for solving
it manipulates the global array 'grid' with aliasing
finds all the solutions using backtracking and recursion

no input
no output
"""
def solve():
    #seraching for an unfilled cell
    for x in range(9):
        for y in range(9):
            if grid[x,y]==0 : #if unfilled
                for n in range(1,10):
                    if is_possible(x,y,n): #verify possibility
                    
                        #case yes : change the value
                        grid[x,y]=n
                        
                        solve() #try continuing with the new modified grid
                        
                        #if we stepped out of the function it means we failed to complete the sudoku so be do backtracking
                        grid[x,y]=0
                        
                return #case where we can't fill a cell
    
    #case where we have a solution
    global res
    res.append(grid.copy()) #adding a copy to the results list


solve()

"""
display of the first solution hiding the numbers we already had
"""
# plt.imshow(res[0]-grid != 0)
# for x in range(9):
#     for y in range(9):
#         plt.annotate(str(res[0][x,y]), (x-0.1, y+0.1))

print(res)

M = np.full((9,9,3), 0.7)

for i in range(9):
    for j in range(9):
        plt.text(i-0.1,j-0.1,str(res[0][i,j]))
        if grid[i,j]==0 :
            M[i,j]=(1,)*3
plt.imshow(M)
plt.xlim(-1,9)
plt.ylim(-1,9)
plt.xticks([])
plt.yticks([])






















