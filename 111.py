import copy
import numpy
data = [1,2,3,4,5,6]
b = [[1,2,3],[4,5,numpy.nan]]
print(numpy.mean(b))
a = copy.deepcopy(b)
print(a)
a.extend (b)
print(a)
c = []
c.append('1')
print(c)

#a = [[] for _ in range(3)]
#print(a)