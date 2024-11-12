import backtrader as bt

class StrategyBase(bt.Strategy):
    params = (
        ('printlog', False),
        ('strategy_name', "TrategyBase")
    )
    def log(self, txt, dt=None, doprint = False):
        if self.params.printlog or doprint:
            dt = dt or self.datas[0].datetime.date(0)
            print('%s %s %s' % (self.params.strategy_name,dt.isoformat(), txt))

    def __init__(self):
        self.dataclose = self.datas[0].close

        self.order = None
        self.buyprice = None
        self.buycomm = None # 佣金

        self.sma5  = bt.indicators.SimpleMovingAverage(self.datas[0], period=5)
        self.sma10 = bt.indicators.SimpleMovingAverage(self.datas[0], period=10)
        self.sma20 = bt.indicators.SimpleMovingAverage(self.datas[0], period=20)
        self.sma30 = bt.indicators.SimpleMovingAverage(self.datas[0], period=30)
        self.sma60 = bt.indicators.SimpleMovingAverage(self.datas[0], period=60)

        self.total_profit = 0.0     # 总利润
        self.positive_trades = 0    # 净利润为正的次数
        self.negative_trades = 0    # 净利润为负的次数
        self.buy_date = None        # 买入日期      
        self.sell_date = None       # 卖出日期
        self.total_holding_days = 0 # 总持股天数

        # macd, 三条线(macd, signal, histro) ,分别代表 DIF，DEA，MACD bar值
        self.macd = bt.indicators.MACDHisto(self.datas[0]) 
    
    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
 
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('已买入, 价格：%.2f, 费用：%.2f, 佣金： %.2f' % 
                         (order.executed.price,
                         order.executed.value,
                         order.executed.comm), doprint=False)
                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            elif order.issell():
                self.log('已卖出, 价格： %.2f, 费用：%.2f, 佣金：%.2f' % 
                         (order.executed.price,
                         order.executed.value,
                         order.executed.comm), doprint=False)

            self.bar_executed = len(self)
        
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('订单取消/保证金不足/拒绝', doprint = True)
        
        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return
        self.total_profit += trade.pnlcomm
        if trade.pnlcomm > 0:
            self.positive_trades += 1
        else:
            self.negative_trades += 1
        self.log("交易利润, 毛利润 %0.2f, 净利润: %0.2f, 总利润: %0.2f, 胜率: %.2f" % 
                 (trade.pnl, trade.pnlcomm, self.total_profit, self.positive_trades/(self.positive_trades + self.negative_trades)))
        duration = self.sell_date - self.buy_date
        #print(self.buy_date, self.sell_date, duration.days)
        self.total_holding_days += duration.days

    def is_long_market(self):
        is_sma30_up = self.sma30[0] > self.sma30[-1] and self.sma30[-1] > self.sma30[-2]
        return  is_sma30_up and self.dataclose[0] > self.sma60[0]
    
    def is_buy_point(self):
        return False
    
    def is_sell_point(self):
        return False

    def next(self):
        #self.log('Close, %.2f, sma[10]: %0.2f' % (self.dataclose[0], self.sma[0]))
        if self.order:
            return

        if not self.position:
            if self.is_long_market():
                #if self.macd.histo[-1] < 0 and self.macd.histo[0] > 0:
                if self.is_buy_point():
                    self.log('买入 %.2f, dif: %.2f' % (self.dataclose[0], self.macd.macd[0]), doprint= True)
                    self.order = self.order_target_percent(target=0.99)
                    self.buy_date = self.datas[0].datetime.date(0)
                #self.order = self.buy()
        else:
            if self.is_sell_point():
                self.percent = (self.dataclose[0] - self.buyprice) / self.buyprice
                self.log('卖出 %.2f, DIF: %.2f, 盈亏 %.2f %%' % (self.dataclose[0], self.macd.macd[0], self.percent*100), doprint= True)
                self.order = self.close()
                self.sell_date = self.datas[0].datetime.date(0)
                
    def stop(self):
        self.log("期末资金 %.2f" % self.broker.getvalue())
        self.log("持股天数：%f" %self.total_holding_days, doprint=True)

class MacdCrossStrategy(StrategyBase):
    """依据多方市场 Macd 金叉，死叉原则的交易系统"""
    params = (
        ('printlog', False),
        ('strategy_name', "MacdCrossStrategy")
    )
    def __init__(self):
        super().__init__()
    
    def is_buy_point(self):
        return self.macd.histo[-1] < 0 and self.macd.histo[0] > 0
    
    def is_sell_point(self):
        return self.macd.histo[-1] > 0 and self.macd.histo[0] < 0

class MacdDIFStrategy(StrategyBase):
    """依据多方市场DIF穿越0轴原则的交易系统"""
    params = (
        ('printlog', False),
        ('strategy_name', "MacdDIFStrategy")
    )
    def __init__(self):
        super().__init__()
    
    def is_buy_point(self):
        return self.macd.macd[-1] < 0 and self.macd.macd[0] > 0
    
    def is_sell_point(self):
        return self.macd.macd[-1] > 0 and self.macd.macd[0] < 0

class Sma10Strategy(StrategyBase):
    """依据多方市场10日均线向上向下原则的交易系统"""
    params = (
        ('printlog', False),
        ('strategy_name', "Sma10Strategy")
    )
    def __init__(self):
        super().__init__()
    
    def is_buy_point(self):
        return self.sma10[-1] < self.sma10[0] and self.sma10[-2] < self.sma10[-1]
    
    def is_sell_point(self):
        return self.sma10[-1] > self.sma10[0] and self.sma10[-2] > self.sma10[-1]