( hint: heron's formula is given as: area = sqrt(s*(s-a)*(s-b)*(s-c)))
  a = float(input("enter the first side of the triangle : "))
  b = float(input("enter the second side of the tringle : "))
  c = float(input("enter the third side of the trongle : "))
  print(a,b,c)
  s = (a+b+c)/2
  area = (s*(s-a)*(s-b)*(s-c))
  print("area = " +str(area))
