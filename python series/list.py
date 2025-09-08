"""Questions of list"""

"""Print positive and negative elements of an List ."""

l = [-45, 67, 12, -68, -69,34]

print("positive elements are :")
for i in l:
    if i >=0:
        print(i)

print("negative element are :")

for i in l :
    if i < 0:
        print(i)


""" mean of list element """

l = [1,2,113,4,5,6,7,8]

sum = 0

for i in l :
    sum = sum+i

print(sum)

print(sum/len(l))


"""find the greatest element and print its index too"""

l =[12,46,14,19,128,6,13]


gretest =l[0]
index = 0 


for i in range(len(l)):
    if l[i]> gretest:
        gretest = l[i]
        index = i

print(f" your larg number is :{gretest} at indext {index} ")

"""find the second largest number and its index too:"""

l = [12,15,34,56,43,67,87,54,88,99,776,5544,876]

largest = l[0]
sec_largest = l[0]



for i in l:
    if i > largest:
        sec_largest = largest
        largest = i
        

print(f"largest {largest} ,second largest {sec_largest}")

"""check if the list is sorted or not """


a=[1,3,5,6]


for i in range(len(a)-1):
    if a[i] < a[i+1]:
        continue
    else:
        print("your list is not sorted ")
        break

else:
    print("your list is sorted")

