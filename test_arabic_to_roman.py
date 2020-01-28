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
    
    
if __name__ == "__main__":
    test_case()   