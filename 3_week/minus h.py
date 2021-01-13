s = input()
n = s.find('h')
k = len(s) - s[::-1].find('h')
print(s[:n], s[k:], sep='')
