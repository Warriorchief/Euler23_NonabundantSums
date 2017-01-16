#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 17:28:32 2016

@author: christophergreen

Non-abundant sums
Problem 23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that
 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called
 abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be
 written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown 
 that all integers greater than 28123 can be written as the sum of two abundant numbers. However, 
 this upper limit cannot be reduced any further by analysis even though it is known that the greatest
 number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import math;

def find_sum_prop_factors(x):
    factors=[];
    i=1;
    while i<math.ceil((x/2)+1):
        if x%i==0:
            factors.append(i);
        i+=1;
    tot=0;
    for f in factors:
        tot+=f
    return tot;
    
abundants=[];
k=11;
while k<28123:
    if k%1000==0:
        print("trying",k,"...");
    if find_sum_prop_factors(k)>k:
        abundants.append(k);
    k+=1;
#print(len(abundants)); #--> 6965

sum2abundants=[];
p=0;
while p<len(abundants):
    if p%100==0:
        print("passing through p being",p,"out of 6965");
    q=0;
    while q<len(abundants):
        if abundants[p]+abundants[q]<28123:
            sum2abundants.append(abundants[p]+abundants[q]);
        q+=1;
    p+=1;  

sum2nodupes=set(sum2abundants); #<-------- set() method VERY HELPFUL 
print("sum2nodupes has length",len(sum2nodupes));  #-->26666

output=0;
z=0;
while z<28123:
    if z%100==0:
        print("passing through z being",z,"out of 28123");
    if z not in sum2nodupes:
        output+=z;
    z+=1;

print("the answer to this question should be",output); #--> 4179871 CORRECT

