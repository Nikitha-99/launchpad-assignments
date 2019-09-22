number = [1,1,2,3,4,64,35,93,35,87,4,3]
a = list()
for i in number:
    if i not in a:
        a.append(i)
  print(a)