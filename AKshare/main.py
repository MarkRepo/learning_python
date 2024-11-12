import backtrader as bt
from strategy import *
import akshare as ak
import datetime
import pandas as pd

def back_trade_stock_daily(area, stock_code, start_date, end_date, strategy):
    cerebro = bt.Cerebro()
    cerebro.broker.set_coc(True)
    #strats = cerebro.optstrategy(TestStrategy, maperiod=range(10, 31))

    cerebro.addstrategy(strategy)

    #cerebro.addanalyzer(bt.analyzers.TimeReturn, _name='pnl')
    cerebro.addanalyzer(bt.analyzers.AnnualReturn, _name="AnnualReturn")

    #stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="600699", period="daily", start_date="20191102", end_date='20241102', adjust="qfq").iloc[:,:7]
    if area == "HSJ": # 沪深京
        stock_history_df = ak.stock_zh_a_hist(symbol=stock_code, period="daily", start_date=start_date, end_date=end_date, adjust="qfq").iloc[:,:7]
        del stock_history_df['股票代码']
    elif area == "HK": # 香港
        stock_history_df = ak.stock_hk_hist(symbol=stock_code, period="daily", start_date=start_date, end_date=end_date, adjust="qfq").iloc[:,:7]
        del stock_history_df['成交额']

    stock_history_df.columns = [
        'date',
        'open',
        'close',
        'high',
        'low',
        'volume'
    ]
    stock_history_df.index = pd.to_datetime(stock_history_df['date'])
    start_date = datetime.datetime(2014, 11, 2)
    end_date = datetime.datetime(2024, 11, 2)
    data = bt.feeds.PandasData(dataname=stock_history_df, fromdate=start_date, todate=end_date)
    cerebro.adddata(data)

    cerebro.broker.setcash(100000.0)
    cerebro.addsizer(bt.sizers.FixedSize, stake=10)
    cerebro.broker.setcommission(commission=0.001)
    print('期初资金: %.2f' % cerebro.broker.getvalue())
    #cerebro.run()
    thestrats = cerebro.run(maxcpus=1)
    thestrat = thestrats[0]
    #print("收益率：", thestrat.analyzers.pnl.get_analysis())
    print("年化收益率: ", thestrat.analyzers.AnnualReturn.get_analysis())

    print('期末资金: %.2f' % cerebro.broker.getvalue())
    #cerebro.plot()

if __name__ == "__main__":
    back_trade_stock_daily("HK", "00700", "20141102", "20241102", MacdCrossStrategy)
    back_trade_stock_daily("HSJ", "002460", "20141102", "20241102", MacdCrossStrategy)
    back_trade_stock_daily("HK", "00700", "20141102", "20241102", MacdDIFStrategy)
    back_trade_stock_daily("HSJ", "002460", "20141102", "20241102", MacdDIFStrategy)
    back_trade_stock_daily("HK", "00700", "20141102", "20241102", Sma10Strategy)
    back_trade_stock_daily("HSJ", "002460", "20141102", "20241102", Sma10Strategy)
