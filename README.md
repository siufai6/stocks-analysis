# stocks-analysis
## Implied Volatility

To understand the role of emotions in markets, we look at Hong Kong market.  HSI (Hang Seng Index) is a major index in Hong Kong.  HSIL is the implied volaility of the index.
We load data from csv files, merge them into a single dataframe and plot them on the same scale (using normalize techniques) to observe them.

Here is a plot of HSI with IV. (see also [this html](https://github.com/siufai6/stocks-analysis/blob/main/sentiment_HSI.html) )

![HSI vs IV](https://github.com/siufai6/stocks-analysis/blob/main/HSI_IV.png)

Observations:
1. Usually IV and HSI goes in different directions.  If index drops, sentiment is usually bad and people rush in to buy insurance for their portfolio
2. from time to time we see there is divergence in HSI and IV, e.g. in late Aug 2023, IV shoots to new high but the index failed to reach new low.  A divergence is observed and then there is a short term market rebound.
3. In the past few months, IV is somewhat "broken".  IV are range bound and not reflecting the actual pessimism in the market.  Market participants are somewhat clueless of where the index is heading. 

## Adding breadth into the same chart
When IV is not reflecting sentiments, what else can we use to make sense of the market?  Breadth is a possible factor to take into consideration.  To check the breadth of a market, we check the number of stocks that are still above their 50 day average price.  Usually index level and breadth are positively correlated.  Divergence in the movement might give us oppurtunity to trade a short term reversal of trend. 

*note that breadth data and code are not shown in the repo. as they are not public.

![HSI vs IV vs breadth](https://github.com/siufai6/stocks-analysis/blob/main/HSI_IV_breadth.png)
