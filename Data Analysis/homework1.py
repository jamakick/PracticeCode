import numpy as np

array1 = np.random.rand(2,3)

print(array1)
print(array1.shape)
print(array1.dtype)
print()

array1 = array1 + 1

print(array1)
print()
array1 = array1 * [10,20,30]

print(array1)
print()

array1[0] = 22

print(array1)
print()

array2 = np.random.rand(1,10)
array3 = np.random.rand(1,10)

print(array2)
print()
print(array3)
print()

array4 = array3 - array2

print(array4)
print()

print(array4.mean())
print(np.median(array4))
print(np.std(array4))

print(array4[array4 > .2])