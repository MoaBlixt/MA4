
"""
Solutions to module 4
Review date:
"""

student = "Moa"
reviewer = "_"


import random as r
import matplotlib.pyplot as plt 

def approximate_pi(n):
    nc = 0
    c_inside = []
    c_outside = []
    for i in range(n):
        x = r.uniform(-1,1)
        y = r.uniform(-1,1)
        if x**2 + y**2 <= 1:
            c_inside.append((x,y))
            nc += 1
        else: 
            c_outside.append((x,y))

    pi = 4*(nc/n)
    return pi, c_inside, c_outside
    


def plot(n, c_inside, c_outside):
    if c_inside:
        plt.scatter(*zip(*c_inside), color='red', s=1)
    if c_outside:
        plt.scatter(*zip(*c_outside), color='blue', s=1)
    plt.axis('square')
    plt.title(f'n = {n}')
    plt.show()


def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        pi, c_inside, c_outside = approximate_pi(n)
        print(f'Estimatied pi with {n} points: {pi}')
        plot(n, c_inside, c_outside)

if __name__ == '__main__':
	main()
