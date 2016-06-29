import copy
a = [1,2,3,"a","b","c"]

b=a 

print(b)
print(a)

print(id(a))
print(id(b))

a.append("d")
print(b)
print(a)

a = [1,2,3,["a","b","c"]]
c = copy.copy(a) #浅拷贝

print(a)
print(c)
print(id(a))
print(id(c))
a.append("d") 
print(a)
print(c)
print(id(a))
print(id(c))

print(id(a[3]))
print(id(c[3]))

d = copy.deepcopy(a) #深拷贝

a[3].append("d")
print(id(a))
print(id(d))
print(a)
print(d)

print(id(a[3]))
print(id(d[3]))

