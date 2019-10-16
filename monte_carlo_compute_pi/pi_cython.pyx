cimport cython
from libc.stdlib cimport rand, RAND_MAX
#cython: language_level=3

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
def compute_pi(long total):
    cdef int inside = 0
    cdef double rnd_max_dbl = RAND_MAX + 1.0
    cdef double x2, y2, radius, pi
    for i in range(0, total):
        x2 = (rand() / rnd_max_dbl)**2
        y2 = (rand() / rnd_max_dbl)**2
        radius = x2 + y2 # math.sqrt
        if radius <= 1.0:
          inside += 1
    pi = (float(inside) / total) * 4
    return inside, total, pi
