from time import time
import random
import pi_cython as run

def run_pi_using_python(total):
    inside = 0
    for i in range(0, total):
        x2 = random.random()**2
        y2 = random.random()**2
        radius = x2 + y2
        if radius <= 1.0:
            inside += 1
    pi = (float(inside) / total) * 4
    return inside, total, pi

def run_pi_using_cython(total):
    inside, total, pi = run.compute_pi(total)
    return inside, total, pi

def main():
    start_time = time()

    total = 1000000
    print("Computing pi using python...")
    inside_python, total_python, pi_python = run_pi_using_python(total)
    time_python = time()
    elapsed_time_python = round(time() - start_time, 3)
    print("Pi value is {}. You hitted the dart target {} times from an amount of {} times. Elapsed time in python: {} seconds".format(pi_python, inside_python, total_python, elapsed_time_python))
    
    print("Computing pi using cython...")
    inside_cython, total_cython, pi_cython = run_pi_using_cython(total)
    time_cython = round(time() - time_python, 3)
    print("Pi value is {}. You hitted the dart target {} times from an amount of {} times. Elapsed time in cython: {} seconds".format(pi_cython, inside_cython, total_cython, time_cython))

main()
