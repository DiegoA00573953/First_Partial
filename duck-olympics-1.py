#Practice round: addition and substraction

def suma(a,b):
  x = a + b
  return x

def resta(a,b):
  x = a - b
  return x

print("give me the first number:")
a = int(input())
print("Give me the secon number:")
b = int(input())
print("la suma da ", suma(a,b), "y la resta da", resta(a,b))



#First round
#multiplication and division
def multiplication(a,b):
  x = a * b
  return x

def division(a,b):
  x = a / b
  return x
print("Give me the first number:")
a = int(input())
print("Give me the second number:")
b = int(input())
print("The multiplication give",multiplication(a,b), "The division gives",division(a,b))

#Second round
#Unit conversion
def conversion(kilometers,meters):
  meters = kilometers * 1000
  return meters
print("give me the kilomenters and I will make it into meters")
kilometers = int(input())
meters = kilometers * 1000
print("this are the meters", conversion(kilometers,meters))

# Third round
#Triangle area
def triangle_area(base, height):
  area = (base*height)/2
  return area
print("give me the base")
base = int(input())
print("give me the height")
height = int(input())
print("The area should be", triangle_area(base, height))
