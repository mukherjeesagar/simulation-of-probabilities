# Simulation of Probabilities

A combination of pseudo-random and hardware-based random number generators is demonstrated using a linear congruential generator and system-generated performance time counter (order in nanoseconds). Thereby, a compilation of some standard algorithmic transformations is presented, with mathematical justifications and Python implementations. The idea is to first generate a Standard Uniform Random Variable and then transform it into another Random Variable which follows a specified probability law/distribution, by using an underlying mathematical algorithm. Refer to the report-file for details.


<p align="center"><img src="./plots/rng.png" alt="rng" width="75%" height="75%"><br><b>Schematic flow diagram</b></p>

The program is split into 3 python files:
- _main.py_: Driver script
- _disctributions.py_: Class to simulate the random variables
- _visualisations.py_: Plotting class for empirical functions (density and cdf)

## Empirical plots
Following are the plots of simulated random variables generated by the main.py, with the help of Visualisations class.
### Uniform (discrete) random variable
![Uniform random variable](/plots/11.png) ![Uniform random variable](/plots/12.png)
### Bernoulli random variable
![Bernoulli random variable](/plots/21.png) ![Bernoulli random variable](/plots/22.png)
### Binomial random variable
![Binomial random variable](/plots/31.png) ![Binomial random variable](/plots/33.png)
### Geometric random variable
![Geometric random variable](/plots/41.png) ![Geometric random variable](/plots/42.png)
### Negative-binomial random variable
![Negative-binomial random variable](/plots/51.png) ![Negative-binomial random variable](/plots/52.png)
### Poisson random variable
![Poisson random variable](/plots/61.png) ![Poisson random variable](/plots/62.png)
### Uniform (continuous) random variable
![Uniform random variable](/plots/71.png) ![Uniform random variable](/plots/72.png)
### Exponential random variable
![Exponential random variable](/plots/81.png) ![Exponential random variable](/plots/82.png)
### Gamma random variable
![Gamma random variable](/plots/91.png) ![Gamma random variable](/plots/92.png)
### Normal (Gaussian) random variable
![Normal random variable](/plots/a1.png) ![Normal random variable](/plots/a2.png)
### Log-normal random variable
![Log-Normal random variable](/plots/b1.png) ![Log-Normal random variable](/plots/b2.png)
### Bivariate normal random variable
![Bi-Normal random variable](/plots/c1.png) ![Bi-Normal random variable](/plots/c2.png)
