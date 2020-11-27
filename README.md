# Predicting the Present with Google Trends

## Abstract

Turning points in financial time series are the hardest and arguably the most important to predict. The authors claim that incorporating Google Trends data in their model improves its performance in periods around turning points. In regards to the financial sector, however, Google search volume and stock prices are not always positively correlated, since in times of crisis and uncertainty people tend to check the market more often as the prices decrease. We will test the model on two additional datasets: (i) stock market data, specifically the S&P 500 index, and (ii) bitcoin data. We will try to improve the model of the paper by performing sentiment analysis on news headlines related to stocks and bitcoin. Our approach will be to use the Trends data to quantify the rate of change in the prices we want to predict, and the news to specify the direction of change (negative or positive).

## Research Questions

* Will the model of the paper work on financial time series whose data may be inversely correlated with the Trends data?
* Can an analysis of news help us predict the direction that the market will move?

## Proposed dataset

* [S&P 500 Index prices](https://finance.yahoo.com/quote/%5EGSPC/) for the period of January 2019 to May 2020, [Google Trends for the S&P 500](https://trends.google.com/trends/explore?date=2019-01-01%202020-05-31&geo=US&q=%2Fm%2F016yss) and [financial news headlines](https://www.kaggle.com/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests?select=analyst_ratings_processed.csv) for the same period.
* [Bitcoin prices](https://www.coindesk.com/price/bitcoin) for the period of December 2016 to April 2020, [Google Trends for bitcoin](https://trends.google.com/trends/explore?date=today%205-y&geo=US&q=%2Fm%2F05p0rrx) and [bitcoin related news](https://www.kaggle.com/asahicantu/cryptocurency-cointelegraph-newsfeed?select=cointelegraph_news_content.csv) for the same period.

## Methods

* **Google Trends data collection:** We will use [pytrends](https://pypi.org/project/pytrends/) to extract the Google Trends data and the Twitter API for the tweets.
* **Sentiment analysis:** We will classify each headline by assigning a {-1, 1} label indicating whether it was negative or positive, respectively. Then, we will experiment with either performing majority voting on the news of each day and get a single label for that day or computing the average and getting a value in the range [-1, 1]. By multiplying these numerical labels with the trends index (indicating the direction) we can get the values to train our model with.

## Proposed timeline

* **Week 1:** Download the two datasets with the Trends data. Find a model that performs sentiment analysis from bibliography.
* **Week 2:** Run the sentiment analysis model on our news to predict their labels. Train and run the autoregressive model with and without the impact of news to compare the performance of the two. Analyze the results and refine our approach if needed.
* **Week 3:** Finish coding, prepare a data story, figures and a short video presentation.

## Organization within the team

* **Week 1:** Orest will download the bitcoin dataset and Theofilos will download the S&P dataset. Each one will download the corresponding Google Trends data. Dimitris will search for papers related to sentimental analysis on Twitter. We will all read some selected papers and decide which model to use.
* **Week 2:** We will work together on applying the sentiment analysis model on the news and incorporating it into the autoregressive model.
* **Week 3:** Dimitris will prepare the data story, Orest will prepare the figures, and Theofilos the short video presentation.

## Questions for TAs (optional)
