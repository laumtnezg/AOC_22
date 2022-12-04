import sys
import string
#fname = sys.argv[1]
fname = "/Users/lmartinezg/Documents/CNIO/AOC_22/data/day3.txt"
score = 1
alphabet = {}
bags = {}
for element in list(string.ascii_letters):
    #print(element)
    alphabet[element] = score
    score += 1
counter = 0
with open(fname, 'r') as fhandle:
    for line in fhandle:
        line = line.replace("\n", "")
        wheresplit = (len(line)/2 )
        bags[counter] = []
        bags[counter].append(line[:wheresplit])
        bags[counter].append(line[wheresplit:])
        counter += 1
total_sum = 0
for bag in bags:
    for element in bags[bag][0]:
        if element in bags[bag][1]:
            total_sum = total_sum + alphabet[element]
            break
print(total_sum)

#2nd part
bags_two = {}
counter = 1
counter_groups = 0
bags_two[0] = []
with open(fname, 'r') as fhandle:
   for line in fhandle:
    line = line.replace("\n", "")
    if counter == 3:
        bags_two[counter_groups].append(line)
        counter_groups += 1
        counter = 1
        bags_two[counter_groups] = []
        continue
    bags_two[counter_groups].append(line)
    counter += 1
#print(bags_two)
total_two = 0
for bag in bags_two:
    for element in bags_two[bag][0]:
        if element in bags_two[bag][1] and element in bags_two[bag][2]:
            #print(element)
            total_two = total_two + alphabet[element]
            print(total_two)
            break