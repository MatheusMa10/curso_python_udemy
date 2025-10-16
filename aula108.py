# count é um iterador sem fim
from itertools import count

count1 = count(10, 8)
range1 = range(10, 100, 8)

print('count1', hasattr(count1, '__iter__'))
print('count1', hasattr(count1, '__next__'))
print('range1', hasattr(range1, '__iter__'))
print('range1', hasattr(range1, '__next__'))

print('count')
for i in count1:
    if i > 100:
        break

    print(i)
print()

print('range')
for i in range1:
    print(i)
