#!/usr/bin/env python

from calc import Calculator

def assertAlmostEqual(a,b):
    assert round(a-b, 7)==0, "{} is not equal to {}.".format(a,b)

c1 = Calculator()

