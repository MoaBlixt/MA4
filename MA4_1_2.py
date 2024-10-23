
"""
Solutions to module 4
Review date:
"""

student = "Moa"
reviewer = "xxx"

import math as m
import random as r

def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    points = [[r.uniform(-1,1) for _ in range(d)] for _ in range(n)]
    inside_points = sum(1 for point in points if sum(map(lambda x: x**2, point)) <= 1)
    volume = (inside_points / n) * 2**d
    return volume

def hypersphere_exact(d):
    return (m.pi **(d/2) * m.gamma(d/2 +1)) 

def main():
    n_list = [100000, 100000]
    d_list = [2, 11]
    for n,d in zip(n_list, d_list):
        print(f'Approx sphere volume with {n} points and {d} dimensions: {sphere_volume(n,d)}')
        print(f'Exact sphere volume in {d} dimensions: {hypersphere_exact(d)}')


if __name__ == '__main__':
	main()
