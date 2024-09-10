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


def call_heatmap_maker(current_price, strike_price, time, volatility, interest_rate):

    call_value = call_pricer(current_price, strike_price, time, volatility, interest_rate)
    put_value = put_pricer(current_price, strike_price, time, volatility, interest_rate)

    high_vol = volatility*1.5
    call_df = pl.DataFrame({
        'Call':[high_vol],
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
        'Call':[new_vol],
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

    high_vol = volatility*1.5
    put_df = pl.DataFrame({
        'Put':[high_vol],
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
        'Put':[new_vol],
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
call_df = call_heatmap_maker(current_price, strike_price, time, volatility, interest_rate)
put_df = put_heatmap_maker(current_price, strike_price, time, volatility, interest_rate)
put_val = put_pricer(current_price, strike_price, time, volatility, interest_rate)
call_val = call_pricer(current_price, strike_price, time, volatility, interest_rate)
print('Call Value = '+str(call_val)+'\n')
print("Put Value = "+str(put_val)+"\n")
call_df.write_excel('CallHeatmap.xlsx')
put_df.write_excel('PutHeatmap.xlsx')