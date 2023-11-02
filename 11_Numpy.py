import numpy as np


# ## 1
# ## Try this.
# import numpy as np
# 
# y = np.array([1, 3, 5, 6, 12, 32])
# print(y)


# ## 2
# ## Try this.
# import numpy as np
# 
# x = np.array([1, 3, 5, 6, 12, 32])
# print(x)
# print(x.dtype)
# 
# y = np.array([1.26, 5.0, 1.1])
# print(y)
# print(y.dtype)

## 3
## Try this.
# import numpy as np
# 
# y = np.linspace(0, 5, 10, endpoint=True)
# print(y)

## 4
# ## Try this to create the same array as the previous example with endpoint=False
# import numpy as np
# 
# y = np.arange(0, 5, .5)
# print(y)

## 5
## Try this.
# import numpy as np
# 
# y = np.linspace(0, 5, 10, endpoint=False)
# print(y)
# print(y.dtype)

## 6
# ## Try this.
# import numpy as np
# 
# y = np.linspace(0, 5, 10, endpoint=False, dtype=int)
# print(y)

## 7
# ## Try this.
# x = np.array([3, 9, 18])  
# y = np.array([64, 7, 12])  
# z = np.concatenate([x, y])
# print(z)
# 
# import numpy as np

## 8
# x = 5
# y = 6
# print(x == y)

## 9
# x = 5
# y = 5
# print(x == y)

## 10
# x = [1, 2, 3]
# y = [1, 2, 4]
# print(x == y)


## 11
## this will give an error; look at #12 below for correct way
# x = np.array([3, 9, 18])
# y = np.array([64, 7, 12])
# if x == y:
#      print("same")
# else:
#      print("different")


## 12
## This works
# x = np.array([1, 2, 3])
# y = np.array([1, 2, 4])
# print(x == y)
# areAllEqual = (x == y).all()
# print(areAllEqual)


## 13
## Using the > comparison operator
# x = np.array([3, 2, 1])
# y = np.array([5, 0, 4])
# print(x > y)


## 14
## Another example
# x = np.array([4, 3, 1])
# print(x > 2)





























