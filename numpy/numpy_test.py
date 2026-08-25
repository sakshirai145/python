import numpy as np

#arr = np.array([[10, 20], [30, 40], [50, 60]])

# print(arr)
# print(type(arr))

#a = np.zeros((2,3))
#print(a)

#b = np.ones(3)
#print(b)

#c = np.array([[[1, 2, 3], [4, 5, 6]]])
#print(c)


#d = np.linspace(20,45)
#print(d)

#e = np.empty([2,2])
#print(e)

#f = np.linspace(20,45,7,retstep=True)
#print(f)

g = np.arange(10,20,2)
print(g)

h = np.array([2, 25, 30, 3, 47, 45])
print(type(h))
a=np.sort(h)
print(a)
print(np.concatenate((h, g)))

print(h.shape)

#i = np.array([[1, 2, 3], [4, 5, 6]])
#j = np.array([[7, 8, 9], [10, 11, 12]])
#add = i+j
#print(add)

k = h[np.newaxis, :]
print(k.shape)

l = k.reshape(3,2)


