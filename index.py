import time

# def calculate_volatility_index(data):
#     # Calculate the volatility index here
#     return volatility_index

import numpy as np

def calculate_volatility_index(data, time_period=252):
    """
    Calculates the volatility index for the given data.

    Parameters:
    data (list): A list of data points representing the asset's returns.
    time_period (int): The number of data points to use in the calculation. Default is 252 (trading days in a year).

    Returns:
    float: The volatility index.
    """
    # Calculate the returns of the asset
    returns = [data[i] - data[i-1] for i in range(1, len(data))]
    
    # Calculate the standard deviation of the returns
    std = np.std(returns[-time_period:])
    
    # Calculate the volatility index
    volatility_index = std * np.sqrt(time_period)
    
    return volatility_index


start_time = time.time()
volatility_index = calculate_volatility_index(data, time_period)
end_time = time.time()
latency = end_time - start_time

print("Latency:", latency)

