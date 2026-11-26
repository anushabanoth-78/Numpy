import numpy as np
arr =np.arange(1,13)
arr2 =arr.reshape(3,4)
print(arr2)
arr3 =arr.reshape(4,-1)
print(arr3)
arr4 =arr3.flatten()
print(arr4)
