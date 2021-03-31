a = [5, 8, -5]

for i in a:
  print(i)


for x in range(len(a)):
 print(a[x])


print("=================")


q = [[1,2,3], [4,5,6], [7,8,9], [1,0,1]]
x = [5, 50, 500]
y = "hello"

w = ""

for z in y:
  w = z + w
  print(z)
print(w)

for i in q:
  for z in i:
    print(z, end=" ")
  print()
  







frog = 0
a = [1,5,5,0,2]

for i in a:
   frog =frog * i
print(frog)



basket = [["banana", 2], ["apple", 3], ["raspberry", 6], ["avocado", 0]]
for i in basket:
  print(i)



print("================================================")


# Homework 1: Find product of all elements

a = [1,5,5,0,2]

def multiply (a):  
  total = 1
  for x in a:
     total = total * x
     return total
     
a = [1,5,5,0,2]

print(multiply(a))


print("================================================")
# Homework 2:Find min and max elements from the same array

a = [1,5,5,0,2]

print(min(a))
print(max(a))
 
 