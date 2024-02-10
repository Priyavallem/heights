#python program to print positive numbers in a given range 
lst=[]
n=int(input("enter the size of the list"))
for i in range(0,n):
    e=int(input("enter the element of the list"))
    lst.append(e)
pos = [num for num in lst if num>=0]
print(pos)
