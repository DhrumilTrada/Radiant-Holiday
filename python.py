print("Hello , gfdst",end=", ")
print("Boys", end = ",b")
help("keywords")

# A-Z a-z 0-9 and underscore
# name cannot start with a number 
# reserved keywords are not allowed
# int float str 
a = float(input("Enter a number: "))
print(a)
print(type(a))

# seperator by default is space \n
# \n and \t and ..... are escape characters
print("Hello", end = ", ")
print("This is not python")
print("DT\nSDMN", end = " ")
print("DT")

# \u is used for
# r = raw string 
print("C:\\Users\\Username")

a = "Name"
print("Hello",a)
# f = formatted text
print(f"Hello {a}")

l = [1,2,3,4]
print(2 in l)
s = "Hello eorld"
print("hell" in s)
print(type(l))
a = (1,2,3)
print(type(a))

x = "Manav"
print("Manav" if x=="Manav" else "Gandu")
print(4+False)

num = int(input("Enter a number: "))
if num % 2 == 0 :
    print("Even")
else :
    print("Odd")

a = int(input("Enter a three digit number: "))
sum = sum + a % 10
a = int(a / 10)
sum = sum + a % 10
a = int(a / 10)
sum = sum + a % 10
print("Sum is",sum)

year = int(input("Enter a year: "))
if(year%4 == 0 and year%100 != 0 or year%400 == 0):
    print("Leap year")
else:
    print("Not a Leap year")

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = input("Enter operator: ")
if(c == '+'):
    print(a+b)
elif(c == '-'):
    print(a-b)
elif(c == '*'):
    print(a*b)
elif(c == '/'):
    print(a/b)
elif(c == '**'):
    print(a**b)
elif(c == '^'):
    print(a**b)
elif(c == '%'):
    print(a%b)
elif(c == '//'):
    print(a//b)
else:
    print("Enter a valid operator")             

for i in range(10):
    if i%2 == 0:
        print(i,end=" ")
    else:
        print()
        print("Odd")
print()
for i in range(5,10):
    print(i,end=" ")
print()
print()
for i in range(1, 10, 5):
    print(i,end=" ")
print()
print() 
for i in range (10, 0, -1):
    print(i,end=" ")
print()
print()
i=0
while 1:
    print(i,end=" ")
    i = i+1
    if i==10:
        break

for i in range(6):
    for j in range(6-i, 0, -1):
        print("* ",end=" ")
    print()

for i in range(1, 7):
    print(i,end=" ")
else:
    print()
    print("Loop COMPLETED")
    print(i)

for i in range(1, 10000):
    temp = i
    count = 0
    sum = 0
    while temp != 0 :
        count = count+1
        temp = int(temp/10)
    temp = i
    while temp != 0:
        sum = sum + (temp%10)**count
        temp = temp//10
    if(sum == i):
        print(i,end=" ")

for i in range(1, 6):
    for j in range(1, i+1):
        if((i+j) % 2 != 1):
            print("1", end = " ")
        else:
            print("0", end = " ")
    print()