triangles = ["   +   ","  +++  "," +++++ ","+++++++"]
for triangle in triangles:
    print(triangle)

diamonds = ["   +   ","  +++  "," +++++ ","+++++++"]
for diamond in diamonds:
    print(diamond)
diamonds.pop()
diamonds.reverse()
for diamond in diamonds:
    print(diamond)