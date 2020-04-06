"""
This Python file (main.py) is the driver program for 'distributions.py' 
and 'visualisations.py' modules, and was created by Sagar Mukherjee, 
as part of the Final Project.

It tests the functionalities of all the methods defined.

At first, working of pseudo-random number generation is demonstrated

Then, random variables from various probability distributions are created
and their empirical densities and empirical cumulative distribution functions
are plotted

Finally, just for fun, bivariate normal random variables are created and 
their 2D and 3D densities are plotted.

NOTE:
Nowhere is Random module imported, and all the random numbers are generated,
only from Mathematical Algorithms.

"""

from distributions import Distributions
from visualisations import Plot

###############################################################################
# Random number generator demonstration:  -  -  -  -  -  -  -  -  -  -  -  -  -
###############################################################################

d = Distributions()

random_digit = d.rand_digit()

print("\nRandom digit from system time:")
print(random_digit)

states = []
for i in range(5):
    d = Distributions()
    states.append(d.state)

print("\nRandom initial states:")
print(states)

d = Distributions()
random_numbers = []
for i in range(5):
    random_number = next(d.RNG())
    random_numbers.append(random_number)

print("\nRandom numbers generated between 0 and 1 with equal probabilities:")
print(random_numbers)

###############################################################################
# Discrete Random Variables-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
###############################################################################

cdf = Plot()

# Discrete Uniform Random Variable:
l = []
for _ in range(100000):
    rv = d.discreteUniform(0,10)
    l.append(rv)

cdf.draw("Discrete Uniform Distribution", l)

# Bernoulli Random Variable:
l = []
for _ in range(100000):
    rv = d.bernoulli(0.5)
    l.append(rv)

cdf.draw("Bernoulli Distribution", l)

# Binomial Random Variable:
l = []
for _ in range(10000):
    rv = d.binomial(40, 0.5)
    l.append(rv)

cdf.draw("Binomial Distribution", l)

# Geometric Random Variable:
l = []
for _ in range(100000):
    rv = d.geometric(0.5)
    l.append(rv)

cdf.draw("Geometric Distribution", l)

# Negative Binomial Random Variable:
l = []
for _ in range(100000):
    rv = d.negativeBinomial(4, 0.5)
    l.append(rv)

cdf.draw("Negative Binomial Distribution", l)

# Poisson Random Variable:
l = []
for _ in range(100000):
    rv = d.poisson(4)
    l.append(rv)

cdf.draw("Poisson Distribution", l)

###############################################################################
# Continuous Random Variables -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
###############################################################################

# Uniform Random Variable:
l = []
for _ in range(1000000):
    rv = d.uniform()
    l.append(rv)

cdf.draw("Uniform Distribution", l)

# Exponential Random Variable:
l = []
for _ in range(100000):
    rv = d.exponential(1)
    l.append(rv)

cdf.draw("Exponential Distribution", l)

# Gamma Random Variable:
l = []
for _ in range(100000):
    rv = d.gamma(4, 1)
    l.append(rv)

cdf.draw("Gamma Distribution", l)

# Normal Random Variable:
l = []
for _ in range(100000):
    rv = d.normal(0, 1)
    l.append(rv)

cdf.draw("Normal Distribution", l)

# Log-normal Random Variable:
l = []
for _ in range(100000):
    rv = d.logNormal(0, 0.4)
    l.append(rv)

cdf.draw("Log-normal Distribution", l)

###############################################################################
# Bivariate Random Variable-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
###############################################################################

# Bivariate Independent Normal Random Variable:
l1 = []
l2 = []
for _ in range(10000):
    rv = d.bivariateNormal(0, 1)
    l1.append(rv[0])
    l2.append(rv[1])

cdf.draw("Bivariate Normal Distribution", l1, l2)