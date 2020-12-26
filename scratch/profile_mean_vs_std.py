from line_profiler import LineProfiler
import numpy as np


def mean_and_std(a):
    np.mean(a)
    np.std(a)


def main():
    a = np.random.normal(size=(1000, 1000))
    for i in range(1000):
        mean_and_std(a[i])


lp = LineProfiler()
lp.add_function(mean_and_std)
lp.runcall(main)
lp.print_stats()
