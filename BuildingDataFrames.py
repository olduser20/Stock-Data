

import pandas as pd
# import matplotlib.pyplot as plt

# def get_max_close(symbol):
    # df=pd.read_csv("data/{}.csv".format(symbol))
    # return df['Close'].max()

def test_run():
    start_date='2015-03-25'
    end_date='2019-03-16'
    dates=pd.date_range(start_date,end_date)
    # print(dates[0])
    df1=pd.DataFrame(index=dates)
    
    
    dfSHARAK=pd.read_csv("data/SHARAK.csv",index_col="GDate",parse_dates=True)
    # print(dfSHARAK)
    df1=df1.join(dfSHARAK)
    print(df1)
    
    
    # print(df['ClosePrice','LastPrice'])
    # df[['ClosePrice','PriceFirst']].plot()
    # plt.show()
	
    


	
	
if __name__ == "__main__":
    test_run()