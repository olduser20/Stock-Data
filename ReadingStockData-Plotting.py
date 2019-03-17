

import pandas as pd
import matplotlib.pyplot as plt

# def get_max_close(symbol):
    # df=pd.read_csv("data/{}.csv".format(symbol))
    # return df['Close'].max()

def test_run():
    df=pd.read_csv("data/SHARAK.csv")
    # print(df['ClosePrice','LastPrice'])
    df[['ClosePrice','PriceFirst']].plot()
    plt.show()
	
    


	
	
if __name__ == "__main__":
    test_run()