import json

detsad = {123456: ('Oleg', 10),
          235457: ('Clone', 10),
          112907: ('Nika', 21),
          132907: ('Veronika', 12),
          150401: ('Vlad', 21)}
with open('file.json', 'w') as w:
    json.dump(detsad, w)
