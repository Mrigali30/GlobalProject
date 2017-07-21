import numpy as np
a=[[1,2],[3,4],[1,2]]
b=[[1,2],[5,6]]

print list(set(map(tuple,a+b)))