
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



def test_run():

    """
    LESSON 3
    """
    ### Part 8-11 ###
    # start_date='2018-03-16'
    # end_date='2019-03-16'
    # dates=pd.date_range(start_date,end_date)
    # # print(dates)
    # df1=pd.DataFrame(index=dates)
    # # print(df1)

    # dfSHARAK=pd.read_csv("data/SHARAK.csv",index_col='GDate',
    #                      parse_dates=True,usecols=['GDate','ClosePrice'],
    #                      na_values=['nan'])

    # dfSHARAK=dfSHARAK.drop_duplicates()

    # dfSHARAK = dfSHARAK.rename(columns={'ClosePrice':'SHARAK'})

    # df1=df1.join(dfSHARAK,how='inner')
    # # df1=df1.dropna()
    # # print(df1)

    # symbols=['VBMELLAT','KHODRO','FAMLI']
    # for symbol in symbols:
    #     df_temp=pd.read_csv("data/{}.csv".format(symbol),index_col='GDate',
    #                      parse_dates=True,usecols=['GDate','ClosePrice'],
    #                      na_values=['nan'])
    #     df_temp=df_temp.rename(columns={'ClosePrice':symbol})

    #     df1=df1.join(df_temp)
    #     print(df1)
    

    ### Part 12 ###
    start_date='2018-03-16'
    end_date='2019-03-16'
    dates=pd.date_range(start_date,end_date)

    symbols=['VBMELLAT','KHODRO','FAMLI']

    df=get_data(symbols,dates)
    print(df)

    ### Part 13 ###
    

    ### Part 14 ###
    
    
	
	
if __name__ == "__main__":
    test_run()