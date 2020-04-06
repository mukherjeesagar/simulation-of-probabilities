"""
This python module (visualisations.py) was made by Sagar Mukherjee, 
as part of the Final Project. It can be used to plot a list of random variables 
defined by some distribution laws.

The class 'Plot' is incorporated with a draw() method, which takes as argue-
ments, the distribution name (for the purpose of plot title), the random-
variable list X, and an optional random-variable list Y (Bivariate Case).

NOTE:
In this module, numpy is imported, only for the usage of numpy arrays, meshgrid,
and exponents. Numpy random is not used.

"""

from matplotlib import cm         # For colormap
# This import registers the 3D projection, but is otherwise unused
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np                # For Meshgrid

continuous_distributions = ["Uniform Distribution", "Exponential Distribution", "Gamma Distribution", "Normal Distribution", "Log-normal Distribution"]
discrete_distributions = ["Discrete Uniform Distribution", "Bernoulli Distribution", "Binomial Distribution", "Geometric Distribution", "Negative Binomial Distribution", "Poisson Distribution"]

class Plot:
    
    def __init__(self):
        pass
    
    def draw(self, distribution_name, X, Y = None):
        print('\n\n', distribution_name, ":")
        
        # Univariate Case:
        if Y == None:
            # Empirical Density Plot
            plt.subplots()
            plt.title("Empirical Density")
            # kde paramter gives a Gaussian Kernel estimate: 
            # Plots an approximate true density curve
            if distribution_name in continuous_distributions:
                sns.distplot(X, bins=100, kde=True, hist_kws={"histtype": "step"})
            
            # For Discrete case, kde is inappropriate
            elif distribution_name in discrete_distributions:
                plt.hist(X, bins = 100, density=True, histtype='step')
                
            plt.show()
            
            # Empirical Distribution Plot
            plt.subplots()
            plt.title("Empirical Distribution")
            plt.hist(X, bins = 100, cumulative=True, density=True, histtype='step')
            plt.show()
        
        # Bivariate Normal Case:
        else:
            plt.subplots()
            plt.title("2-Dimensional Histogram Plot")
            plt.hist2d(X, Y, bins=100)          # 2-D Histogram plot
            plt.show()
            
            X.sort()
            Y.sort()
            _X = np.array(X)                # numpy array for X
            _Y = np.array(Y)                # numpy array for Y
            
            x, y = np.meshgrid(_X, _Y)      # Meshgrid of X and Y
            z = np.exp(-(x**2 + y**2))      # Z gives the height of surface
            
            fig = plt.figure()
            fig.suptitle("3-Dimensional Projection Plot")
            ax = fig.add_subplot(111, projection='3d')
            ax.plot_surface(x,y,z, cmap=cm.jet)
            plt.show()