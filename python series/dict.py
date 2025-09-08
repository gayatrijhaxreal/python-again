"""Write a Python script to merge two Python dictionaries"""

d1 ={1:100,20:200,40:300}
d2 ={4:400,50:500,60:600}

for i in d2:
    d1[i] = d2[i]
print(d1)
"""Write a Python program to sum all the values in a dictionary"""

d1 ={1:100,20:200,40:300}

sum = 0

for i in d1:
    sum = sum + d1[i]

print(sum)

"""Count the frequency in a list of each elements"""

a =[1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,7,8]

d={1:3,2:3,3:3}


if i in a: 
    if d.keys():
        d[i] = d[i]+1
    else:
        d[i] = 1
print(d)

"""Write a Python program to combine two dictionary by adding
values for common keys"""

d1 ={1:100,20:200,40:300}
d2 ={4:400,50:500,60:600}
for i in d2:
    if i in d1.keys():
        d1[i] = d2[i] 
    else:
        d1[i] = d2[i]
print(d1)