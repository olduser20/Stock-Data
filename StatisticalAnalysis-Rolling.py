

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

def get_data(symbols,dates):
    df=pd.DataFrame(index=dates)
    dfSHARAK=pd.read_csv("data/SHARAK.csv",index_col="GDate",parse_dates=True,
                          usecols=['GDate','ClosePrice'],na_values=['nan'])
                          
    dfSHARAK=dfSHARAK.rename(columns={'ClosePrice':'SHARAK'})
    
    # print(dfSHARAK)
    df=df.join(dfSHARAK,how='inner')

    for symbol in symbols:
        df_temp=pd.read_csv("data/{}.csv".format(symbol),index_col='GDate',
                             parse_dates=True,usecols=['GDate','ClosePrice'],
                             na_values=['nan'])
                             
        df_temp=df_temp.rename(columns={'ClosePrice':symbol})
        df=df.join(df_temp)

    return df

def test_run():
    start_date='2018-03-21'
    end_date='2019-03-16'
    dates=pd.date_range(start_date,end_date)
    
    # symbols=['VBMELLAT','SHPETRO','KHODRO','FAMLI']
    symbols=['VBMELLAT']

    df1=get_data(symbols,dates)
            
    plot_data(normalize_data(df1))

	
    ax=df1['VBMELLAT'].plot(title="VBMELLAT rolling mean", label='VBMELLAT')
    

    # Calculating the rolling mean
    rm_VBMELLAT=df1['VBMELLAT'].rolling(window=5).mean()

    # Add rolling mean to same plot
    rm_VBMELLAT.plot(label='Rolling mean',ax=ax)

    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()


	
	
if __name__ == "__main__":
    test_run()