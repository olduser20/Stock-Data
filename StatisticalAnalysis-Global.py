

import pandas as pd
import matplotlib.pyplot as plt

# def get_max_close(symbol):
    # df=pd.read_csv("data/{}.csv".format(symbol))
    # return df['Close'].max()
    
def plot_data(df,title='Stock Prices'):
    ax=df.plot(title=title,fontsize=10)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()
    
def normalize_data(df):
    
    return df/df.ix[0,:]
    
def test_run():
    start_date='2018-03-21'
    end_date='2019-03-16'
    dates=pd.date_range(start_date,end_date)
    # print(dates[0])
    df1=pd.DataFrame(index=dates)
    
    
    dfSHARAK=pd.read_csv("data/SHARAK.csv",index_col="GDate",parse_dates=True,
                          usecols=['GDate','ClosePrice'],na_values=['nan'])
                          
    dfSHARAK=dfSHARAK.rename(columns={'ClosePrice':'SHARAK'})
    
    # print(dfSHARAK)
    df1=df1.join(dfSHARAK,how='inner')
    
    
    symbols=['VBMELLAT','SHPETRO','KHODRO','FAMLI']
    for symbol in symbols:
        df_temp=pd.read_csv("data/{}.csv".format(symbol),index_col='GDate',
                             parse_dates=True,usecols=['GDate','ClosePrice'],
                             na_values=['nan'])
                             
        df_temp=df_temp.rename(columns={'ClosePrice':symbol})
        df1=df1.join(df_temp)
        
    # print(df1)
    # print(df['ClosePrice','LastPrice'])
    # df1[['ClosePrice','PriceFirst']].plot()
    
    plot_data(normalize_data(df1))

	
    # print(df1.mean())
    print(df1.median())
    # print(df1.std())

    


	
	
if __name__ == "__main__":
    test_run()