print("HELLO WORLD")
a = input("Enter a Name:")
print("ALL THE BEST",a)
b = int(input("enter first number:"))
c = int(input("enter second number:"))
e = int(input("enter third number:"))
add = b+c
average = b+c+e
print("Average",average)
print("Add",add)
d = "Shubman Gill" 
e = 45
f = 78.5
g = True
print(type(d))
print(type(e))
print(type(f))
print(type(g))
s={10,23,34,54,56}
h = int(input("enter the element:"))
s.add(h)
print("updated sets:",h)


x = int(input("enter first number:"))
y = int(input("enter second number:"))
print(x>y)
print(x<y)

n = [24,45,56,67,78]
b = int(input("enter the value:"))
n.append(b)
print("updated list:",b)

def greet():
    "this functions greeting message"
    print("Welcome to python")
    print(greet.__doc__)

num = int ( input("enter the number:"))
square = num*num
print("Square=",square)

#1.using the temporary variable ( swamp)
a = int(input("enter the no:"))
b = int(input("enter the no:"))
tem=a
a=b
b=tem
print("After the swapping:")
print("a=",a)
print("b=",b)

#2.without using the varible
a = int(input("enter the no:"))
b = int(input("enter the no:"))
a,b=b,a
print("After the swapping:")
print("a=",a)
print("b=",b)

student = {"Name":"Tanvi","Age":17,"Course":"BSC.DSAI","Dream":"AI Engineer"}
print(student)

v = int(input("enter no in ur mind:"))
if v%2==0 :
    print("even")
elif v%3==0 :
    print("odd")
else:
    print("zero")

code = input("enter the string:")
upper__text = code.upper()
lower__text = code.lower()
print("Upper",upper__text)
print("lower",lower__text)
length = len(code)
print("Length od code",length)

 

 #n = int(input("enter no:"))
#for i in range (1,16):
 print(n,"x",i,"=",n*i)

# o = input("enter the initial:")
 #print("I LOVE YOU",o)

i = 34
while i<=40:
    print(i)
    i = i + 1