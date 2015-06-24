# s2i2 first python script

my_atoms = {'hydrogen' : 1, 'helium' : 2, 'lithium' : 3, 'boron' : 4, 'nitrogen' : 5, 'carbon' : 6}

for atom in my_atoms:
  print("Atomic number of " + atom + ": " + str(my_atoms[atom])),
  if my_atoms[atom]%2 == 0:
    print("Atomic number is even")
  else:
    print("Atomic number is odd")
  
