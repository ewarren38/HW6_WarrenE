class SLR_slope_simulator:
  #import some modules needed
  import numpy as np
  from numpy.random import default_rng
  from sklearn import linear_model
  slopes = []

  # Set initial attributes
  def __init__(self, beta_0, beta_1, x, sigma, seed):
    """
    Initiator Attributes
    """
    self.beta_0 = 7
    self.beta_1 = 1.5
    self.rng = default_rng(32)
    self.beta_0 = 7
    self.beta_1 = 1.5
    self.x = list(np.linspace(start = 0, stop = 10, num = 11))*3
    self.n = len(self.x)

  # Methods defined below
  def generate_data(self):
    """
    Method to generate one random data set
    """
    import pandas as pd
    x_list = self.x
    y_list = []
    #create the 'responses' modeled from the line plus a random deviation
    for i in range(0,self.n):
      y = beta_0 + beta_1*x_list[i] + rng.standard_normal(1) # calculate y for each x value
      y_list.append(y) # save y values as a list
      sim_data = pd.DataFrame(zip(x_list, y_list), columns = ("x", "y")) # create dataframe from x and y
    return sim_data

  def fit_slope(self, sim_data):
    """
    Method to fit the slope of one data set using an SLR
    """
    reg.fit(sim_data['x'].values.reshape(-1, 1), sim_data['y']) # fit the sample data
    return reg.coef_

  def run_simulations(self, simulations):
    """
    Method to run a given number of simulations to generate random data
    based on an SLR, then fit their slopes and save them
    """
    for i in range(simulations+1):
        x = SLR_slope_simulator(7, 1.5, list(np.linspace(start = 0, stop = 10, num = 11))*3, 1, 32) # create instance
        data = x.generate_data() 
        slope = x.fit_slope(data)
        SLR_slope_simulator.slopes.append(slope)
    return SLR_slope_simulator.slopes[0:11] # only print the first 10 slopes

  def plot_sampling_distribution(self):
    """
    Method to create a histogram plot illustrating the sampling
    distribution of beta_1
    """
    import pandas as pd
    if len(SLR_slope_simulator.slopes) > 0:
      DF = pd.DataFrame(SLR_slope_simulator.slopes)
      DF.plot.hist()
    else:
      print("run_simulations() must be called first")

  def find_prob(self, value, sided):
    """
    Method to calculate the probability of observing a fitted slope
    larger/smaller than a given value
    """
    slopes = np.array(SLR_slope_simulator.slopes) 
    if len(SLR_slope_simulator.slopes) > 0:
      if sided == "above": # find the probability that beta_1 is above our value
        count_above = np.sum(slopes > value) 
        prob = count_above / len(slopes)
      elif sided == "below": # find the probability that beta_1 is below our value
        count_below = np.sum(slopes < value)
        prob = count_below / len(slopes)
      elif sided == "two-sided":
        if value > slopes.median(): # find if the value is above the median beta_1
          count_above = np.sum(slopes > value)
          prob = 2*(count_above / len(slopes))
        else:
          count_below = np.sum(slopes < value)
          prob = 2*(count_below / len(slopes))
    return prob

# Create a new instance
instance = SLR_slope_simulator(12, 2, list(np.linspace(start = 0, stop = 10, num = 11))*3, 1, 10)

# Run the simulation 10000 times
instance.run_simulations(10000)

# Create a histogram that shows the sampling distribution based on our 10000 fitted slopes
instance.plot_sampling_distribution()

# Calculate the probability of observing a fitted slope above 2.1
x.find_prob(2.1, "above")

# Print off the first 10 fitted slopes from our attribute
x.slopes[0:11]