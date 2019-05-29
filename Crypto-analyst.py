import pandas as pd

#Export json to csv and read csv
df = pd.read_json('https://api.coinmarketcap.com/v1/ticker')
df.to_csv('../Desktop/crypto.csv')
data_file = pd.read_csv('../Desktop/crypto.csv')


#Collect columns: id and market_cap_usd
collected_data = data_file[['id', 'market_cap_usd']]

cap = collected_data.query('market_cap_usd > 0')

top_cap_title = 'Top 10 market capitalization'
top_cap_ylabel = '% of total cap'

cap10 = cap[:10].set_index('id')
cap10 = cap10.assign(market_cap_perc = lambda x:(x.market_cap_usd/cap.market_cap_usd.sum())*100)

ax = cap10.market_cap_perc.head(10).plot.bar(title=TOP_CAP_TITLE)

ax.set_ylabel(TOP_CAP_YLABEL)


print(cap10)

