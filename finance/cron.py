from django_cron import CronJobBase, Schedule
import yfinance as yf
import numpy as np
from finance.models import Stock,Detail,DisplaySr
from django.utils import timezone


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'    # a unique code

    def do(self):
        #Retrive a list of all available tickers
        for ticker in Stock.objects.all():
            y_stock = ticker.ticker
        #Retrive data for each ticker in the Stock
        #and format for to be input in the StockAnalysis clas
            stock_df = yf.download(tickers=y_stock,period="6mo",interval="1d")
            stock_df.drop(labels=["Open","High","Low","Close","Volume"],axis=1,inplace=True)

        #Calculate the
        #Calculate the expected_return
            stock_df['returns'] = stock_df.pct_change(1)
            daily_return = stock_df['returns'].mean()
            annual_return = ((daily_return+1)**252-1)*100


        #Calculate the expected_return
            daily_std = np.std(stock_df['returns'])
            annual_std = np.sqrt(252)*daily_std*100

        #Calculate the expected_return
            sharpe = annual_return/annual_std

        ###############################
        #### POPULATE THE DATABASE ####
        ###############################

            nytt_obj, created = Detail.objects.get_or_create(analyzed_stock_id=y_stock)
            nytt_obj.expected_return = annual_return
            nytt_obj.volatility = annual_std
            nytt_obj.sharperatio = sharpe
            nytt_obj.created_date = timezone.now()
            nytt_obj.save()
