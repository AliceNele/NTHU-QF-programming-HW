# -*- coding: utf-8 -*-
"""
Created on Tue May  5 15:23:04 2020

@author: ASUS
"""
#Lab1
class Specialist:
    def __init__(self,m):
        self.m = m
        
    def __sub__(self,other):
        ans = []
        
        for i in range(0,len(self.m)):
            ans.append(self.m[i] - other.m[i])
        return ans
a = Specialist([1,2,3])
b = Specialist([3,4,5])
c = a - b
print(c)
#==============================================================================















   


