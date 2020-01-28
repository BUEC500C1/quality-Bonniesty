#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 23:32:08 2020

@author: tysun
"""

import arabic_to_roman as test
import pytest

def test_case():
    assert test.arabic2roman(3) == "III"
    assert test.arabic2roman(1) == "I"
    assert test.arabic2roman(10) == "X"
    assert test.arabic2roman(9) == "IX"
    assert test.arabic2roman(40) == "XL"
    assert test.arabic2roman(1000) == "M"
    assert test.arabic2roman(100) == "C"
    assert test.arabic2roman(400) == "CD"
    assert test.arabic2roman(500) == "D"
    assert test.arabic2roman(5) == "V"
    assert test.arabic2roman(4) == "IV"
    assert test.arabic2roman(7) == "VII"
    assert test.arabic2roman(2013) == "MMXIII"
    assert test.arabic2roman(1975) == "MCMLXXV"
    assert test.arabic2roman(3999) == "MMMCMXCIX"    
    
    
if __name__ == "__main__":
    test_case()   
