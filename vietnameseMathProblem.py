import itertools
answers=[]

stuff = [1,2,3,4,5,6,7,8,9]
for L in range(0, len(stuff)+1):
  for subset in itertools.permutations	(stuff, 9):
    if (subset[0]+13*subset[1]/float(subset[2])+subset[3]+12*subset[4]-subset[5]-11+subset[6]*subset[7]/float(subset[8])-10)==66:
    	answers.append(subset)

print len(answers)
print answers
