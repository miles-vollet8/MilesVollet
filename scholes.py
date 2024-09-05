import polars as pl
import numpy as np
from scipy.stats import norm
def call_pricer(current_price, strike_price, time, volatility, interest_rate):
    ln = np.log(current_price/strike_price)
    numerator = (ln + (interest_rate + .5*volatility*volatility)*time)
    denominator = (volatility*np.sqrt(time))
    d1 = numerator/denominator
    d2 = d1-denominator
    n1 = norm.cdf(d1)
    n2 = norm.cdf(d2)
    frac = strike_price/(np.exp(interest_rate*time))
    call_value = current_price*n1 - (frac*n2)
    
    return(call_value)

def put_pricer(current_price, strike_price, time, volatility, interest_rate):
    ln = np.log(current_price/strike_price)
    numerator = (ln + (interest_rate + .5*volatility*volatility)*time)
    denominator = (volatility*np.sqrt(time))
    d1 = numerator/denominator
    d2 = d1-denominator
    n1 = norm.cdf(d1)
    n2 = norm.cdf(d2)
    frac = strike_price/(np.exp(interest_rate*time))
    call_value = current_price*n1 - (frac*n2)
    
    put_value = call_value + frac - current_price
    
    return(put_value)


# def df_maker():
#     df = pl.DataFrame({'ID':[0],
#                     #'Option Name':[],
#                     'Asset Price':[0.0],
#                     'Strike Price':[0.0],
#                     'Time to Expiry':[0.0],
#                     'Volatility':[0.0],
#                     'Interest Rate':[0.0],
#                     'Call Value':[0.0],
#                     'Put Value':[0.0]})
#     count = 1
#     current_price = 0
#     while current_price != -1:
#         current_price = float(input("Asset's current price: "))
#         if current_price ==-1: break
#         strike_price = float(input("Option's strike price: "))
#         time = float(input("Time to expiry(in years): "))
#         volatility = float(input("Volatility: "))
#         interest_rate = float(input("Interest rate: "))
#         call_value = call_pricer(current_price, strike_price, time, volatility, interest_rate)
#         put_value = put_pricer(current_price, strike_price, time, volatility, interest_rate)
#         newdf = pl.DataFrame({'ID':[count],
#                             'Asset Price':[current_price],
#                             'Strike Price':[strike_price],
#                             'Time to Expiry':[time],
#                             'Volatility':[volatility],
#                             'Interest Rate':[interest_rate],
#                             'Call Value':[call_value],
#                             'Put Value':[put_value]}) 
#         df = df.extend(newdf)
#         count += 1
#     return(df)    
    
# df = df_maker()
def call_heatmap_maker(current_price, strike_price, time, volatility, interest_rate):

    call_value = call_pricer(current_price, strike_price, time, volatility, interest_rate)
    put_value = put_pricer(current_price, strike_price, time, volatility, interest_rate)
    # call_df = pl.DataFrame{
    #     'Volatility':[0.0],
    #     '.75':[0.0],
    #     '.8':[0.0],
    #     '.85':[0.0],
    #     '.9':[0.0],
    #     '.95':[0.0],
    #     '1.0':[0.0],
    #     '1.05':[0.0],
    #     '1.1':[0.0],
    #     '1.15':[0.0],
    #     '1.2':[0.0],
    #     '1.25':[0.0]
    # }

    high_vol = volatility*1.5
    call_df = pl.DataFrame({
        'Volatility':[high_vol],
        str(.75*current_price):[call_pricer(.75*current_price, strike_price, time, high_vol, interest_rate)],
        str(.8*current_price):[call_pricer(.8*current_price, strike_price, time, high_vol, interest_rate)],
        str(.85*current_price):[call_pricer(.85*current_price, strike_price, time, high_vol, interest_rate)],
        str(.9*current_price):[call_pricer(.9*current_price, strike_price, time, high_vol, interest_rate)],
        str(.95*current_price):[call_pricer(.95*current_price, strike_price, time, high_vol, interest_rate)],
        str(1.0*current_price):[call_pricer(current_price, strike_price, time, high_vol, interest_rate)],
        str(1.05*current_price):[call_pricer(1.05*current_price, strike_price, time, high_vol, interest_rate)],
        str(1.1*current_price):[call_pricer(1.1*current_price, strike_price, time, high_vol, interest_rate)],
        str(1.15*current_price):[call_pricer(1.15*current_price, strike_price, time, high_vol, interest_rate)],
        str(1.2*current_price):[call_pricer(1.2*current_price, strike_price, time, high_vol, interest_rate)],
        str(1.25*current_price):[call_pricer(1.25*current_price, strike_price, time, high_vol, interest_rate)]
        })
    vol_list = [1.4, 1.3, 1.2, 1.1, 1, .9, .8, .7, .6, .5]
    for vol in vol_list:
        new_vol = vol*volatility
        newdf = pl.DataFrame({
        'Volatility':[new_vol],
        str(.75*current_price):[call_pricer(.75*current_price, strike_price, time, new_vol, interest_rate)],
        str(.8*current_price):[call_pricer(.8*current_price, strike_price, time, new_vol, interest_rate)],
        str(.85*current_price):[call_pricer(.85*current_price, strike_price, time, new_vol, interest_rate)],
        str(.9*current_price):[call_pricer(.9*current_price, strike_price, time, new_vol, interest_rate)],
        str(.95*current_price):[call_pricer(.95*current_price, strike_price, time, new_vol, interest_rate)],
        str(1.0*current_price):[call_pricer(current_price, strike_price, time, new_vol, interest_rate)],
        str(1.05*current_price):[call_pricer(1.05*current_price, strike_price, time, new_vol, interest_rate)],
        str(1.1*current_price):[call_pricer(1.1*current_price, strike_price, time, new_vol, interest_rate)],
        str(1.15*current_price):[call_pricer(1.15*current_price, strike_price, time, new_vol, interest_rate)],
        str(1.2*current_price):[call_pricer(1.2*current_price, strike_price, time, new_vol, interest_rate)],
        str(1.25*current_price):[call_pricer(1.25*current_price, strike_price, time, new_vol, interest_rate)]
        })
        call_df = call_df.extend(newdf)
    return call_df

def put_heatmap_maker(current_price, strike_price, time, volatility, interest_rate):

    put_value = put_pricer(current_price, strike_price, time, volatility, interest_rate)
    put_value = put_pricer(current_price, strike_price, time, volatility, interest_rate)
    # put_df = pl.DataFrame{
    #     'Volatility':[0.0],
    #     '.75':[0.0],
    #     '.8':[0.0],
    #     '.85':[0.0],
    #     '.9':[0.0],
    #     '.95':[0.0],
    #     '1.0':[0.0],
    #     '1.05':[0.0],
    #     '1.1':[0.0],
    #     '1.15':[0.0],
    #     '1.2':[0.0],
    #     '1.25':[0.0]
    # }

    high_vol = volatility*1.5
    put_df = pl.DataFrame({
        'Volatility':[high_vol],
        str(.75*current_price):[put_pricer(.75*current_price, strike_price, time, high_vol, interest_rate)],
        str(.8*current_price):[put_pricer(.8*current_price, strike_price, time, high_vol, interest_rate)],
        str(.85*current_price):[put_pricer(.85*current_price, strike_price, time, high_vol, interest_rate)],
        str(.9*current_price):[put_pricer(.9*current_price, strike_price, time, high_vol, interest_rate)],
        str(.95*current_price):[put_pricer(.95*current_price, strike_price, time, high_vol, interest_rate)],
        str(1.0*current_price):[put_pricer(current_price, strike_price, time, high_vol, interest_rate)],
        str(1.05*current_price):[put_pricer(1.05*current_price, strike_price, time, high_vol, interest_rate)],
        str(1.1*current_price):[put_pricer(1.1*current_price, strike_price, time, high_vol, interest_rate)],
        str(1.15*current_price):[put_pricer(1.15*current_price, strike_price, time, high_vol, interest_rate)],
        str(1.2*current_price):[put_pricer(1.2*current_price, strike_price, time, high_vol, interest_rate)],
        str(1.25*current_price):[put_pricer(1.25*current_price, strike_price, time, high_vol, interest_rate)]
        })
    vol_list = [1.4, 1.3, 1.2, 1.1, 1, .9, .8, .7, .6, .5]
    for vol in vol_list:
        new_vol = vol*volatility
        newdf = pl.DataFrame({
        'Volatility':[new_vol],
        str(.75*current_price):[put_pricer(.75*current_price, strike_price, time, new_vol, interest_rate)],
        str(.8*current_price):[put_pricer(.8*current_price, strike_price, time, new_vol, interest_rate)],
        str(.85*current_price):[put_pricer(.85*current_price, strike_price, time, new_vol, interest_rate)],
        str(.9*current_price):[put_pricer(.9*current_price, strike_price, time, new_vol, interest_rate)],
        str(.95*current_price):[put_pricer(.95*current_price, strike_price, time, new_vol, interest_rate)],
        str(1.0*current_price):[put_pricer(current_price, strike_price, time, new_vol, interest_rate)],
        str(1.05*current_price):[put_pricer(1.05*current_price, strike_price, time, new_vol, interest_rate)],
        str(1.1*current_price):[put_pricer(1.1*current_price, strike_price, time, new_vol, interest_rate)],
        str(1.15*current_price):[put_pricer(1.15*current_price, strike_price, time, new_vol, interest_rate)],
        str(1.2*current_price):[put_pricer(1.2*current_price, strike_price, time, new_vol, interest_rate)],
        str(1.25*current_price):[put_pricer(1.25*current_price, strike_price, time, new_vol, interest_rate)]
        })
        put_df = put_df.extend(newdf)
    return put_df
current_price = float(input("Asset's current price: "))
strike_price = float(input("Option's strike price: "))
time = float(input("Time to expiry(in years): "))
volatility = float(input("Volatility: "))
interest_rate = float(input("Interest rate: "))
put_df = put_heatmap_maker(current_price, strike_price, time, volatility, interest_rate)
print(put_df)

put_df.write_excel('test.xlsx')