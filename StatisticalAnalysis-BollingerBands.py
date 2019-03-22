

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

def get_rolling_mean(df,window):
    r=df.rolling(window)
    rm=r.mean()
    return rm

def get_rolling_std(df,window):
    s=df.rolling(window)
    rstd=s.std()
    return rstd

def get_bollinger_bands(rm,rstd):
    upper_band=rm+2*rstd
    lower_band=rm-2*rstd
    return upper_band,lower_band
    

def test_run():
    start_date='2018-03-21'
    end_date='2019-03-16'
    dates=pd.date_range(start_date,end_date)
    
    # symbols=['VBMELLAT','SHPETRO','KHODRO','FAMLI']
    symbols=['FAMLI']

    df1=get_data(symbols,dates)
            
    # plot_data(normalize_data(df1))

	
    rm_SMBL=get_rolling_mean(df1[symbols],window=20)
    rstd_SMBL=get_rolling_std(df1[symbols],window=20)

    upper_band,lower_band=get_bollinger_bands(rm_SMBL,rstd_SMBL)

    ax1=df1[symbols].plot(title="Bollinger Bands",label="sABER")
    rm_SMBL.plot(label="Rolling mean",ax=ax1)
    upper_band.plot(label="upper band",ax=ax1)
    lower_band.plot(label="lower band",ax=ax1)
    plt.show()

	
	
if __name__ == "__main__":
    test_run()