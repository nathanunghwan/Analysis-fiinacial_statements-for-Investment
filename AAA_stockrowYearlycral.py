import requests
import pandas as pd
import pymysql
import datetime
from dateutil.relativedelta import relativedelta
from os import makedirs
import os.path, time, re
import csv
import numpy as np
from tqdm import tqdm
from scipy.stats import linregress

'''
#connect MySQL download Stock info
def connect_db():
    return pymysql.connect(host='localhost', user='root', password='********', db='USASTOCK', charset='utf8')
conn = connect_db()
curs = conn.cursor()
sql = "SELECT DISTINCT STOCK_CODE FROM USA_STOCK_INFO"
curs.execute(sql)
stock_list = [item[0] for item in curs.fetchall()]
conn.commit()
conn.close()
len(stock_list)
print(stock_list)
'''

#file list(Use local storage)
US_ticker = pd.read_csv('data/US_ticker.csv')
Us_ticker_symbol = US_ticker.loc[:,"symbol"]
stock_list = Us_ticker_symbol

#tickers = si.tickers_sp500()
stock_list = [item.replace(".", "-") for item in stock_list]  # Yahoo Finance uses dashes instead of dots

def download(url, file_name=None):
    if not file_name:
        file_name = url.split('/')[-1]

    with open(file_name, "wb") as file:
        response = requests.get(url)
        if response.status_code == 200:
            file.write(response.content)
            return True
    return False


def slope_reg(arr):
    y = np.array(arr)
    x = np.arange(len(y))
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    return slope


# For Downloading data 
def download_data(ticker):
    income_url = "https://stockrow.com/api/companies/{ticker}/financials.xlsx?dimension=A&section=Income%20Statement&sort=desc"
    income_trailing_url = "https://stockrow.com/api/companies/{ticker}/financials.xlsx?dimension=T&section=Income%20Statement&sort=desc"
    growth_url = "https://stockrow.com/api/companies/{ticker}/financials.xlsx?dimension=A&section=Growth&sort=desc"
    cashflow_url = "https://stockrow.com/api/companies/{ticker}/financials.xlsx?dimension=A&section=Cash Flow&sort=desc"
    cashflow_trailing_url = "https://stockrow.com/api/companies/{ticker}/financials.xlsx?dimension=T&section=Cash Flow&sort=desc"
    metrics_url = "https://stockrow.com/api/companies/{ticker}/financials.xlsx?dimension=A&amp;section=Metrics&amp;sort=desc"
    metrics_trailing_url = "https://stockrow.com/api/companies/{ticker}/financials.xlsx?dimension=T&section=Metrics&sort=desc"
    balance_url = "https://stockrow.com/api/companies/{ticker}/financials.xlsx?dimension=A&section=Balance Sheet&sort=desc"

    income_down = download(income_url.format(ticker=ticker), "{ticker}_INCOME.xlsx".format(ticker=ticker))
    income_trailing_down = download(income_trailing_url.format(ticker=ticker),
                                    "{ticker}_INCOME_Trailing.xlsx".format(ticker=ticker))
    growth_down = download(growth_url.format(ticker=ticker), "{ticker}_GROWTH.xlsx".format(ticker=ticker))
    cash_down = download(cashflow_url.format(ticker=ticker), "{ticker}_CASH.xlsx".format(ticker=ticker))
    cash_trailing_down = download(cashflow_trailing_url.format(ticker=ticker), "{ticker}_CASH_Trailing.xlsx".format(ticker=ticker))
    metrics_down = download(metrics_url.format(ticker=ticker), "{ticker}_METRICS.xlsx".format(ticker=ticker))
    metrics_trailing_down = download(metrics_trailing_url.format(ticker=ticker),
                                     "{ticker}_METRICS_trailing.xlsx".format(ticker=ticker))
    balance_down = download(balance_url.format(ticker=ticker), "{ticker}_Balance.xlsx".format(ticker=ticker))

    if income_down == True and growth_down == True and cash_down == True and metrics_down == True and income_trailing_down==True\
            and metrics_trailing_down == True and balance_down == True and cash_trailing_down == True :

        return True
    else:
        return False

a=pd.date_range('2000-12-31', periods=10, freq='A')
first=a[1]
second=a[2]
third=a[3]
fourth=a[4]
fifth=a[5]
sixth=a[6]
seventh=a[7]
eighth=a[8]
nineth=a[9]
from datetime import datetime
# Get stock data function
def get_stock_data(ticker):
    # Ticker  Read
    df_income = pd.read_excel("{ticker}_INCOME.xlsx".format(ticker=ticker), index_col=0).fillna(0)
    a = len(df_income.index)
    print(a)
    list_zero = []
    for i in range(0,a):
        list_zero.append(0)


    if len(df_income.columns)<10:
        diff = 10-len(df_income.columns)
        if diff ==1:
            df_income[first] = list_zero
            df_income.fillna(0)
        elif diff ==2:
            df_income[second] = list_zero
            df_income[first] = list_zero
            df_income.fillna(0)
            df_income.fillna(0)
        elif diff ==3:
            df_income[third] = list_zero
            df_income[second] = list_zero
            df_income[first] = list_zero
            df_income.fillna(0)
            df_income.fillna(0)
        elif diff ==4:
            df_income[fourth] = list_zero
            df_income[third] = list_zero
            df_income[second] = list_zero
            df_income[first] = list_zero
            df_income.fillna(0)
        elif diff ==5:
            df_income[fifth] = list_zero
            df_income[fourth] = list_zero
            df_income[third] = list_zero
            df_income[second] = list_zero
            df_income[first] = list_zero
            df_income.fillna(0)
        elif diff ==6:
            df_income[sixth] = list_zero
            df_income[fifth] = list_zero
            df_income[fourth] = list_zero
            df_income[third] = list_zero
            df_income[second] = list_zero
            df_income[first] = list_zero
            df_income.fillna(0)
        elif diff ==7:
            df_income[seventh] = list_zero
            df_income[sixth] = list_zero
            df_income[fifth] = list_zero
            df_income[fourth] = list_zero
            df_income[third] = list_zero
            df_income[second] = list_zero
            df_income[first] = list_zero
            df_income.fillna(0)
        elif diff ==8:
            df_income[eighth] = list_zero
            df_income[seventh] = list_zero
            df_income[sixth] = list_zero
            df_income[fifth] = list_zero
            df_income[fourth] = list_zero
            df_income[third] = list_zero
            df_income[second] = list_zero
            df_income[first] = list_zero
            df_income.fillna(0)
        else :
            df_income[nineth] = list_zero
            df_income[eighth] = list_zero
            df_income[seventh] = list_zero
            df_income[sixth] = list_zero
            df_income[fifth] = list_zero
            df_income[fourth] = list_zero
            df_income[third] = list_zero
            df_income[second] = list_zero
            df_income[first] = list_zero
            df_income.fillna(0)
    else:
        df_income = df_income
    df_income = df_income.T
###################################################################################################################

#########################################################################################

    df_growth = pd.read_excel("{ticker}_GROWTH.xlsx".format(ticker=ticker), index_col=0).fillna(0)
    b = len(df_growth.index)
    list_zero1 = []
    for i in range(0,b):
        list_zero1.append(0)

    if len(df_growth.columns)<10:
        diff = 10-len(df_growth.columns)
        if diff ==1:
            df_growth[first] = list_zero1
            df_growth.fillna(0)
        elif diff ==2:
            df_growth[second] = list_zero1
            df_growth[first] = list_zero1
            df_growth.fillna(0)
        elif diff ==3:
            df_growth[third] = list_zero1
            df_growth[second] = list_zero1
            df_growth[first] = list_zero1
            df_growth.fillna(0)
        elif diff ==4:
            df_growth[fourth] = list_zero1
            df_growth[third] = list_zero1
            df_growth[second] = list_zero1
            df_growth[first] = list_zero1
            df_growth.fillna(0)
        elif diff ==5:
            df_growth[fifth] = list_zero1
            df_growth[fourth] = list_zero1
            df_growth[third] = list_zero1
            df_growth[second] = list_zero1
            df_growth[first] = list_zero1
            df_growth.fillna(0)
        elif diff ==6:
            df_growth[sixth] = list_zero1
            df_growth[fifth] = list_zero1
            df_growth[fourth] = list_zero1
            df_growth[third] = list_zero1
            df_growth[second] = list_zero1
            df_growth[first] = list_zero1
            df_growth.fillna(0)
        elif diff ==7:
            df_growth[seventh] = list_zero1
            df_growth[sixth] = list_zero1
            df_growth[fifth] = list_zero1
            df_growth[fourth] = list_zero1
            df_growth[third] = list_zero1
            df_growth[second] = list_zero1
            df_growth[first] = list_zero1
            df_growth.fillna(0)
        elif diff ==8:
            df_growth[eighth] = list_zero1
            df_growth[seventh] = list_zero1
            df_growth[sixth] = list_zero1
            df_growth[fifth] = list_zero1
            df_growth[fourth] = list_zero1
            df_growth[third] = list_zero1
            df_growth[second] = list_zero1
            df_growth[first] = list_zero1
            df_growth.fillna(0)
        else :
            df_growth[nineth] = list_zero1
            df_growth[eighth] = list_zero1
            df_growth[seventh] = list_zero1
            df_growth[sixth] = list_zero1
            df_growth[fifth] = list_zero1
            df_growth[fourth] = list_zero1
            df_growth[third] = list_zero1
            df_growth[second] = list_zero1
            df_growth[first] = list_zero1
            df_growth.fillna(0)
    else:
        df_growth = df_growth
    df_growth = df_growth.T
#################################################################################################################




##################################################################################################################
    df_cash = pd.read_excel("{ticker}_CASH.xlsx".format(ticker=ticker), index_col=0).fillna(0)
    c = len(df_cash.index)
    list_zero2 = []
    for i in range(0, c):
        list_zero2.append(0)

    if len(df_cash.columns) < 10:
        diff = 10 - len(df_cash.columns)
        if diff == 1:
            df_cash[first] = list_zero2
            df_cash.fillna(0)
        elif diff == 2:
            df_cash[second] = list_zero2
            df_cash[first] = list_zero2
            df_cash.fillna(0)
        elif diff == 3:
            df_cash[third] = list_zero2
            df_cash[second] = list_zero2
            df_cash[first] = list_zero2
            df_cash.fillna(0)
        elif diff == 4:
            df_cash[fourth] = list_zero2
            df_cash[third] = list_zero2
            df_cash[second] = list_zero2
            df_cash[first] = list_zero2
            df_cash.fillna(0)
        elif diff == 5:
            df_cash[fifth] = list_zero2
            df_cash[fourth] = list_zero2
            df_cash[third] = list_zero2
            df_cash[second] = list_zero2
            df_cash[first] = list_zero2
            df_cash.fillna(0)
        elif diff == 6:
            df_cash[sixth] = list_zero2
            df_cash[fifth] = list_zero2
            df_cash[fourth] = list_zero2
            df_cash[third] = list_zero2
            df_cash[second] = list_zero2
            df_cash[first] = list_zero2
            df_cash.fillna(0)
        elif diff == 7:
            df_cash[seventh] = list_zero2
            df_cash[sixth] = list_zero2
            df_cash[fifth] = list_zero2
            df_cash[fourth] = list_zero2
            df_cash[third] = list_zero2
            df_cash[second] = list_zero2
            df_cash[first] = list_zero2
            df_cash.fillna(0)
        elif diff == 8:
            df_cash[eighth] = list_zero2
            df_cash[seventh] = list_zero2
            df_cash[sixth] = list_zero2
            df_cash[fifth] = list_zero2
            df_cash[fourth] = list_zero2
            df_cash[third] = list_zero2
            df_cash[second] = list_zero2
            df_cash[first] = list_zero2
            df_cash.fillna(0)
        else:
            df_cash[nineth] = list_zero2
            df_cash[eighth] = list_zero2
            df_cash[seventh] = list_zero2
            df_cash[sixth] = list_zero2
            df_cash[fifth] = list_zero2
            df_cash[fourth] = list_zero2
            df_cash[third] = list_zero2
            df_cash[second] = list_zero2
            df_cash[first] = list_zero2
            df_cash.fillna(0)
    else:
        df_cash = df_cash
    df_cash = df_cash.T
#############################################################################################################
    df_metrics = pd.read_excel("{ticker}_METRICS.xlsx".format(ticker=ticker), index_col=0).fillna(0)
    d = len(df_metrics.index)
    list_zero3 = []
    for i in range(0, d):
        list_zero3.append(0)

    if len(df_metrics.columns) < 10:
        diff = 10 - len(df_metrics.columns)
        if diff == 1:
            df_metrics[first] = list_zero3
            df_metrics.fillna(0)
        elif diff == 2:
            df_metrics[second] = list_zero3
            df_metrics[first] = list_zero3
            df_metrics.fillna(0)
        elif diff == 3:
            df_metrics[third] = list_zero3
            df_metrics[second] = list_zero3
            df_metrics[first] = list_zero3
            df_metrics.fillna(0)
        elif diff == 4:
            df_metrics[fourth] = list_zero3
            df_metrics[third] = list_zero3
            df_metrics[second] = list_zero3
            df_metrics[first] = list_zero3
            df_metrics.fillna(0)
        elif diff == 5:
            df_metrics[fifth] = list_zero3
            df_metrics[fourth] = list_zero3
            df_metrics[third] = list_zero3
            df_metrics[second] = list_zero3
            df_metrics[first] = list_zero3
            df_metrics.fillna(0)
        elif diff == 6:
            df_metrics[sixth] = list_zero3
            df_metrics[fifth] = list_zero3
            df_metrics[fourth] = list_zero3
            df_metrics[third] = list_zero3
            df_metrics[second] = list_zero3
            df_metrics[first] = list_zero3
            df_metrics.fillna(0)
        elif diff == 7:
            df_metrics[seventh] = list_zero3
            df_metrics[sixth] = list_zero3
            df_metrics[fifth] = list_zero3
            df_metrics[fourth] = list_zero3
            df_metrics[third] = list_zero3
            df_metrics[second] = list_zero3
            df_metrics[first] = list_zero3
            df_metrics.fillna(0)
        elif diff == 8:
            df_metrics[eighth] = list_zero3
            df_metrics[seventh] = list_zero3
            df_metrics[sixth] = list_zero3
            df_metrics[fifth] = list_zero3
            df_metrics[fourth] = list_zero3
            df_metrics[third] = list_zero3
            df_metrics[second] = list_zero3
            df_metrics[first] = list_zero3
            df_metrics.fillna(0)
        else:
            df_metrics[nineth] = list_zero3
            df_metrics[eighth] = list_zero3
            df_metrics[seventh] = list_zero3
            df_metrics[sixth] = list_zero3
            df_metrics[fifth] = list_zero3
            df_metrics[fourth] = list_zero3
            df_metrics[third] = list_zero3
            df_metrics[second] = list_zero3
            df_metrics[first] = list_zero3
            df_metrics.fillna(0)
    else:
        df_metrics = df_metrics
    df_metrics = df_metrics.T

####################################################################################################################
    df_income_trailing = pd.read_excel("{ticker}_INCOME_Trailing.xlsx".format(ticker=ticker), index_col=0).fillna(0)
    e= len(df_income_trailing.index)
    list_zero4 = []
    for i in range(0, e):
        list_zero4.append(0)

    if len(df_income_trailing.columns) < 10:
        diff = 10 - len(df_income_trailing.columns)
        if diff == 1:
            df_income_trailing[first] = list_zero4
            df_income_trailing .fillna(0)
        elif diff == 2:
            df_income_trailing [second] = list_zero4
            df_income_trailing[first] = list_zero4
            df_income_trailing .fillna(0)
        elif diff == 3:
            df_income_trailing [third] = list_zero4
            df_income_trailing [second] = list_zero4
            df_income_trailing[first] = list_zero4
            df_income_trailing .fillna(0)
        elif diff == 4:
            df_income_trailing [fourth] = list_zero4
            df_income_trailing [third] = list_zero4
            df_income_trailing [second] = list_zero4
            df_income_trailing[first] = list_zero4
            df_income_trailing .fillna(0)
        elif diff == 5:
            df_income_trailing[fifth] = list_zero4
            df_income_trailing [fourth] = list_zero4
            df_income_trailing [third] = list_zero4
            df_income_trailing [second] = list_zero4
            df_income_trailing[first] = list_zero4
            df_income_trailing .fillna(0)
        elif diff == 6:
            df_income_trailing [sixth] = list_zero4
            df_income_trailing[fifth] = list_zero4
            df_income_trailing [fourth] = list_zero4
            df_income_trailing [third] = list_zero4
            df_income_trailing [second] = list_zero4
            df_income_trailing[first] = list_zero4
            df_income_trailing .fillna(0)
        elif diff == 7:
            df_income_trailing [seventh] = list_zero4
            df_income_trailing [sixth] = list_zero4
            df_income_trailing[fifth] = list_zero4
            df_income_trailing [fourth] = list_zero4
            df_income_trailing [third] = list_zero4
            df_income_trailing [second] = list_zero4
            df_income_trailing[first] = list_zero4
            df_income_trailing .fillna(0)
        elif diff == 8:
            df_income_trailing [eighth] = list_zero4
            df_income_trailing [seventh] = list_zero4
            df_income_trailing [sixth] = list_zero4
            df_income_trailing[fifth] = list_zero4
            df_income_trailing [fourth] = list_zero4
            df_income_trailing [third] = list_zero4
            df_income_trailing [second] = list_zero4
            df_income_trailing[first] = list_zero4
            df_income_trailing .fillna(0)
        else:
            df_income_trailing [nineth] = list_zero4
            df_income_trailing [eighth] = list_zero4
            df_income_trailing [seventh] = list_zero4
            df_income_trailing [sixth] = list_zero4
            df_income_trailing[fifth] = list_zero4
            df_income_trailing [fourth] = list_zero4
            df_income_trailing [third] = list_zero4
            df_income_trailing [second] = list_zero4
            df_income_trailing[first] = list_zero4
            df_income_trailing .fillna(0)
    else:
        df_income_trailing  = df_income_trailing
    df_income_trailing = df_income_trailing.T
#####################################################################################################################
    df_metrics_trailing = pd.read_excel("{ticker}_METRICS_trailing.xlsx".format(ticker=ticker), index_col=0).fillna(0)
    f = len(df_metrics_trailing.index)
    list_zero5 = []
    for i in range(0, f):
        list_zero5.append(0)

    if len(df_metrics_trailing.columns) < 10:
        diff = 10 - len(df_metrics_trailing.columns)
        if diff == 1:
            df_metrics_trailing[first] = list_zero5
            df_metrics_trailing.fillna(0)
        elif diff == 2:
            df_metrics_trailing[second] = list_zero5
            df_metrics_trailing[first] = list_zero5
            df_metrics_trailing.fillna(0)
        elif diff == 3:
            df_metrics_trailing[third] = list_zero5
            df_metrics_trailing[second] = list_zero5
            df_metrics_trailing[first] = list_zero5
            df_metrics_trailing.fillna(0)
        elif diff == 4:
            df_metrics_trailing[fourth] = list_zero5
            df_metrics_trailing[third] = list_zero5
            df_metrics_trailing[second] = list_zero5
            df_metrics_trailing[first] = list_zero5
            df_metrics_trailing.fillna(0)
        elif diff == 5:
            df_metrics_trailing[fifth] = list_zero5
            df_metrics_trailing[fourth] = list_zero5
            df_metrics_trailing[third] = list_zero5
            df_metrics_trailing[second] = list_zero5
            df_metrics_trailing[first] = list_zero5
            df_metrics_trailing.fillna(0)
        elif diff == 6:
            df_metrics_trailing[sixth] = list_zero5
            df_metrics_trailing[fifth] = list_zero5
            df_metrics_trailing[fourth] = list_zero5
            df_metrics_trailing[third] = list_zero5
            df_metrics_trailing[second] = list_zero5
            df_metrics_trailing[first] = list_zero5
            df_metrics_trailing.fillna(0)
        elif diff == 7:
            df_metrics_trailing[seventh] = list_zero5
            df_metrics_trailing[sixth] = list_zero5
            df_metrics_trailing[fifth] = list_zero5
            df_metrics_trailing[fourth] = list_zero5
            df_metrics_trailing[third] = list_zero5
            df_metrics_trailing[second] = list_zero5
            df_metrics_trailing[first] = list_zero5
            df_metrics_trailing.fillna(0)
        elif diff == 8:
            df_metrics_trailing[eighth] = list_zero5
            df_metrics_trailing[seventh] = list_zero5
            df_metrics_trailing[sixth] = list_zero5
            df_metrics_trailing[fifth] = list_zero5
            df_metrics_trailing[fourth] = list_zero5
            df_metrics_trailing[third] = list_zero5
            df_metrics_trailing[second] = list_zero5
            df_metrics_trailing[first] = list_zero5
            df_metrics_trailing.fillna(0)
        else:
            df_metrics_trailing[nineth] = list_zero5
            df_metrics_trailing[eighth] = list_zero5
            df_metrics_trailing[seventh] = list_zero5
            df_metrics_trailing[sixth] = list_zero5
            df_metrics_trailing[fifth] = list_zero5
            df_metrics_trailing[fourth] = list_zero5
            df_metrics_trailing[third] = list_zero5
            df_metrics_trailing[second] = list_zero5
            df_metrics_trailing[first] = list_zero5
            df_metrics_trailing.fillna(0)
    else:
        df_metrics_trailing = df_metrics_trailing
    df_metrics_trailing = df_metrics_trailing.T

#################################################################################################################
    df_balance = pd.read_excel("{ticker}_Balance.xlsx".format(ticker=ticker), index_col=0).fillna(0)
    g= len(df_balance.index)
    list_zero6 = []
    for i in range(0, g):
        list_zero6.append(0)

    if len(df_balance.columns) < 10:
        diff = 10 - len(df_balance.columns)
        if diff == 1:
            df_balance[first] = list_zero6
            df_balance.fillna(0)
        elif diff == 2:
            df_balance[second] = list_zero6
            df_balance[first] = list_zero6
            df_balance.fillna(0)
        elif diff == 3:
            df_balance[third] = list_zero6
            df_balance[second] = list_zero6
            df_balance[first] = list_zero6
            df_balance.fillna(0)
        elif diff == 4:
            df_balance[fourth] = list_zero6
            df_balance[third] = list_zero6
            df_balance[second] = list_zero6
            df_balance[first] = list_zero6
            df_balance.fillna(0)
        elif diff == 5:
            df_balance[fifth] = list_zero6
            df_balance[fourth] = list_zero6
            df_balance[third] = list_zero6
            df_balance[second] = list_zero6
            df_balance[first] = list_zero6
            df_balance.fillna(0)
        elif diff == 6:
            df_balance[sixth] = list_zero6
            df_balance[fifth] = list_zero6
            df_balance[fourth] = list_zero6
            df_balance[third] = list_zero6
            df_balance[second] = list_zero6
            df_balance[first] = list_zero6
            df_balance.fillna(0)
        elif diff == 7:
            df_balance[seventh] = list_zero6
            df_balance[sixth] = list_zero6
            df_balance[fifth] = list_zero6
            df_balance[fourth] = list_zero6
            df_balance[third] = list_zero6
            df_balance[second] = list_zero6
            df_balance[first] = list_zero6
            df_balance.fillna(0)
        elif diff == 8:
            df_balance[eighth] = list_zero6
            df_balance[seventh] = list_zero6
            df_balance[sixth] = list_zero6
            df_balance[fifth] = list_zero6
            df_balance[fourth] = list_zero6
            df_balance[third] = list_zero6
            df_balance[second] = list_zero6
            df_balance[first] = list_zero6
            df_balance.fillna(0)
        else:
            df_balance[nineth] = list_zero6
            df_balance[eighth] = list_zero6
            df_balance[seventh] = list_zero6
            df_balance[sixth] = list_zero6
            df_balance[fifth] = list_zero6
            df_balance[fourth] = list_zero6
            df_balance[third] = list_zero6
            df_balance[second] = list_zero6
            df_balance[first] = list_zero6
            df_balance.fillna(0)
    else:
        df_balance = df_balance
    df_balance = df_balance.T

#####################################################################################################
    df_cash_trailing = pd.read_excel("{ticker}_CASH_Trailing.xlsx".format(ticker=ticker), index_col=0).fillna(0)
    h = len(df_cash_trailing.index)
    list_zero7 = []
    for i in range(0, h):
        list_zero7.append(0)

    if len(df_cash_trailing.columns) < 10:
        diff = 10 - len(df_cash_trailing.columns)
        if diff == 1:
            df_cash_trailing [first] = list_zero7
            df_cash_trailing .fillna(0)
        elif diff == 2:
            df_cash_trailing [second] = list_zero7
            df_cash_trailing [first] = list_zero7
            df_cash_trailing .fillna(0)
        elif diff == 3:
            df_cash_trailing [third] = list_zero7
            df_cash_trailing [second] = list_zero7
            df_cash_trailing [first] = list_zero7
            df_cash_trailing .fillna(0)
        elif diff == 4:
            df_cash_trailing [fourth] = list_zero7
            df_cash_trailing [third] = list_zero7
            df_cash_trailing [second] = list_zero7
            df_cash_trailing [first] = list_zero7
            df_cash_trailing .fillna(0)
        elif diff == 5:
            df_cash_trailing [fifth] = list_zero7
            df_cash_trailing [fourth] = list_zero7
            df_cash_trailing [third] = list_zero7
            df_cash_trailing [second] = list_zero7
            df_cash_trailing [first] = list_zero7
            df_cash_trailing .fillna(0)
        elif diff == 6:
            df_cash_trailing [sixth] = list_zero7
            df_cash_trailing [fifth] = list_zero7
            df_cash_trailing [fourth] = list_zero7
            df_cash_trailing [third] = list_zero7
            df_cash_trailing [second] = list_zero7
            df_cash_trailing [first] = list_zero7
            df_cash_trailing .fillna(0)
        elif diff == 7:
            df_cash_trailing [seventh] = list_zero7
            df_cash_trailing [sixth] = list_zero7
            df_cash_trailing [fifth] = list_zero7
            df_cash_trailing [fourth] = list_zero7
            df_cash_trailing [third] = list_zero7
            df_cash_trailing [second] = list_zero7
            df_cash_trailing [first] = list_zero7
            df_cash_trailing .fillna(0)
        elif diff == 8:
            df_cash_trailing [eighth] = list_zero7
            df_cash_trailing [seventh] = list_zero7
            df_cash_trailing [sixth] = list_zero7
            df_cash_trailing [fifth] = list_zero7
            df_cash_trailing [fourth] = list_zero7
            df_cash_trailing [third] = list_zero7
            df_cash_trailing [second] = list_zero7
            df_cash_trailing [first] = list_zero7
            df_cash_trailing .fillna(0)
        else:
            df_cash_trailing [nineth] = list_zero7
            df_cash_trailing [eighth] = list_zero7
            df_cash_trailing [seventh] = list_zero7
            df_cash_trailing [sixth] = list_zero7
            df_cash_trailing [fifth] = list_zero7
            df_cash_trailing [fourth] = list_zero7
            df_cash_trailing [third] = list_zero7
            df_cash_trailing [second] = list_zero7
            df_cash_trailing [first] = list_zero7
            df_cash_trailing .fillna(00)
    else:
        df_cash_trailing  = df_cash_trailing
    df_cash_trailing = df_cash_trailing.T

########################################################################################################

    revenue_isnert = ["{ticker}".format(ticker=ticker), "Revenue"]
    revenue_trailing_isnert = ["{ticker}".format(ticker=ticker), "Revenue"]
    revenue_growth_isnert = ["{ticker}".format(ticker=ticker), "revenue_growth"]
    revenue_growth_trailing_isnert = ["{ticker}".format(ticker=ticker), "revenue_growth"]
    revenue_growth_slope_isnert = ["{ticker}".format(ticker=ticker), "revenue_growth_slope"]
    growth_margin_isnert = ["{ticker}".format(ticker=ticker), "growth_margin"]
    growth_margin_trailing_isnert = ["{ticker}".format(ticker=ticker), "growth_margin"]
    growth_margin_slope_isnert = ["{ticker}".format(ticker=ticker), "growth_margin_slope"]
    operating_income_isnert = ["{ticker}".format(ticker=ticker), "Operating_Income"]
    operating_income_trailing_isnert = ["{ticker}".format(ticker=ticker), "Operating_Income"]
    operating_income_slope_isnert = ["{ticker}".format(ticker=ticker), "Operating_Income_slpoe"]
    operating_growth_isnert = ["{ticker}".format(ticker=ticker), "operating_growth"]
    operating_growth_trailing_isnert = ["{ticker}".format(ticker=ticker), "operating_growth"]
    operating_growth_slope_isnert = ["{ticker}".format(ticker=ticker), "operating_growth_slope"]
    operating_margin_isnert = ["{ticker}".format(ticker=ticker), "operating_margin"]
    operating_margin_trailing_isnert = ["{ticker}".format(ticker=ticker), "operating_margin"]
    operating_margin_slope_isnert = ["{ticker}".format(ticker=ticker), "operating_margin_slope"]
    net_income_isnert = ["{ticker}".format(ticker=ticker), "net_income"]
    net_income_trailing_isnert = ["{ticker}".format(ticker=ticker), "net_income"]
    net_income_margin_isnert = ["{ticker}".format(ticker=ticker), "net_income_margin"]
    net_income_margin_trailing_isnert = ["{ticker}".format(ticker=ticker), "net_income_margin"]
    netincome_growth_isnert = ["{ticker}".format(ticker=ticker), "net_income_growth"]
    netincome_growth_trailing_isnert = ["{ticker}".format(ticker=ticker), "net_income_growth"]
    netincome_growth_slope_isnert = ["{ticker}".format(ticker=ticker), "net_income_growth_slope"]
    eps_isnert = ["{ticker}".format(ticker=ticker), "EPS"]
    eps_trailing_isnert = ["{ticker}".format(ticker=ticker), "EPS"]
    eps_growth_isnert = ["{ticker}".format(ticker=ticker), "EPS_growth"]
    eps_growth_trailing_isnert = ["{ticker}".format(ticker=ticker), "EPS_growth"]
    eps_growth_slope_isnert = ["{ticker}".format(ticker=ticker), "EPS_growth_slope"]
    dividends_paid_isnert = ["{ticker}".format(ticker=ticker), "dividends_paid"]
    dividends_paid_trailing_isnert = ["{ticker}".format(ticker=ticker), "dividends_paid"]
    payout_ratio_isnert = ["{ticker}".format(ticker=ticker), "payout_ratio"]
    payout_ratio_trailing_isnert = ["{ticker}".format(ticker=ticker), "payout_ratio"]
    shares_isnert = ["{ticker}".format(ticker=ticker), "shares"]
    shares_trailing_isnert = ["{ticker}".format(ticker=ticker), "shares"]
    operating_cash_isnert = ["{ticker}".format(ticker=ticker), "operating_cash_flow"]
    operating_cash_trailing_isnert = ["{ticker}".format(ticker=ticker), "operating_cash_flow"]
    operating_cash_growth_isnert = ["{ticker}".format(ticker=ticker), "OCF_growth"]
    operating_cash_growth_trailing_isnert = ["{ticker}".format(ticker=ticker), "OCF_growth"]
    operating_cash_growth_slope_isnert = ["{ticker}".format(ticker=ticker), "OCF_growth_slope"]
    capital_expenditures_isnert = ["{ticker}".format(ticker=ticker), "capital_expenditures"]
    capital_expenditures_trailing_isnert = ["{ticker}".format(ticker=ticker), "capital_expenditures"]
    netincome_capex_ratio_isnert = ["{ticker}".format(ticker=ticker), "netincome_capex_ratio"]
    netincome_capex_ratio_trailing_isnert = ["{ticker}".format(ticker=ticker), "netincome_capex_ratio"]
    free_cashflow_isnert = ["{ticker}".format(ticker=ticker), "Free_Cash_Flow"]
    free_cashflow_trailing_isnert = ["{ticker}".format(ticker=ticker), "Free_Cash_Flow"]
    free_cashflow_growth_isnert = ["{ticker}".format(ticker=ticker), "FCF_growth"]
    free_cashflow_growth_trailing_isnert = ["{ticker}".format(ticker=ticker), "FCF_growth"]
    free_cashflow_growth_slope_isnert = ["{ticker}".format(ticker=ticker), "FCF_growth_slope"]
    fcf_per_share_isnert = ["{ticker}".format(ticker=ticker), "fcf_per_share"]
    fcf_per_share_trailing_isnert = ["{ticker}".format(ticker=ticker), "fcf_per_share"]
    roe_isnert = ["{ticker}".format(ticker=ticker), "ROE"]
    roe_trailing_isnert = ["{ticker}".format(ticker=ticker), "ROE"]
    roe_slope =  ["{ticker}".format(ticker=ticker), "ROE_slope"]
    roic_isnert = ["{ticker}".format(ticker=ticker), "ROIC"]
    roic_trailing_isnert = ["{ticker}".format(ticker=ticker), "ROIC"]
    bps_isnert = ["{ticker}".format(ticker=ticker), "BPS"]
    bps_trailing_isnert = ["{ticker}".format(ticker=ticker), "BPS"]
    pe_isnert = ["{ticker}".format(ticker=ticker), "PER"]
    pe_trailing_isnert = ["{ticker}".format(ticker=ticker), "PER"]
    psr_isnert = ["{ticker}".format(ticker=ticker), "PSR"]
    psr_trailing_isnert = ["{ticker}".format(ticker=ticker), "PSR"]
    p_fcf_ratio_isnert = ["{ticker}".format(ticker=ticker), "P/FCF"]
    p_fcf_ratio_trailing_isnert = ["{ticker}".format(ticker=ticker), "P/FCF"]
    freecash_per_share_isnert = ["{ticker}".format(ticker=ticker), "Freecash_Per_share"]
    average_days_of_receivables_isnert = ["{ticker}".format(ticker=ticker), "average_days_of_receivables"]
    average_days_of_payables_isnert = ["{ticker}".format(ticker=ticker), "average_days_of_payables"]
    day_of_hand_isnert = ["{ticker}".format(ticker=ticker), "day_of_hand"]
    ccc_isnert = ["{ticker}".format(ticker=ticker), "CCC"]
    approate_money_isnert  = ["{ticker}".format(ticker=ticker), "approate_money"]
    ccr_1_isnert =["{ticker}".format(ticker=ticker), "CCR_1OCF"]
    ccr_2_isnert = ["{ticker}".format(ticker=ticker), "CCR_2FCF"]
    ccr_diff_isnert = ["{ticker}".format(ticker=ticker), "CCR_DIFF"]
    intangible_assets_out_of_total_assets_isnert= ["{ticker}".format(ticker=ticker), "intangible_assets_out_of_total_assets"]
    debt_equity_isnert = ["{ticker}".format(ticker=ticker), "debt_equity"]
    cash_short_term_isnert = ["{ticker}".format(ticker=ticker), "cash_short_term"]
    total_current_assets_isnert = ["{ticker}".format(ticker=ticker), "total_current_assets"]
    total_assets_isnert = ["{ticker}".format(ticker=ticker), "total_assets"]
    total_current_liabilities_isnert = ["{ticker}".format(ticker=ticker), "total_current_liabilities"]
    total_liabilities_isnert = ["{ticker}".format(ticker=ticker), "total_liabilities"]
    total_shareholder_equity_isnert = ["{ticker}".format(ticker=ticker), "total_shareholder_equity"]
    currency_vs_totalassets_isnert = ["{ticker}".format(ticker=ticker), "currency_vs_totalassets"]
    null_value = float(0)

    # 10Years Revenue
    if 'Revenue' in df_income.columns:
        for i in reversed(range(0, 10)):
            revenue_isnert.append(float(df_income.iloc[i]['Revenue']))
    else:
        revenue_isnert = revenue_isnert + [0, 0, 0,0, 0, 0,0, 0, 0, 0]

    #trailing revenue
    if 'Revenue' in df_income_trailing.columns:
        revenue_isnert.append(float(df_income_trailing.iloc[0]['Revenue']))
    else:
        revenue_isnert = revenue_isnert + [0]

    # revenue growth
    if 'Revenue Growth' in df_income.columns:
        for i in reversed(range(0, 10)):
            revenue_growth_isnert.append(round((float(df_income.iloc[i]['Revenue Growth'])) * 100, 2))
    else:
        revenue_growth_isnert = revenue_growth_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    #revenue trailing
    if 'Revenue Growth' in df_income_trailing.columns:
        revenue_growth_isnert.append(round((float(df_income_trailing.iloc[0]['Revenue Growth'])) * 100, 2))
    else:
        revenue_growth_isnert = revenue_growth_isnert + [0]

    # growth margin
    if 'Gross Margin' in df_income.columns:
        for i in reversed(range(0, 10)):
            growth_margin_isnert.append(round((float(df_income.iloc[i]['Gross Margin'])) * 100, 2))
    else:
        growth_margin_isnert = growth_margin_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


    # growth margin
    if 'Gross Margin' in df_income_trailing.columns:
        growth_margin_isnert.append(round((float(df_income_trailing.iloc[0]['Gross Margin'])) * 100, 2))
    else:
        growth_margin_isnert = growth_margin_isnert + [0]


    # Operationg Income
    if 'Operating Income' in df_income.columns:
        for i in reversed(range(0, 10)):
            operating_income_isnert.append(float(df_income.iloc[i]['Operating Income']))
    else:
        operating_income_isnert = operating_income_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Operating income trailing
    if 'Operating Income' in df_income_trailing.columns:
        operating_income_isnert.append(float(df_income_trailing.iloc[0]['Operating Income']))
    else:
        operating_income_isnert = operating_income_isnert + [0]

    # operating growth
    if 'Operating Income Growth' in df_growth.columns:
        for i in reversed(range(0, 10)):
            operating_growth_isnert.append(round((float(df_growth.iloc[i]['Operating Income Growth'])) * 100, 2))
    else:
        operating_growth_isnert = operating_growth_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # operating growth trailing
    if 'Operating Income' in df_income_trailing.columns:
        if df_income_trailing.iloc[3]['Operating Income']==0:
            operating_growth_isnert = operating_growth_isnert + [0]
        else:
            operating_growth_isnert.append(round((((float(df_income_trailing.iloc[0]['Operating Income'])-
                                                     float(df_income_trailing.iloc[3]['Operating Income']))/
                                                    float(df_income_trailing.iloc[3]['Operating Income'])) * 100), 2))
    else:
        operating_growth_isnert = operating_growth_isnert + [0]


    # operating margin
    if 'Operating Income' in df_income.columns:
        for i in reversed(range(0, 10)):
            if df_income.iloc[i]['Revenue']==0:
                operating_margin_isnert.append(0)
            else:
                operating_margin_isnert.append(
                 round((float(df_income.iloc[i]['Operating Income']) / float(df_income.iloc[i]['Revenue'])) * 100, 2))
    else:
        operating_margin_isnert = operating_margin_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # operating margin trailing
    if 'Operating Income' in df_income_trailing.columns:
        if df_income_trailing.iloc[0]['Revenue']==0:
            operating_margin_isnert.append(0)
        else:
            operating_margin_isnert.append(
                round((float(df_income_trailing.iloc[0]['Operating Income']) / float(df_income_trailing.iloc[0]['Revenue'])) * 100, 2))
    else:
        operating_margin_isnert= operating_margin_isnert + [0]

    # Net income
    if 'Net Income Common' in df_income.columns:
        for i in reversed(range(0, 10)):
            net_income_isnert.append(float(df_income.iloc[i]['Net Income Common']))
    else:
        net_income_isnert = net_income_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # NetIncome trailing
    if 'Net Income Common' in df_income_trailing.columns:
        net_income_isnert.append(float(df_income_trailing.iloc[0]['Net Income Common']))
    else:
        net_income_isnert = net_income_isnert + [0]

    # Net income growth
    if 'Net Income Growth' in df_growth.columns:
        for i in reversed(range(0,10)):
            netincome_growth_isnert.append(round((float(df_growth.iloc[i]['Net Income Growth']))*100,2))
    else : netincome_growth_isnert = netincome_growth_isnert + [0,0,0,0,0,0,0,0,0,0]

    # Net income growth trailing
    if 'Net Income Common' in df_income_trailing.columns:
        if df_income_trailing.iloc[3]['Net Income Common']==0:
            netincome_growth_isnert.append(0)
        else:
            calcul= round(float(((float(df_income_trailing.iloc[0]['Net Income Common'])-
                                                       float(df_income_trailing.iloc[3]['Net Income Common']))/
                                                        float(df_income_trailing.iloc[3]['Net Income Common']))* 100),2 )
            netincome_growth_isnert.append(calcul)
    else:
        netincome_growth_isnert = netincome_growth_isnert + [0]

    #   net_income_margin
    for i in range(2, 13):
        if revenue_isnert[i]==0 :
            net_income_margin_isnert.append(0)
        else:
            net_income_margin=round((net_income_isnert[i]/revenue_isnert[i])*100,2)
            net_income_margin_isnert.append(net_income_margin)

    # eps 10Years
    if 'EPS (Diluted)' in df_income.columns:
        for i in reversed(range(0, 10)):
            eps_isnert.append(round(float(df_income.iloc[i]['EPS (Diluted)']), 2))
    else:
        eps_isnert = eps_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # eps trailing
    if 'EPS (Diluted)' in df_income_trailing.columns:
        eps_isnert.append(round(float(df_income_trailing.iloc[0]['EPS (Diluted)']), 2))
    else:
        eps_isnert = eps_isnert + [0]

    # eps growth
    if 'EPS Growth (diluted)' in df_growth.columns:
        for i in reversed(range(0, 10)):
            eps_growth_isnert.append(round((float(df_growth.iloc[i]['EPS Growth (diluted)'])) * 100, 2))
    else:
        eps_growth_isnert = eps_growth_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # eps growth trailing
    if 'EPS (Diluted)' in df_income_trailing.columns:
        if df_income_trailing.iloc[3]['EPS (Diluted)']==0:
            eps_growth_isnert.append(0)
        else:
            calcul1= round(float(((float(df_income_trailing.iloc[0]['EPS (Diluted)'])-
                                                       float(df_income_trailing.iloc[3]['EPS (Diluted)']))/
                                                        float(df_income_trailing.iloc[3]['EPS (Diluted)']))* 100),2 )
            eps_growth_isnert.append(calcul1)
    else:
        eps_growth_isnert = eps_growth_isnert + [0]

    # dividend
    if 'Dividends Paid (Common)' in df_cash.columns:
        for i in reversed(range(0, 10)):
            dividends_paid_isnert.append(float(df_cash.iloc[i]['Dividends Paid (Common)']))
    else:
        dividends_paid_isnert = dividends_paid_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # dividend trailing
    if 'Dividends Paid (Common)' in df_cash_trailing.columns:
        dividends_paid_isnert.append(float(df_cash_trailing.iloc[0]['Dividends Paid (Common)']))
    else:
        dividends_paid_isnert = dividends_paid_isnert + [0]

    #payout ratio
    if 'Dividends Paid (Common)' in df_cash.columns:
        for i in reversed(range(0, 10)):
            if df_income.iloc[i]['Net Income Common'] ==0:
                payout_ratio_isnert.append(0)
            else:
                payout_ratio_isnert.append(round((float(df_cash.iloc[i]['Dividends Paid (Common)']) / float(
                 df_income.iloc[i]['Net Income Common'])) * -100, 2))
    else:
        payout_ratio_isnert = payout_ratio_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # payout ratio trailing
    if 'Dividends Paid (Common)' in df_cash_trailing.columns:
        if df_income_trailing.iloc[0]['Net Income Common']==0:
            payout_ratio_isnert.append(0)
        else:
            payout_ratio_isnert.append(round((float(df_cash_trailing.iloc[0]['Dividends Paid (Common)']) / float(
                df_income_trailing.iloc[0]['Net Income Common'])) * -100, 2))

    else:
        payout_ratio_isnert = payout_ratio_isnert + [0]

    # share
    if 'Shares (Diluted, Average)' in df_income.columns:
        for i in reversed(range(0, 10)):
            shares_isnert.append(float(df_income.iloc[i]['Shares (Diluted, Average)']))
    else:
        shares_isnert = shares_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # share trailing
    if 'Shares (Diluted, Average)' in df_income_trailing.columns:
        shares_isnert.append(float(df_income_trailing.iloc[0]['Shares (Diluted, Average)']))
    else:
        shares_isnert = shares_isnert + [0]

    # Cash and Short Term Investments 현금자산
    if 'Cash and Short Term Investments' in df_balance.columns:
        for i in reversed(range(0, 10)):
            cash_short_term_isnert.append(float(df_balance.iloc[i]['Cash and Short Term Investments']))
    else:
        cash_short_term_isnert = cash_short_term_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cash_short_term_isnert.append(0)

    #total_current_assets
    if 'Total current assets' in df_balance.columns:
        for i in reversed(range(0, 10)):
            total_current_assets_isnert.append(float(df_balance.iloc[i]['Total current assets']))
    else:
        total_current_assets_isnert = total_current_assets_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    total_current_assets_isnert.append(0)

    #total_assets_isnert
    if 'Total Assets' in df_balance.columns:
        for i in reversed(range(0, 10)):
            total_assets_isnert.append(float(df_balance.iloc[i]['Total Assets']))
    else:
        total_assets_isnert = total_assets_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    total_assets_isnert.append(0)

    #total_current_liabilities_isnert
    if 'Total current liabilities' in df_balance.columns:
        for i in reversed(range(0, 10)):
            total_current_liabilities_isnert.append(float(df_balance.iloc[i]['Total current liabilities']))
    else:
        total_current_liabilities_isnert = total_current_liabilities_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    total_current_liabilities_isnert.append(0)

    #total_liabilities_isnert
    if 'Total liabilities' in df_balance.columns:
        for i in reversed(range(0, 10)):
            total_liabilities_isnert.append(float(df_balance.iloc[i]['Total liabilities']))
    else:
        total_liabilities_isnert = total_liabilities_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    total_liabilities_isnert.append(0)

    #total_shareholder_equity_isnert
    if 'Shareholders Equity (Total)' in df_balance.columns:
        for i in reversed(range(0, 10)):
            total_shareholder_equity_isnert.append(float(df_balance.iloc[i]['Shareholders Equity (Total)']))
    else:
        total_shareholder_equity_isnert = total_shareholder_equity_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    total_shareholder_equity_isnert.append(0)

    # Operating Cash Flow
    if 'Operating Cash Flow' in df_cash.columns:
        for i in reversed(range(0, 10)):
            operating_cash_isnert.append(float(df_cash.iloc[i]['Operating Cash Flow']))
    else:
        operating_cash_isnert = operating_cash_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Operating Cash Flow trailing
    if 'Operating Cash Flow' in df_cash_trailing.columns:
        operating_cash_isnert.append(float(df_cash_trailing.iloc[0]['Operating Cash Flow']))
    else:
        operating_cash_isnert = operating_cash_isnert + [0]

    # Operating Cash Flow Growth
    if 'Operating Cash Flow Growth' in df_growth.columns:
        for i in reversed(range(0, 10)):
            operating_cash_growth_isnert.append(
                round((float(df_growth.iloc[i]['Operating Cash Flow Growth'])) * 100, 2))
    else:
        operating_cash_growth_isnert = operating_cash_growth_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Operating Cash Flow Growth trailing
    if 'Operating Cash Flow' in df_cash_trailing.columns:
        if df_cash_trailing.iloc[3]['Operating Cash Flow'] ==0:
            operating_cash_growth_isnert.append(0)
        else:
            calcul2 =round((((float(df_cash_trailing.iloc[0]['Operating Cash Flow'])-
                                                       float(df_cash_trailing.iloc[3]['Operating Cash Flow']))/
                                                        float(df_cash_trailing.iloc[3]['Operating Cash Flow']))* 100),2 )
            operating_cash_growth_isnert.append(calcul2)
    else:
        operating_cash_growth_isnert = operating_cash_growth_isnert + [0]

    # Capital expenditures
    if 'Capital expenditures' in df_cash.columns:
        for i in reversed(range(0, 10)):
            capital_expenditures_isnert.append(float(df_cash.iloc[i]['Capital expenditures']))
    else:
        capital_expenditures_isnert = capital_expenditures_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Capital expenditures trailing
    if 'Capital expenditures' in df_cash_trailing.columns:
        capital_expenditures_isnert.append(float(df_cash_trailing.iloc[0]['Capital expenditures']))
    else:
        capital_expenditures_isnert = capital_expenditures_isnert + [0]

    # Rate of (Capital expenditures VS Net Income)
    if 'Capital expenditures' in df_cash.columns:
        for i in reversed(range(0, 10)):
            if df_income.iloc[i]['Net Income Common']==0:
                netincome_capex_ratio_isnert.append(0)
            else:
                netincome_capex_ratio_isnert.append(round(
                     float((df_cash.iloc[i]['Capital expenditures']) / float(df_income.iloc[i]['Net Income Common'])) * -100,
                      2))
    else:
        netincome_capex_ratio_isnert = netincome_capex_ratio_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Rate of (Capital expenditures VS Net Income) trailing
    if 'Capital expenditures' in df_cash_trailing.columns:
        if df_income_trailing.iloc[0]['Net Income Common']==0:
            netincome_capex_ratio_isnert.append(0)
        else:
            calcul4 =round(
                   float((df_cash_trailing.iloc[0]['Capital expenditures']) / float(df_income_trailing.iloc[0]['Net Income Common'])) * -100,
                   2)
        netincome_capex_ratio_isnert.append(calcul4)
    else:
        netincome_capex_ratio_isnert = netincome_capex_ratio_isnert + [0]

    # FCF
    if 'Free Cash Flow' in df_metrics.columns:
        for i in reversed(range(0, 10)):
            free_cashflow_isnert.append(float(df_metrics.iloc[i]['Free Cash Flow']))
    else:
        free_cashflow_isnert = free_cashflow_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # FCF trailing
    if 'Free Cash Flow' in df_metrics_trailing.columns:
        free_cashflow_isnert.append(float(df_metrics_trailing.iloc[0]['Free Cash Flow']))
    else:
        free_cashflow_isnert = free_cashflow_isnert + [0]

    # Free Cash Flow Growth
    if 'Free Cash Flow Growth' in df_growth.columns:
        for i in reversed(range(0, 10)):
            free_cashflow_growth_isnert.append(round((float(df_growth.iloc[i]['Free Cash Flow Growth'])) * 100, 2))
    else:
        free_cashflow_growth_isnert = free_cashflow_growth_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Free Cash Flow Growth trailing
    if 'Free Cash Flow' in df_metrics_trailing.columns:
        if df_metrics_trailing.iloc[3]['Free Cash Flow']==0:
            free_cashflow_growth_isnert.append(0)
        else:
            calcul5= round((((float(df_metrics_trailing.iloc[0]['Free Cash Flow'])-
                                                       float(df_metrics_trailing.iloc[3]['Free Cash Flow']))/
                                                        float(df_metrics_trailing.iloc[3]['Free Cash Flow']))* 100),2 )
            free_cashflow_growth_isnert.append(calcul5)
    else:
        free_cashflow_growth_isnert = free_cashflow_growth_isnert + [0]


    # Free Cash Flow per Share
    if 'Free Cash Flow per Share' in df_metrics.columns:
        for i in reversed(range(0, 10)):
            fcf_per_share_isnert.append(round(float(df_metrics.iloc[i]['Free Cash Flow per Share']), 2))
    else:
        fcf_per_share_isnert = fcf_per_share_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Free Cash Flow per Share trailing
    if 'Free Cash Flow per Share' in df_metrics_trailing.columns:
        fcf_per_share_isnert.append(round(float(df_metrics_trailing.iloc[0]['Free Cash Flow per Share']), 2))
    else:
        fcf_per_share_isnert = fcf_per_share_isnert + [0]

    # ROE
    if 'ROE' in df_metrics.columns:
        for i in reversed(range(0, 10)):
            roe_isnert.append(round((float(df_metrics.iloc[i]['ROE'])) * 100, 2))
    else:
        roe_isnert = roe_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # ROE trailing
    if 'ROE' in df_metrics_trailing.columns:
        roe_isnert.append(round((float(df_metrics_trailing.iloc[0]['ROE'])) * 100, 2))
    else:
        roe_isnert = roe_isnert + [0]

    # ROIC
    if 'ROIC' in df_metrics.columns:
        for i in reversed(range(0, 10)):
            roic_isnert.append(round((float(df_metrics.iloc[i]['ROIC'])) * 100, 2))
    else:
        roic_isnert = roic_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # ROIC trailing
    if 'ROIC' in df_metrics_trailing.columns:
        roic_isnert.append(round((float(df_metrics_trailing.iloc[0]['ROIC'])) * 100, 2))
    else:
        roic_isnert = roic_isnert + [0]

    # Book value per Share
    if 'Book value per Share' in df_metrics.columns:
        for i in reversed(range(0, 10)):
            bps_isnert.append(round(float(df_metrics.iloc[i]['Book value per Share']), 2))
    else:
        bps_isnert = bps_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Book value per Share trailing
    if 'Book value per Share' in df_metrics_trailing.columns:
        bps_isnert.append(round(float(df_metrics_trailing.iloc[0]['Book value per Share']), 2))
    else:
        bps_isnert = bps_isnert + [0]

    # P/E ratio
    if 'P/E ratio' in df_metrics.columns:
        for i in reversed(range(0, 10)):
            pe_isnert.append(round(float(df_metrics.iloc[i]['P/E ratio']), 2))
    else:
        pe_isnert = pe_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # P/E ratio trailing
    if 'P/E ratio' in df_metrics_trailing.columns:
        pe_isnert.append(round(float(df_metrics_trailing.iloc[0]['P/E ratio']), 2))
    else:
        pe_isnert = pe_isnert + [0]


    # psr
    if 'P/S ratio' in df_metrics.columns:
        for i in reversed(range(0, 10)):
            psr_isnert.append(round(float(df_metrics.iloc[i]['P/S ratio']), 2))
    else:
        psr_isnert = psr_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # psr trailing
    if 'P/S ratio' in df_metrics_trailing.columns:
        psr_isnert.append(round(float(df_metrics_trailing.iloc[0]['P/S ratio']), 2))
    else:
        psr_isnert = psr_isnert + [0]

    # P/ FCF
    if 'P/FCF ratio' in df_metrics.columns:
        for i in reversed(range(0, 10)):
            p_fcf_ratio_isnert.append(round(float(df_metrics.iloc[i]['P/FCF ratio']), 2))
    else:
        p_fcf_ratio_isnert = p_fcf_ratio_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # P/ FCF trailing
    if 'P/FCF ratio' in df_metrics_trailing.columns:
        p_fcf_ratio_isnert.append(round(float(df_metrics_trailing.iloc[0]['P/FCF ratio']), 2))
    else:
        p_fcf_ratio_isnert = p_fcf_ratio_isnert + [0]

    # Free Cash Flow per Share
    if 'Free Cash Flow per Share' in df_metrics.columns:
        for i in reversed(range(0, 10)):
            freecash_per_share_isnert.append(round(float(df_metrics.iloc[i]['Free Cash Flow per Share']), 2))
    else:
        freecash_per_share_isnert = freecash_per_share_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # P/ FCF trailing
    if 'Free Cash Flow per Share' in df_metrics_trailing.columns:
        freecash_per_share_isnert.append(round(float(df_metrics_trailing.iloc[0]['Free Cash Flow per Share']), 2))
    else:
        freecash_per_share_isnert = freecash_per_share_isnert + [0]

    # Intangible Assets out of Total Assets
    if 'Intangible Assets out of Total Assets' in df_metrics.columns:
        for i in reversed(range(0, 10)):
            intangible_assets_out_of_total_assets_isnert.append(round(float(df_metrics.iloc[i]['Intangible Assets out of Total Assets']), 2))
    else:
        intangible_assets_out_of_total_assets_isnert = intangible_assets_out_of_total_assets_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Intangible Assets out of Total Assets
    if 'Intangible Assets out of Total Assets' in df_metrics_trailing.columns:
        intangible_assets_out_of_total_assets_isnert.append(round(float(df_metrics_trailing.iloc[0]['Intangible Assets out of Total Assets']), 2))
    else:
        intangible_assets_out_of_total_assets_isnert = intangible_assets_out_of_total_assets_isnert + [0]

    #Debt/Equity
    if 'Debt/Equity' in df_metrics.columns:
        for i in reversed(range(0, 10)):
            debt_equity_isnert.append(round(float(df_metrics.iloc[i]['Debt/Equity']), 2))
    else:
        debt_equity_isnert = debt_equity_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # IDebt/Equity
    if 'Debt/Equity' in df_metrics_trailing.columns:
        debt_equity_isnert.append(round(float(df_metrics_trailing.iloc[0]['Debt/Equity']), 2))
    else:
        debt_equity_isnert = debt_equity_isnert + [0]


#########################################################
    #장홍래 신뢰성지표
    ###CCC :현금전환일수 =본플로트->재고자산회전일수+매출채권회전일수-매입채무회전일수-->적정보유현금 산출가능
    ##적정보유현금 = 매출*(1-당기순이익률)*(현금전환일수/365)
    ##- CCC 분석이 주가의 원인에 대한 분석이 된다. 경쟁 기업의 CCC를 5년 이상 비교하면 기업의 현금흐름 상황과
    # 경쟁우위 유무를 명확히 파악할 수 있다. -> 재무 <-> 기업을 번갈아 확인하면, 기업의 실체, 경쟁력을 확인할 수 있다.
    # Average Days of Receivables
    if 'Average Days of Receivables' in df_metrics.columns:
        for i in reversed(range(0, 10)):
            average_days_of_receivables_isnert.append(round(float(df_metrics.iloc[i]['Average Days of Receivables']), 2))
    else:
        average_days_of_receivables_isnert = average_days_of_receivables_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Average Days of Receivables
    if 'Average Days of Receivables' in df_metrics_trailing.columns:
        average_days_of_receivables_isnert.append(round(float(df_metrics_trailing.iloc[0]['Average Days of Receivables']), 2))
    else:
        average_days_of_receivables_isnert = average_days_of_receivables_isnert + [0]

    # Average Days of Payables
    if 'Average Days of Payables' in df_metrics.columns:
        for i in reversed(range(0, 10)):
            average_days_of_payables_isnert.append(round(float(df_metrics.iloc[i]['Average Days of Payables']), 2))
    else:
        average_days_of_payables_isnert = average_days_of_payables_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Average Days of Payables
    if 'Average Days of Payables' in df_metrics_trailing.columns:
        average_days_of_payables_isnert.append(round(float(df_metrics_trailing.iloc[0]['Average Days of Payables']), 2))
    else:
        average_days_of_payables_isnert = average_days_of_payables_isnert + [0]

    # Days of Inventory on Hand
    if 'Days of Inventory on Hand' in df_metrics.columns:
        for i in reversed(range(0, 10)):
            day_of_hand_isnert.append(round(float(df_metrics.iloc[i]['Days of Inventory on Hand']), 2))
    else:
        day_of_hand_isnert = day_of_hand_isnert + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Days of Inventory on Hand
    if 'Days of Inventory on Hand' in df_metrics_trailing.columns:
        day_of_hand_isnert.append(round(float(df_metrics_trailing.iloc[0]['Days of Inventory on Hand']), 2))
    else:
        day_of_hand_isnert = day_of_hand_isnert + [0]

    #CCC 현금 전환일수
    for i in range(2, 13):
        ccc=round(day_of_hand_isnert[i] + average_days_of_receivables_isnert[i] - average_days_of_payables_isnert[i],2)
        ccc_isnert.append(ccc)
    
    ##적정보유현금 = 매출*(1-당기순이익률)*(현금전환일수/365)
    for i in range(2, 13):
        money_approate=round(revenue_isnert[i]*(1-net_income_margin_isnert[i])*(ccc_isnert[i]/365),2)
        approate_money_isnert.append(money_approate)

    #정량기준 이익신뢰성CCR1--영업현금흐름/당기순이익->1이상->10년이상 지속적인 기업은 0.1%미난
    #투자 대상을 분석할 때 경쟁 기업과 5년 이상 비교하면 정량적으로 신뢰할 수 있는지 명확히 드러난다
    for i in range(2, 13):
        if net_income_isnert[i]==0:
            ccr_1_isnert.append(0)
        else:
            ccr_1 = round(operating_cash_isnert[i]/net_income_isnert[i],2)
            ccr_1_isnert.append(ccr_1)

    for i in range(2, 13):
        if net_income_isnert[i]==0:
            ccr_2_isnert.append(0)
        else:
            ccr_2 = round(free_cashflow_isnert[i]/net_income_isnert[i],2)
            ccr_2_isnert.append(ccr_2)

    for i in range(2, 13):
        ccr_diff = round(ccr_1_isnert[i]-ccr_2_isnert[i],2)
        ccr_diff_isnert.append(ccr_diff )

    #정량기준 자산신뢰성--현금/자산->10%이상-현실인 현금’은 언제 어디서나 기업의 실제 상황을 가장 잘 보여주는 신호다.특히 경쟁 기업과 장기간 비교 분석하면 경쟁우위를 명확히 알 수 있다
    for i in range(2, 13):
        if total_assets_isnert[i]==0:
            currency_vs_totalassets_isnert.append(0)
        else:
            currency_vs_totalassets = round(cash_short_term_isnert[i] / total_assets_isnert[i],2)
            currency_vs_totalassets_isnert.append(currency_vs_totalassets)


    #정량기준 무형자산 : 자산의 15%미만(무형자산/총자산), CCR1(영업현금흐름)ccr2(잉여현금흐름)의 차이가 적을 수록 강력한 무형자산 보유
    #해서 투자하기 좋은 기업-->고정비용이 적다는 방증
    ##--->모두 위에서 계산
    #정량기준 재무안정성: 부채비율 50%미만만---부채총계/자본총계*100
    #--->위에서 계산

    ###Slope###########################################################################################

    if revenue_isnert[-1] == revenue_isnert[-2]:
        revenue_growth_slope_isnert = ["{ticker}".format(ticker=ticker), "revenue_growth_slope"]
        revenue_growth = revenue_growth_isnert[2:12]
        sr1 = pd.Series(revenue_growth)
        aaa = sr1.rolling(window=3).apply(slope_reg)
        aaaa = aaa.tolist()
        for i in aaaa:
            a =round(i,2)
            revenue_growth_slope_isnert.append(a)
        revenue_growth_slope_isnert.append("Same_FIS")
        growth_margin_slope_isnert = ["{ticker}".format(ticker=ticker), " growth_margin_slope"]
        growth_margin = growth_margin_isnert[2:13]  ###??왜 13 12가 맞는듯 하여 일단 12로 바꿈
        sr2 = pd.Series(growth_margin)
        aaa1 = sr2.rolling(window=3).apply(slope_reg)
        aaaa1 = aaa1.tolist()
        for i in aaaa1:
            a =round(i,2)
            growth_margin_slope_isnert.append(a)
        operating_income_slope_isnert = ["{ticker}".format(ticker=ticker), "Operating_Income_slpoe"]
        operating_income = operating_income_isnert[2:12]
        sr3 = pd.Series(operating_income)
        aaa2 = sr3.rolling(window=3).apply(slope_reg)
        aaaa2 = aaa2.tolist()
        for i in aaaa2:
            operating_income_slope_isnert.append(i)
        operating_income_slope_isnert.append("Same_FIS")
        operating_growth_slope_isnert = ["{ticker}".format(ticker=ticker), "operating_growth_slope"]
        operating_growth = operating_growth_isnert[2:12]
        sr4 = pd.Series(operating_growth)
        aaa4 = sr4.rolling(window=3).apply(slope_reg)
        aaaa4 = aaa4.tolist()
        for i in aaaa4:
            a = round(i, 2)
            operating_growth_slope_isnert.append(a)
        operating_growth_slope_isnert.append("Same_FIS")
        operating_margin_slope_isnert = ["{ticker}".format(ticker=ticker), "operating_margin_slope"]
        operating_margin = operating_margin_isnert[2:12]
        sr5 = pd.Series(operating_margin)
        aaa5 = sr5.rolling(window=3).apply(slope_reg)
        aaaa5 = aaa5.tolist()
        for i in aaaa5:
            a = round(i, 2)
            operating_margin_slope_isnert.append(a)
        operating_margin_slope_isnert.append("Same_FIS")
        netincome_growth_slope_isnert = ["{ticker}".format(ticker=ticker), "net_income_growth_slope"]
        netincome_growth = netincome_growth_isnert[2:12]
        sr6 = pd.Series(netincome_growth)
        aaa6 = sr6.rolling(window=3).apply(slope_reg)
        aaaa6 = aaa6.tolist()
        for i in aaaa6:
            a = round(i, 2)
            netincome_growth_slope_isnert.append(a)
        netincome_growth_slope_isnert.append("Same_FIS")
        eps_growth_slope_isnert = ["{ticker}".format(ticker=ticker), "EPS_growth_slope"]
        eps_growth = eps_growth_isnert[2:12]
        sr7 = pd.Series(eps_growth)
        aaa7 = sr7.rolling(window=3).apply(slope_reg)
        aaaa7 = aaa7.tolist()
        for i in aaaa7:
            a = round(i, 2)
            eps_growth_slope_isnert.append(a)
        eps_growth_slope_isnert.append("Same_FIS")
        operating_cash_growth_slope_isnert = ["{ticker}".format(ticker=ticker), "OCF_growth_slope"]
        operating_cash_growth = operating_cash_growth_isnert[2:12]
        sr8 = pd.Series(operating_cash_growth)
        aaa8 = sr8.rolling(window=3).apply(slope_reg)
        aaaa8 = aaa8.tolist()
        for i in aaaa8:
            a = round(i, 2)
            operating_cash_growth_slope_isnert.append(a)
        operating_cash_growth_slope_isnert.append("Same_FIS")
        free_cashflow_growth_slope_isnert = ["{ticker}".format(ticker=ticker), "FCF_growth_slope"]
        free_cashflow_growth = free_cashflow_growth_isnert[2:12]
        sr9 = pd.Series(free_cashflow_growth)
        aaa9 = sr9.rolling(window=3).apply(slope_reg)
        aaaa9 = aaa9.tolist()
        for i in aaaa9:
            a = round(i, 2)
            free_cashflow_growth_slope_isnert.append(a)
        free_cashflow_growth_slope_isnert.append("Same_FIS")
        roe_slope_isnert = ["{ticker}".format(ticker=ticker), "ROE_slope"]
        roe = roe_isnert[2:12]
        sr10 = pd.Series(roe)
        aaa10 = sr10.rolling(window=3).apply(slope_reg)
        aaaa10 = aaa10.tolist()
        for i in aaaa10:
            a = round(i, 2)
            roe_slope_isnert.append(a)
        roe_slope_isnert.append("Same_FIS")
    else:
        revenue_growth_slope_isnert = ["{ticker}".format(ticker=ticker), "revenue_growth_slope"]
        revenue_growth = revenue_growth_isnert[2:13]
        sr1 = pd.Series(revenue_growth)
        aaa = sr1.rolling(window=3).apply(slope_reg)
        aaaa = aaa.tolist()
        for i in aaaa:
            a = round(i, 2)
            revenue_growth_slope_isnert.append(a)

        growth_margin_slope_isnert = ["{ticker}".format(ticker=ticker), " growth_margin_slope"]
        growth_margin = growth_margin_isnert[2:13]
        sr2 = pd.Series(growth_margin)
        aaa1 = sr2.rolling(window=3).apply(slope_reg)
        aaaa1 = aaa1.tolist()
        for i in aaaa1:
            a = round(i, 2)
            growth_margin_slope_isnert.append(a)

        operating_income_slope_isnert = ["{ticker}".format(ticker=ticker), "Operating_Income_slpoe"]
        operating_income = operating_income_isnert[2:13]
        sr3 = pd.Series(operating_income)
        aaa2 = sr3.rolling(window=3).apply(slope_reg)
        aaaa2 = aaa2.tolist()
        for i in aaaa2:
            a = round(i, 2)
            operating_income_slope_isnert.append(a)

        operating_growth_slope_isnert = ["{ticker}".format(ticker=ticker), "operating_growth_slope"]
        operating_growth = operating_growth_isnert[2:13]
        sr4 = pd.Series(operating_growth)
        aaa4 = sr4.rolling(window=3).apply(slope_reg)
        aaaa4 = aaa4.tolist()
        for i in aaaa4:
            a = round(i, 2)
            operating_growth_slope_isnert.append(a)

        operating_margin_slope_isnert = ["{ticker}".format(ticker=ticker), "operating_margin_slope"]
        operating_margin = operating_margin_isnert[2:13]
        sr5 = pd.Series(operating_margin)
        aaa5 = sr5.rolling(window=3).apply(slope_reg)
        aaaa5 = aaa5.tolist()
        for i in aaaa5:
            operating_margin_slope_isnert.append(i)

        netincome_growth_slope_isnert = ["{ticker}".format(ticker=ticker), "net_income_growth_slope"]
        netincome_growth = netincome_growth_isnert[2:13]
        sr6 = pd.Series(netincome_growth)
        aaa6 = sr6.rolling(window=3).apply(slope_reg)
        aaaa6 = aaa6.tolist()
        for i in aaaa6:
            a = round(i, 2)
            netincome_growth_slope_isnert.append(a)

        eps_growth_slope_isnert = ["{ticker}".format(ticker=ticker), "EPS_growth_slope"]
        eps_growth = eps_growth_isnert[2:13]
        sr7 = pd.Series(eps_growth)
        aaa7 = sr7.rolling(window=3).apply(slope_reg)
        aaaa7 = aaa7.tolist()
        for i in aaaa7:
            a = round(i, 2)
            eps_growth_slope_isnert.append(a)

        operating_cash_growth_slope_isnert = ["{ticker}".format(ticker=ticker), "OCF_growth_slope"]
        operating_cash_growth = operating_cash_growth_isnert[2:13]
        sr8 = pd.Series(operating_cash_growth)
        aaa8 = sr8.rolling(window=3).apply(slope_reg)
        aaaa8 = aaa8.tolist()
        for i in aaaa8:
            a = round(i, 2)
            operating_cash_growth_slope_isnert.append(a)

        free_cashflow_growth_slope_isnert = ["{ticker}".format(ticker=ticker), "FCF_growth_slope"]
        free_cashflow_growth = free_cashflow_growth_isnert[2:13]
        sr9 = pd.Series(free_cashflow_growth)
        aaa9 = sr9.rolling(window=3).apply(slope_reg)
        aaaa9 = aaa9.tolist()
        for i in aaaa9:
            a = round(i, 2)
            free_cashflow_growth_slope_isnert.append(a)

        roe_slope_isnert = ["{ticker}".format(ticker=ticker), "ROE_slope"]
        roe = roe_isnert[2:13]
        sr10 = pd.Series(roe)
        aaa10 = sr10.rolling(window=3).apply(slope_reg)
        aaaa10 = aaa10.tolist()
        for i in aaaa10:
            a = round(i, 2)
            roe_slope_isnert.append(a)

    return revenue_isnert, revenue_growth_isnert, growth_margin_isnert, operating_income_isnert, \
           operating_growth_isnert,  operating_margin_isnert,\
           net_income_isnert, net_income_margin_isnert,netincome_growth_isnert, eps_isnert,\
           eps_growth_isnert, dividends_paid_isnert, payout_ratio_isnert,\
           shares_isnert, cash_short_term_isnert, total_current_assets_isnert, total_assets_isnert,\
           total_current_liabilities_isnert, total_liabilities_isnert, total_shareholder_equity_isnert, operating_cash_isnert, \
           operating_cash_growth_isnert, capital_expenditures_isnert,netincome_capex_ratio_isnert,\
           free_cashflow_isnert, free_cashflow_growth_isnert, fcf_per_share_isnert, \
           roe_isnert, roic_isnert, bps_isnert,  pe_isnert,  psr_isnert, p_fcf_ratio_isnert, freecash_per_share_isnert,\
           revenue_growth_slope_isnert, growth_margin_slope_isnert, operating_income_slope_isnert, \
           operating_growth_slope_isnert, operating_margin_slope_isnert, netincome_growth_slope_isnert, \
           eps_growth_slope_isnert, operating_cash_growth_slope_isnert, free_cashflow_growth_slope_isnert, \
           roe_slope_isnert, average_days_of_receivables_isnert, average_days_of_payables_isnert, day_of_hand_isnert, \
           approate_money_isnert, ccc_isnert, ccr_1_isnert, ccr_2_isnert, ccr_diff_isnert, intangible_assets_out_of_total_assets_isnert, \
           debt_equity_isnert, currency_vs_totalassets_isnert

#
'''Insert to MYSQL
conn = connect_db()
curs = conn.cursor()
sql = """insert into STOCK_INFO_USA(STOCK_CODE, AREA, Y2012, Y2013, Y2014, Y2015, Y2016, Y2017, Y2018, Y2019, Y2020, Y2021) 
    values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
'''
'''
result = []
'''
'''
# 반복문 돌면서 INSERT
for i, ticker in enumerate(stock_list):
    try:
        if download_data(ticker):
            stock_info = get_stock_data(ticker)
            result.append(stock_info)
            curs.execute(sql, result)
            conn.commit()
        # else:
          # print(i, ' 번 째 ', ticker, ' : NO DATA PASS')
    except Exception as e:
        print(i, ' 번 째 오류 발생 : ', ticker, ' 오류:', str(e))

conn.close()
'''
'''
import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active

sheet.append(["티커", "영역", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"])

'''
finance_data =pd.DataFrame()

# 반복문 돌면서 INSERT
for i, ticker in enumerate(stock_list):

    try:
        if download_data(ticker):
            stock_info = get_stock_data(ticker)
            # sheet.append(stock_info)
            # result=result.append(stock_info)
            data = pd.DataFrame(stock_info)
            print(data)
            #finance_data.append(data)
            finance_data=pd.concat([finance_data, data])
            #data.loc['revenue_growth_slope'] = data.loc['revenue_growth'].rolling(window=3, axis=1).apply(slope_reg)
            print(finance_data)


            #data.to_csv('D:\data\AAAFinance_2022_01_22.csv', mode='a')
            # else:
        # print(i, ' 번 째 ', ticker, ' : NO DATA PASS')
    except Exception as e:
        print(i, ' 번 째 오류 발생 : ', ticker, ' 오류:', str(e))
finance_data.to_csv('D:\data\AAAFinance_temprray2022_01_22.csv')
finance_data.columns = ["Ticker", "Area", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021","TTM"]

finance_data.to_csv('D:\data\AAAFinance_2022_01_22.csv')

#df['SMA_slope_30'] = df['SMA_30'].rolling(window=20).apply(slope_reg)
