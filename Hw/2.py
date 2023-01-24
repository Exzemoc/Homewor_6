a = "First sting"
b = "Second string"
c = "Third string"
d = "Fourth string"
with open('file.txt', 'w') as w:
    w.write(a + '\n' + b)
with open('file.txt', 'a') as a:
    a.write('\n' + c + '\n' + d)
