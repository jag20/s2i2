# second exercise s2i2

#read file into memory one line at a time
#f = open("yob2013.txt", "r")
#for line in f
#reads the whole file into memory
#  i = 0
#  for line in list_of_lines: 
#    line = line.strip()
#    i += 1
#    if i > 10:
#      print(line)
  
import matplotlib.pyplot as plt
with open("yob2013.txt", "r") as f:
  list_of_lines = f.readlines()

  #my name
  print("Exercise 1")
  target_name = "john"
  for line in list_of_lines: 
    line = line.split(',')
    if line[0].lower() == target_name:
      if line[1].lower() == 'm':
        print("The boy's name 'John' occurs " + str(line[2]) + " times")
      elif line[1].lower() == 'f':
        print("The girl's name 'John' occurs " + str(line[2]) + " times")
      else:
        print("Unknown gender on line: ")
        print line
        break
  
  #longest names
  print("")
  print("Exercise 2")
  name = ['m','f']
  length = [0,0]
  for line in list_of_lines: 
    line = line.split(',')
    if line[1].lower() == 'm' and len(line[0]) > length[0]:
      name[0] = line[0]
      length[0] = len(line[0])  
    if line[1].lower() == 'f' and len(line[0]) > length[1]:
      name[1] = line[0]
      length[1] = len(line[0]) 
  male_names = []
  female_names = []
  for line in list_of_lines: 
    line = line.split(',')
    if line[1].lower() == 'm' and len(line[0])  == length[0]:
      male_names.append(line[0])
    if line[1].lower() == 'f' and len(line[0])  == length[0]:
      female_names.append(line[0])
  
  print("The longest male names are " + str(length[0]) + " letters long.")
  for item in male_names:
    print item
  print("")
  print("The longest female names are " + str(length[1]) + " letters long.")
  for item in female_names:
    print item

  print("")
  print("Exercise 3")
  common_male = 'm'
  times_male = 0
  common_female = 'f'
  times_female = 0
  for line in list_of_lines: 
    line = line.strip()
    line = line.split(',')
    if line[1].lower() == 'm' and int(line[2]) > times_male:
      common_male = line[0]
      times_male = int(line[2])
    elif line[1].lower() == 'f' and int(line[2]) > times_female:
      common_female = line[0]
      times_female = int(line[2])

  print("Most common names")
  print("Males: " + common_male + " occurs " + str(times_male) + " times.")
  print("Females: " + common_female + " occurs " + str(times_female) + " times.")

  print("")
  print("Exercise 4")
  male = {}
  female = {}
  count = [0,0]
  for line in list_of_lines: 
    line = line.strip()
    line = line.split(',')
    if line[1].lower() == 'm':
      male[line[0]] = line[2]
    elif line[1].lower() == 'f':
      female[line[0]] = line[2]

#  for mname in male:
#    for fname in female:
#      if mname == fname:
#        print mname
#        print fname
#        count[0] += int(male[mname])
#        count[1] += int(female[fname])
#        print(count)
  print("males with unisex names = " + str(count[0]))
  print("females with unisex names = " + str(count[1]))

  print("")
  print("Exercise 5")
  male = {}
  female = {}
  count = [0,0]
  for line in list_of_lines: 
    line = line.strip()
    line = line.split(',')
    if line[1].lower() == 'm':
      male[line[0]] = line[2]
    elif line[1].lower() == 'f':
      female[line[0]] = line[2]
  #get variance
  #get average usage per name
  mcount = len(male)
  fcount = len(female)
  mnum = 0
  fnum = 0
  for mname in male:
    mnum += int(male[mname]) 
  for fname in female:
    fnum += int(female[fname]) 
  #average usage
  mavg = float(mnum)/float(mcount)
  favg = float(fnum)/float(fcount)
  #get variance
  mvar = 0
  fvar = 0
  for mname in male:
    mvar += (float(male[mname])-mavg)**2  
  mvar = mvar/(mcount-1) 
  for fname in female:
    fvar += (float(female[fname])-favg)**2  
  fvar = fvar/(fcount-1) 
  print('Variances: ')
  print('Male: ' + str(mvar))
  print('Female: ' + str(fvar))
  
  plt.figure()
  i = 0
  lst = [0]*len(male)
  stff = [0]*len(male)
  for item in male: 
    lst[i] = i
    stff[i] = int(male[item])
    i += 1
  plt.plot(lst,stff)
  plt.xlabel("Name")
  plt.ylabel("Occurances")
  plt.show()

