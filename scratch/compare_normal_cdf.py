from scipy.stats import norm
from scipy.special import erf
from numpy import sqrt
from time import time

print("The scratch folder is a place to try out random things without fear of polluting the rest of the code base.")
print("This typically includes (1) testing whether something does what you think it should.")
print("or (2) profiling two different ways of doing things.")

x = .1
nruns = 10000

start = time()
for _ in range(nruns):
    a = norm.cdf(x)
print(f"First method took {time() - start} seconds.")

start = time()
for _ in range(nruns):
    a_ = (1 + erf(x/sqrt(2))) / 2
print(f"Second method took {time() - start} seconds.")

print(a)
print(a_)
