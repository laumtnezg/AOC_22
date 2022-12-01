import sys
fname = sys.argv[1]
elfs = {}
i = 0
elfs[0] = []
with open(fname, 'r') as fhandle:
    for line in fhandle:
        if line == '\n' or line == '':
            i += 1
            elfs[i] = []
        else:
            elfs[i].append(int(line.replace('\n', '')))
total = []
for elf in elfs:
    total.append(sum(elfs[elf]))
print(max(total))
total.sort(reverse = True)
print(sum(total[:3]))