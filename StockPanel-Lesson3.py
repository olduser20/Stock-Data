

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_max_close(symbol):
    """ Return the maximum closing value for stock indicated by symbol.

    Note: Data for a stock is stored in file: data/<symbol>.csv
    """
    df=pd.read_csv("data/{}.csv".format(symbol))    # read in data
    return df['ClosePrice'].max()    # compute and return max

def get_mean_volume(symbol):
    """ Return the mean volume value for stock indicated by symbol.

    Note: Data for a stock is stored in file: data/<symbol>.csv
    """
    df=pd.read_csv("data/{}.csv".format(symbol))    # read in data
    return df['VolumeTrade'].mean()    # compute and return max


def test_run():

    """
    LESSON 3
    """
    ### Part 8-9 ###
    

    ### Part 10-11 ###
    

    ### Part 12 ###
    

    ### Part 13 ###
    

    ### Part 14 ###
    
    
	
	
if __name__ == "__main__":
    test_run()