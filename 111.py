import copy

data = [1,2,3,4,5,6]
b = [[1,2,3],[4,5,6,7]]
a = copy.deepcopy(b)
print(a)
a.extend (b)
print(a)


#a = [[] for _ in range(3)]
#print(a)