s = b'r\xc3\xa9sum\xc3\xa9'
print(s)
d = s.decode('utf-8')
print(d)
c = d.encode('Latin1')
print(c)
a = c.decode('Latin1')
print(a)