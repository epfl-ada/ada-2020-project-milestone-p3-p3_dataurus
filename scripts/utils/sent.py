from textblob import TextBlob
import pandas as pd
import datetime


def get_mean_sentiment(filename):
    def proc(x):
        try:
            x = pd.to_datetime(x)
        except:
            x = pd.to_datetime('2000-01-01')
        return x

    sentiment = pd.read_csv(filename)
    sentiment['date'] = sentiment['date'].apply(lambda x : proc(x))

    sentiment['date'] = sentiment['date'].apply(lambda x : x.replace(tzinfo=None))
    sentiment = sentiment[sentiment['date'] > pd.to_datetime('2019-01-01')]
    sentiment = sentiment[sentiment['date'] < pd.to_datetime('2020-06-01')]

    sentiment['sentiment'] = sentiment['title'].apply(lambda x: TextBlob(x).sentiment[0])
    sentiment['date'] = sentiment['date'].apply(lambda dt: datetime.date(dt.year, dt.month, dt.day))

    sentiment = sentiment.drop(['Unnamed: 0'], axis =1)
    sentiment = sentiment.groupby(['date']).agg(['mean', 'count'])
    return sentiment

def get_mean_sentiment_btc(filename):
    def proc(x):
        try:
            x = pd.to_datetime(x)
        except:
            x = pd.to_datetime('2000-01-01')
        return x

    sentiment = pd.read_csv(filename)
    sentiment = sentiment.drop(['id', 'total_views', 'total_shares', 'content'], axis =1)
    sentiment['date'] = sentiment['date'].apply(lambda x : proc(x))

    sentiment['date'] = sentiment['date'].apply(lambda x : x.replace(tzinfo=None))
    sentiment = sentiment[sentiment['date'] > pd.to_datetime('2016-12-01')]
    sentiment = sentiment[sentiment['date'] < pd.to_datetime('2020-05-01')]

    sentiment['sentiment'] = sentiment['header'].apply(lambda x: TextBlob(x).sentiment[0])
    sentiment['date'] = sentiment['date'].apply(lambda dt: datetime.date(dt.year, dt.month, dt.day))

    sentiment = sentiment.groupby(['date']).agg(['mean', 'count'])
    return sentiment


# The bitcoin news sentiment extraction
bitc = get_mean_sentiment_btc('../../data/bitcoin_news.csv')
bitc.to_csv('../../data/bitcoin_sentim.csv', sep='\t')

# The snp news sentiment extraction
snp = get_mean_sentiment('../../data/fin_news.csv')
snp.to_csv('../../data/bitcoin_sentim.csv', sep='\t')
