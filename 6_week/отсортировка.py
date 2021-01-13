inputFile = open('input.txt', 'r', encoding='utf-8')
outputFile = open('output.txt', 'w', encoding='utf-8')
d = []
for pupil in inputFile:
    d.append(pupil.strip())
d.sort(key=lambda person: person.split()[0])
for pupil in d:
    print(pupil.split()[0],
          pupil.split()[1],
          pupil.split()[3], file=outputFile)
outputFile.close()
inputFile.close()
