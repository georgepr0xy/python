a = float(input('First side'))
b = float(input('Second side'))
c = float(input('Third side'))
s =(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))** 0.5
print('the area of the triangle is %f' %area)
