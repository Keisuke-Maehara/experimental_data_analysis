fin = open('input.txt','r')

i = 1
for line in fin:
    line = line.rstrip()
    print(line)
    i += 1

fin.close()
