fin = open('input.txt')
mySet = {}
for line in fin:
    line = line.strip()
    line = line.split()
    for word in line:
        mySet[word] = mySet.get(word, -1) + 1
        print(mySet[word], end=' ')
fin.close()
