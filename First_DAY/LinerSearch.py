l=[10,45,85,69,535,455]
t = int(input("Enter your taget number to show it's index:"))
for i in range(len(l)):
    if t == l[i]:
      print("The element found at",i)
      break
