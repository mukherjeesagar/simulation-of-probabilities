"""
This python module (distributions.py) was made by Sagar Mukherjee, 
as part of the Final Project. It can be used to generate random variables 
from some of the most standard distribution laws:
    
   (A) Discrete Distributions:
       ``````````````````````
        1. Uniform
        2. Bernoulli
        3. Binomial
        4. Geometric
        5. Negative Binomial
        6. Poisson
    
   (B) Continuous Distributions:
       ````````````````````````
        1. Uniform
        2. Exponential
        3. Gamma
        4. Normal (Gaussian)
        5. Log-normal
        6. Bivariate Normal
        
For random number generation, the Lehmer (Park-Miller) linear-congruential 
generator is used and initial seed for the algorithm is picked from system-time,
taking the 100-th digit of time in nanoseconds (10**(-7) second).

"""


from time import perf_counter_ns
from math import exp, log, sin, cos

# Constant-Value, Pi upto 16 significant digits
PI = 3.141592653589793
MODULO = 2**31 - 1
MULTIPLIER = 7**5

class Distributions:
    """
    Base Class for pseudo-random number generator and all the derived random-
    varibles with various laws.
    
    """
    
    def __init__(self):
        """Constructor class"""
        self.state = 1
        self.seed()             # seed() called at initialization of object
    
    # Utilizes System-time in nano-seconds (taking last digit non-zero) to 
    # produce a random digit between 0 and 9 for seeding the state
    rand_digit = lambda self : int((int(perf_counter_ns()) / 100) % 10)

    def seed(self, n = None):
        """
        Method to initialize the starting state of the RNG() method
        """
        # 4 random digits are picked and this 4-digit number is set as the 
        # starting point (initial state) of the random number generator.
        if n != None:
            pass
        else:
            n = 0
            for i in range(4):
                n *= 10
                n += self.rand_digit()
        self.state = n

    def RNG(self):
        """
        Lehmer random number generator is used for random number generation,
        which is a type of linear congruential generator:
            
        X(n+1) = a*X(n) mod m.
        
        Instead of a regular function, a 'python generator' is used so as to
        be memory efficient, as none of the random numbers generated will have 
        to be stored.
        
        Furthermore, it is also time-efficient, as we do not need to wait until
        all the numbers have been generated.
        """
        
        # Modulo 'm' is chosen as a Mersenne prime here (2**31 - 1),
        # so as to keep it coprime with any arbitrary seed, less than m, 
        # is computationally efficient, and also is large enough 
        # so as to not begin repitions.
        
        # Multiplier 'a' is chosen as 7**5
        
        X = self.state                                 # Restore previous state
        self.state = X = (MULTIPLIER * X) % MODULO     # Save the state
        yield X/MODULO

####___________________________________________________________________________
#### DISCRETE RANDOM VARIABLES-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    
    def discreteUniform(self, a, b):
        """
        Method for obtaining a random integer between integers 'a' and 'b',
        with equal (uniform) probabilities.
        """
        # Picked a random number between [a,b) and used int()
        # as the greatest integer function.
        U = next(self.RNG())
        X = a + int((b-a)*U)
        return X
    
    def bernoulli(self, p):
        """
        Method for obtaining a Bernoulli random variable, with parameter p,
        which takes value 1 with probability 'p' and 0 with probability '1-p'.       
        """
        # Inverse-Transform Method: (Sheldon Ross, "Simulation-4th-Edition")
        U = next(self.RNG())
        if U <= p:
            X = 1
        else:
            X = 0
        return X
    
    def binomial(self, n, p):
        """
        Method for obtaining a Binomial random variable, with parameter n & p,
        which given number of successes from 'n' independent Bernoulli trials,
        each with parameter probability 'p'.
        """        
        X = 0
        for i in range(n):
            U = next(self.RNG())
            if U <= p:                  # Success Case
                X += 1
        return X
    
    def geometric(self, p):
        """
        Method for obtaining a Geometric random variable, with parameter p,
        which gives the number of independent Bernoulli trials (parameter = p)
        required for obtaining the first success
        """
        U = 1
        X = 0
        while U > p:                    # True, if Bernoulli trial fails
            U = next(self.RNG())
            X += 1
        return X
    
    def negativeBinomial(self, r, p):
        """
        Method for obtaining a Negative Binomial random variable, with 
        parameter r and p, which gives the number of success out of independent
        Bernoulli trials (parameter = p), before getting 'r' failures
        """
        X = 0
        failures = 0
        while failures < r:
            U = next(self.RNG())
            if U <= p:                  # Success Case
                X += 1
            else:                       # Failure Case
                failures += 1
        return X
    
    def poisson(self, mean):
        """
        Method for obtaining a Poisson random variable, with parameter 'mean',
        which gives the number of events occuring in a fixed interval of time,
        events occur independently and with a constant 'mean' rate
        """
        # Inverse-Transform Method: (Sheldon Ross, "Simulation-4th-Edition")
        U = next(self.RNG())
        i = 0
        p = exp(-mean)
        F = p
        while F <= U:
            #                        mean * P(X=i)
            # Property:  P(X=i+1) =  -------------
            #                            (i+1)
            p = mean*p/(i+1)
            F += p
            i += 1
        X = i
        return X
            
####___________________________________________________________________________
#### CONTINUOUS RANDOM VARIABLES -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  

    def uniform(self, a = 0, b = 1):
        """
        Method for obtaining a Uniform random variable between floats 'a' & 'b'
        """
        # U is a uniformly generated random number between [0,1)
        # Thus, U is shifted by a and scaled by (b-a)
        U = next(self.RNG())
        X = a + (b-a)*U
        return X
    
    def exponential(self, rate):
        """
        Method for obtaining an Exponential random variable, with parameter
        'rate', which gives the time between two events occuring continuously 
        and independently at a constant average 'rate'
        """
        # Inverse-Transform Method: (Sheldon Ross, "Simulation-4th-Edition")
        U = next(self.RNG())
        X = -log(U)/rate
        return X
    
    def gamma(self, n, rate):
        """
        Method for obtaining a Gamma random variable, with parameters n & rate,
        which gives the sum of 'n' independent exponential random variables, 
        each with the same parameter of average 'rate'.
        """
        Y = 1
        for i in range(n):
            U = next(self.RNG())
            Y *= U
        # Property: log(U1)+log(U2)+... = log(U1*U2...) = log(Y)
        X = -log(Y)/rate
        return X
    
    def normal(self, m = 0, s = 1):
        """
        Method for obtaining a Normal/Gaussian random variable, with paramters 
        mean (mu) = 'm' and standard deviation (sigma) = 's', which follows the
        Normal/Gaussian distribution.
        """
        # Box-Muller Transformation: (Sheldon Ross, "Simulation-4th-Edition")
        U1 = next(self.RNG())
        U2 = next(self.RNG())
        X = ((-2*log(U1))**0.5)*cos(2*PI*U2)
        return m + s*X
    
    def logNormal(self, m = 0, s = 1):
        """
        Method for obtaining a Log-normal random variable, with parameters m,s:
        It's logarithm is normally distributed.
        """
        Y = self.normal(m, s)
        # Since the logarithm of a Log-normal rv is normally distributed,
        # taking the inverse of a normal rv will be log-normally distributed
        X = exp(Y)
        return X
    
# BONUS:_______________________________________________________________________
# Bivariate Normal Random Variable  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    def bivariateNormal(self, m = 0, s = 1):
        """
        Method for obtaining two independent normal random variables, both 
        having parameters mean (mu) = 'm' and standard deviation (sigma) = 's'.
        """
        # Box-Muller Transformation: (Sheldon Ross, "Simulation-4th-Edition")
        U1 = next(self.RNG())
        U2 = next(self.RNG())
        X = ((-2*log(U1))**0.5)*cos(2*PI*U2)
        Y = ((-2*log(U1))**0.5)*sin(2*PI*U2)
        return m + s*X, m + s*Y