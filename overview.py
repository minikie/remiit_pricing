# coding=utf-8
import xenarix as xen
import xenarix.sample as xen_s
import xenarix.results as xen_r

# xen.set_repository('c:\repository')

# generation setting
maxyear = 5

# assuption
total_remittance_amount = 30000000000 # 30억 (월간)
remittance_marketshare_ratio = 0.3

remi_issue_amount = 11500000000 # 115억개
remi_circulation_amount = 5000000000 # 50억개
remittance_fee = 0.015
dividend_ratio = 0.7
IEO_price = 1
market_capitalization = remi_circulation_amount * IEO_price
rf = 0.015
per = 0.05

total_profit = 0
total_discounted_profit = 0
# 1년간만 뿌림
for month in range(1,12):
    holder_profit = total_remittance_amount * remittance_marketshare_ratio * remittance_fee * dividend_ratio
    total_profit += holder_profit
    total_discounted_profit += holder_profit / ((1.0+rf)**(month/12.0))


remi_yield = total_discounted_profit / remi_circulation_amount
expected_price = remi_yield / per

print 'total profit : ' + str(total_profit)
print 'total discounted profit : ' + str(total_discounted_profit)
print 'yield : ' + str(round(remi_yield * 100, 2)) + ' %'
print 'expected price : ' + str(expected_price)