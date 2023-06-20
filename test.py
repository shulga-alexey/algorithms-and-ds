from data_structures import Heap

l = [1,2,3]
h = Heap(l)
print(h.data)
l.append(-1)
print(h.data)