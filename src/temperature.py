#! /usr/bin/python

"""
This is a python module that converts temperatures
"""

def f_to_k(temp_f):
  return ((temp_f-32)*5./9.)+273.15

def k_to_c(temp_k):
  return temp_k - 273.15

def f_to_c(temp_f):
  temp_k = f_to_k(temp_f)
  return k_to_c(temp_k)

a = float(raw_input('Enter a number: '))
print(f_to_c(a))


