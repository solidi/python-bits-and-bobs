import multiprocessing as mp
import dill
from math import cos
import pathos.multiprocessing as mp

p = mp.Pool(2)
p.map(lambda x: 2**x, range(10))
print(p.map(cos, range(10)))
dill.dump(lambda x: x**2, open('dillfile', 'wb'))
