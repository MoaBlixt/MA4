
"""
Solutions to module 4
Review date:
"""

student = "Moa"
reviewer = "xxx"

import math as m
import random as r
from time import perf_counter as pc
from concurrent.futures import ProcessPoolExecutor 



def sphere_volume(n, d):
    points = [[r.uniform(-1,1) for _ in range(d)] for _ in range(n)]
    inside_points = sum(1 for point in points if sum(map(lambda x: x**2, point)) <= 1)
    volume = (inside_points / n) * 2**d
    return volume

def hypersphere_exact(d):
    return (m.pi **(d/2) * m.gamma(d/2 +1)) 

# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
    n_list = [n] * np 
    d_list = [d] * np 
    with ProcessPoolExecutor() as ex:
        results = list(ex.map(sphere_volume, n_list, d_list))
    return sum(results) / len(results)

# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
    d_list = np * [d]
    n_list = [n//np for _ in range(np)]
    with ProcessPoolExecutor() as ex: 
        result = ex.map(sphere_volume, n_list, d_list)
    results = list(result)
    return sum(results) / len(results)


def main():
    # part 1.1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11
    np = 10
    
    print('Started')
    start_time = pc()
    for y in range (np):
        sphere_volume(n,d)
    end_time = pc()
    print(f'Time to run {np} sequential: {round(end_time - start_time)} seconds \n')
    
    # part 1.2 --  parallel using def parallel 1 
    n = 1000000
    start_time = pc()
    volume = sphere_volume_parallel1(n,d,np)
    print(f'volume of sphere: {volume}')
    end_time = pc()
    print(f'Time to run paralell: {round(end_time - start_time)} seconds\n')

    start_time = pc()
    volume = sphere_volume_parallel2(n,d,np)
    print(f'Volume of sphere 2: {volume}')
    end_time = pc()
    print(f'Time to run parallel 2: {round(end_time - start_time)} seconds')






if __name__ == '__main__':
	main()
