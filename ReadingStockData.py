

import pandas as pd

def test_run():
    df=pd.read_csv("data/IRX.csv")
    print(df.head())
    # print(df.tail())
    # print(df[10:21])
    print(len(df))

    
    
	
	
if __name__ == "__main__":
    test_run()