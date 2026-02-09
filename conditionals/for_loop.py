#using range()
for i in range(1,7):
    print(i)

#loop through a list
fruits=["apple","banana","mango"]
for fruit in fruits:
     print(fruit)

#loop through a string
for ch in "bangtan":
     print(ch)

#loop through characters
char="demonslayer"
for str in char:
     print(str)

#using for loop if
for i in range(1,11):
     if i%2==0:
         print(i)

#for loop with else

for i in range(3):
     print(i)
else:
     print("loop finished")

#nested
for i in range(1,4):
     for j in range(1,3):
          print(i,j)
