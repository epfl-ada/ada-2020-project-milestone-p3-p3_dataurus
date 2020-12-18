# Predicting the Present with Google Trends

## Abstract

Turning points in financial time series are the hardest and arguably the most important to predict. The authors claim that incorporating Google Trends data in their model improves its performance in periods around turning points. In regards to the financial sector, however, Google search volume and stock prices are not always positively correlated, since in times of crisis and uncertainty people tend to check the market more often as the prices decrease. We will test the model on two additional datasets: (i) stock market data, specifically the S&P 500 index, and (ii) bitcoin data. We will try to improve the model of the paper by performing sentiment analysis on news headlines related to stocks and bitcoin. Our approach will be to use the Trends data to quantify the rate of change in the prices we want to predict, and the news to specify the direction of change (negative or positive).

## Research Questions

* Will the model of the paper work on financial time series whose data may be inversely correlated with the Trends data?
* Can an analysis of news help us predict the direction that the market will move?

## Proposed dataset

* [S&P 500 Index prices](https://finance.yahoo.com/quote/%5EGSPC/) for the period of January 2019 to May 2020, [Google Trends for the S&P 500](https://trends.google.com/trends/explore?date=2019-01-01%202020-05-31&geo=US&q=%2Fm%2F016yss) and [financial news headlines](https://www.kaggle.com/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests?select=analyst_ratings_processed.csv) for the same period.
* [Bitcoin prices](https://finance.yahoo.com/quote/BTC-USD/history/) for the period of December 2016 to April 2020, [Google Trends for bitcoin](https://trends.google.com/trends/explore?date=today%205-y&geo=US&q=%2Fm%2F05p0rrx) and [bitcoin related news](https://www.kaggle.com/asahicantu/cryptocurency-cointelegraph-newsfeed?select=cointelegraph_news_content.csv) for the same period.

## Methods

* **Google Trends data collection:** We will use [pytrends](https://pypi.org/project/pytrends/) to extract the Google Trends data.
* **Sentiment analysis:** We will classify each headline by assigning a {-1, 1} label indicating whether it was negative or positive, respectively. We will use an already available tool (still to be decided, e.g., [TextBlob](https://textblob.readthedocs.io/en/dev/)). Then, we will experiment with either performing majority voting on the news of each day and get a single label for that day or computing the average and getting a value in the range [-1, 1]. By multiplying these numerical labels with the trends index (indicating the direction) we can get the values to train our model with.
* **Predictions:** For both datasets, we will predict the closing price on Fridays. Thus, using closing prices of previous weeks and news of the current week, we will try to predict the closing price for this week.


## Organization within the team

* Orest downloaded the bitcoin dataset and selected the news for the required period, contributed to the data story by writing the text and also wrote the report.
* Theofilos downloaded the S&P dataset and selected the news for the required period, contributed to the data story by creating the graphs and implementing the methods.
* Dimitris downloaded and aggregated the Google Trends data. Dimitis also performed the sentimental analysis on the news and contributed to the data story by setting up the Jekyll framework.

