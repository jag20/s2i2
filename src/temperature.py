#! /usr/bin/env python

"""
This is a python module that converts temperatures
"""

def f_to_k(temp_f):
  temp_k = ((temp_f-32)*5./9.)+273.15
  return temp_k

a = float(raw_input('Enter a number: '))
print(f_to_k(a))


