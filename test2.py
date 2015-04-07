# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 09:40:45 2015

@author: tim
"""

import ystockquote

from pprint import pprint



abc = ystockquote.get_all('GOOG')

#print(ystockquote.get_all('GOOG'))


stock_list =['previous_close', 'shares_owned', 'change_from_52_week_low', 'revenue', 'average_daily_volume', 'todays_range_realtime', 'today_open', 'last_trade_realtime_time', 'fiftytwo_week_high', 'ebitda', 'fifty_sma', 'pe_realtime', 'ask_realtime', 'percent_change_50_sma', 'percent_change_from_52_week_low', 'price_paid', 'pe', 'holdings_value', 'price_eps_estimate_next_year', 'dividend_per_share', 'twohundred_sma', 'trade_links', 'market_cap', 'todays_value_change_realtime', 'change_realtime', 'low_limit', 'volume', 'todays_high', 'ask_size', 'holdings_gain', 'shares_outstanding', 'holdings_gain_realtime', 'last_trade_price', 'notes', 'change_percent', 'change_percent_realtime', 'ticker_trend', 'todays_low', 'bid_realtime', 'change_50_sma', 'more_info', 'price_book', 'price_eps_estimate_current_year', 'order_book_realtime', 'todays_range', 'change_from_52_week_high', 'book_value', 'market_cap_realtime', 'dividend_yield', 'percent_change_from_52_week_high', 'holdings_gain_percent', 'stock_exchange', 'annualized_gain', 'high_limit', 'todays_value_change', 'short_ratio', 'company_name', 'trade_date', 'dividend_pay_date', 'change_200_sma', 'peg', 'bid_size', 'last_trade_time_plus', 'eps_estimate_next_quarter', 'eps_estimate_current_year', 'fiftytwo_week_range', 'fiftytwo_week_low', 'last_trade_date', 'holdings_value_realtime', 'ex_dividend_date', 'after_hours_change_realtime', 'price_sales', 'change', 'eps_estimate_next_year', 'holdings_gain_percent_realtime', 'eps', 'one_year_target', 'last_trade_time', 'float_shares', 'change_percent_change', 'last_trade_size']


for i in stock_list:
    print i,abc[i]
    

#print(ystockquote.get_bid_realtime('GOOGL'))

#pprint(ystockquote.get_historical_prices('GOOGL', '2013-01-03', '2013-01-08'))
