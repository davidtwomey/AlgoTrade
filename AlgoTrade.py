from yahoo_finance import Share
from pprint import pprint #for more readable historical data output
import json

class AlgoTrade(object):
	''' 
	BACKTEST ALGO STRATEGIES 
	
	TODO:
		1. UPDATE TO UTILISE NUMPY AND MATPLOTLIB FOR VISUAL ANALYSIS
		2. CONNECTION TO BROKERS (INTERACTIVE BROKERS API)
		3. ADD DATA TRANSFORMS - HYPERBOLIC / PCA / RIDGE REGRESSION
		4. ADD FUNCTIONALITY TO ALLOW ONE TO 'PLUG-IN' A STRATEGY
		5. ADD OUR MACHINE LEARNING
	IB: https://www.quantstart.com/articles/using-python-ibpy-and-the-interactive-brokers-api-to-automate-trades 
	
	'''

	def __init__(self,data,period):
		self.data = data
		self.holding_period = int(period)
	
	
	def open_close(self):
		stats = []
		for detail in self.data:
			stats.append(detail['Open'])
			stats.append(detail['Close'])
		return stats
		
		
	def calc_intraday_difference(self, generated_data):
		''' Difference = Close - Open
			Positive = Up Day
			Nagative = Down Day '''
		price_difference = []
		for i in range(0,len(generated_data)):
			if (i == 0):
				pass
			else:
				price_difference.append(float(generated_data[i]) - float(generated_data[i-1]))	
		return price_difference
	
	
	def what_side(self, intra_day_diff):
		trade_side = []
		for j in range(0,len(intra_day_diff)):
			if(intra_day_diff[j] < 0):
				trade_side.append("BUY")
			else:
				trade_side.append("SELL")
		return trade_side
		
		
	def analyse_profit(self, merged_data):
		''' 
		merged_data = [trade_side, price_difference]
		TODO: 
			1. HERE WE WANT TO STORE THE BUY AND SELLS RARHER THAN PRINT
			2. IMPLEMENT QUANTITATIVE ANALYSIS
		'''
		for k in range(0,len(merged_data[0])):
			if(k == 0):
				pass
			elif(k == (len(merged_data[0]) - self.holding_period)):
				break
			else: 
				trade_side = merged_data[0][k]
				trade_direction = merged_data[1][k+self.holding_period]
				if (trade_side == "BUY" and trade_direction > 0.0):
					print "PROFIT ON BUY - 3 DAY TRADE"
				elif (trade_side == "SELL" and trade_direction < 0.0):
					print "PROFIT ON SELL - 3 DAY TRADE"
				else:
					print "LOST MONEY"