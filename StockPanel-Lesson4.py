
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import jdatetime as jdt


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

def symbol_to_path(symbol,base_dir="data"):
    """ Return CSV file path given ticker symbol. """
    return os.path.join(base_dir,"{}.csv".format(str(symbol)))

def get_data(symbols,dates):
    """ Read stock data (ClosePrice) for given symbols from CSV files. """
    df=pd.DataFrame(index=dates)
    if 'SHARAK' not in symbols:   # add SHARAK for reference, if absent
        symbols.insert(0,'SHARAK')

    for symbol in symbols:
        df_temp=pd.read_csv(symbol_to_path(symbol),index_col='GDate',
                            parse_dates=True,usecols=['GDate','ClosePrice'],
                            na_values=['nan'])
        df_temp=df_temp.rename(columns={'ClosePrice':symbol})
        df=df.join(df_temp)
        if symbol=='SHARAK':
            df=df.dropna(subset=["SHARAK"])


    df=df.drop_duplicates()
    return df


def plot_data(df,title="Stock prices"):
    """ Plot stock prices """
    ax=df.plot(title=title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def plot_selected(df, columns,start_index,end_index):
    """ Plot the desired columns over index values in the given range. """
    plot_data(df.loc[start_index:end_index,columns],title="Selected data")


def normalize_data(df):
    return df/df.ix[0,:]


def test_run():

    """
    LESSON 4
    """
    ### Part 8-11 ###
    

    
    

    ### Part 12 ###
    

    ### Part 14 ###
    



    ### Part 17 ###
    



    
	
	
if __name__ == "__main__":
    test_run()