

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
    LESSON 2
    """
    ### Part 8-9 ###
    # df=pd.read_csv("data/IRX.csv")
    # print(df.head())
    # print(df.tail())
    # print(df[10:21])
    # print(len(df))

    ### Part 10-11 ###
    # for symbol in ['SHARAK','KHODRO']:
    #     print("Max Close")
    #     print(symbol,get_max_close(symbol))
    #     print("Mean Volume")
    #     print(symbol,get_mean_volume(symbol))

    ### Part 12 ###
    # df=pd.read_csv("data/SHARAK.csv")
    # print(df['ClosePrice'])
    # df['ClosePrice'].plot()
    # plt.show()

    ### Part 13 ###
    # df=pd.read_csv("data/SHARAK.csv")
    # print(df['PriceMax'])
    # df['PriceMax'].plot()
    # plt.show()

    ### Part 14 ###
    # df=pd.read_csv("data/VBMELLAT.csv")
    # df[['ClosePrice','PriceMax','PriceMin']].plot()
    # plt.show()
    
	
	
if __name__ == "__main__":
    test_run()