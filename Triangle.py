#3

def triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False


a = float(input('Please enter length of side a : '))
b = float(input('Please enter length of side b : '))
c = float(input('Please enter length of side c : '))


if triangle(a, b, c):
    print(" Triangle is valid ")
else:
    print(" Triangle is NOT valid ")