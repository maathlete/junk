#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 19:52:58 2021

@author: owllegs
"""

def gcd(a,b):
    u = 1
    g = a
    x = 0
    y = b
    
    while y > 0:
        q = g//y
        t = g % y 
        s = u - (q*x)
        u = x
        g = y
        x = s
        y = t 
    
    v = (g - (a*u))/b
    return(g, u, v)
