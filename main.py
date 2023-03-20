import numpy as np
import pandas as pd
import plotly.express as px

# This is a comment

def coin_toss(n):
    heads = 0
    tails = 0
    for i in range(n):
        if np.random.randint(0, 2) == 0:
            heads += 1
        else:
            tails += 1
    return heads, tails



def main():
    '''
    Plot the distribution of the coin tosses landing on heads or tails.
    '''
    n = 1000
    tosses = coin_toss(n)
    df = pd.DataFrame({'Heads': tosses[0], 'Tails': tosses[1]}, index=[0])
    df = df.melt()
    fig = px.bar(df, x='variable', y='value', color='variable')
    fig.show()



if __name__ == '__main__':
    main()




