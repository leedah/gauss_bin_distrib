import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Binomial(Distribution):

    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float): mean value of the distribution
        stdev (float): standard deviation of the distribution
        data_list (list of floats): a list of floats to be extracted from the data file
        p (float): probability of an event occurring
        n (int): total number of trials        
    """
          
    
    def __init__(self, prob=.5, size=20):
         
        self.p = prob
        self.n = size

        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())
          
    
    def calculate_mean(self):
    
        """ Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
        """
                
        self.mean = self.n * self.p

        return self.mean



    def calculate_stdev(self):

        """ Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
        """ 

        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))
        
        return self.stdev
        
        
        
    def replace_stats_with_data(self):
    
        """ Function to calculate p and n from the data set
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
        """        
        
        self.n = len(self.data)

        positive_trials = 1.0 * sum(self.data)

        self.p = positive_trials / len(self.data) # self.n

        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

        return self.p, self.n

        
    def plot_bar(self):

        """ Function to output a bar chart of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
 
        plt.bar(x = ['0', '1'], height = [(1 - self.p) * self.n, self.p * self.n])
        plt.title('Bar chart of Data')
        plt.xlabel('Outcome')
        plt.ylabel('Count')       
        

    def pdf(self, x):

        """ Probability density function calculator for the gaussian distribution.
        
        Args:
            x (float): point for calculating the probability density function
            
        Returns:
            float: probability density function output
        """
        
        a = math.factorial(self.n) / (math.factorial(x) * (math.factorial(self.n - x)))
        b = (self.p ** x) * (1 - self.p) ** (self.n - x)
        
        return a * b        


    def plot_bar_pdf(self):

        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot    
        """
        
        x = []
        y = []
        
        # calculate the x values to visualize
        for k in range(self.n + 1):
            x.append(k)
            y.append(self.pdf(k))

        # make the plots
        plt.bar(x, y)
        plt.title('Distribution of Outcomes')
        plt.ylabel('Probability')
        plt.xlabel('Outcome')

        plt.show()

        return x, y
                
    def __add__(self, other):
        
        """ Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution   
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
        
        result = Binomial()
        result.n = self.n + other.n
        result.p = self.p
        result.calculate_mean()
        result.calculate_stdev()
        
        return result
        
        
    def __repr__(self):
    
        """ Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian
        """
    
        return "mean {}, standard deviation {:.2f}, p {:.2f}, n {} ".\
                format(self.mean, self.stdev, self.p, self.n)
