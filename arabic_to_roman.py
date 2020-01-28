#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 21:58:59 2020

@author: tysun
"""



def arabic2roman(num):
    arabic = [1,   4,   5,    9,   10,  40, 50,  90, 100,  400,  500, 900,1000]
    roman = ["I","IV", "V", "IX", "X", "XL","L","XC", "C", "CD", "D", "CM", "M"  ]
    if isinstance(num, int):
        res = ''
        i = 12
        if num < 0 or num > 3999:
            return "Error: Number overflow"
        while num > 0:
            while num//arabic[i] > 0:
                res = res + roman[i]
                num = num - arabic[i]
            i-=1
        return res    
    else:
        return "Error: Number type error"
    

