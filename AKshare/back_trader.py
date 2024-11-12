import backtrader as bt
import akshare as ak
import pandas as pd
import time
import datetime
import os.path
import sys

class TestStrategy(bt.Strategy):
    params = (
        ('exitbars', 5),
    )
    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print('%s %s' % (dt.isoformat(), txt))

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.order = None
        self.buyprice = None
        self.buycomm = None
    
    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
 
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('已买入, 价格：%.2f, 费用：%.2f, 佣金： %.2f' % 
                         (order.executed.price,
                         order.executed.value,
                         order.executed.comm))
                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            elif order.issell():
                self.log('已卖出, 价格： %.2f, 费用：%.2f, 佣金：%.2f' % 
                         (order.executed.price,
                         order.executed.value,
                         order.executed.comm))

            self.bar_executed = len(self)
        
        elif order.status in [order.Canceled, order.Margin, order.Rejecteed]:
            self.log('订单取消/保证金不足/拒绝')
        
        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return
        self.log("交易利润, 毛利润 %0.2f, 净利润: %0.2f" % (trade.pnl, trade.pnlcomm))

    def next(self):
        self.log('Close, %.2f' % self.dataclose[0])
        if self.order:
            return

        if not self.position:
            if self.dataclose[0] < self.dataclose[-1]:
                if self.dataclose[-1] < self.dataclose[-2]:
                    self.log('买入，%0.2f' % self.dataclose[0])
                    self.order = self.buy()
        else:
            if len(self) >= (self.bar_executed + self.params.exitbars):
                self.log('卖出， %.2f' % self.dataclose[0])
                self.order = self.sell()

cerebro = bt.Cerebro()

cerebro.addstrategy(TestStrategy)

stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="002460", period="daily", start_date="20170301", end_date='20241102', adjust="qfq").iloc[:,:7]
del stock_zh_a_hist_df['股票代码']
stock_zh_a_hist_df.columns = [
    'date',
    'open',
    'close',
    'high',
    'low',
    'volume'
]
stock_zh_a_hist_df.index = pd.to_datetime(stock_zh_a_hist_df['date'])
start_date = datetime.datetime(2023, 11, 2)
end_date = datetime.datetime(2024, 11, 2)
data = bt.feeds.PandasData(dataname=stock_zh_a_hist_df, fromdate=start_date, todate=end_date)
cerebro.adddata(data)

cerebro.broker.setcash(100000.0)
cerebro.addsizer(bt.sizers.FixedSize, stake=10)
cerebro.broker.setcommission(commission=0.001)
print('期初资金: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('期末资金: %.2f' % cerebro.broker.getvalue())