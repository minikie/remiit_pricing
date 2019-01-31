# assumption

# Daily Transaction ( Each country )
# Exchange Rate ( ex) USD/KRW , JPY/KRW ... )
# InterestRate of each country

# result
#

import xenarix as xen

scen_set = xen.ScenSet('testSet')
scen = xen.Scenario('testScen', 'resultID')

usd_curve = None
krw_curve = None
jpy_curve = None

vasicek_usd = None
vasicek_krw = None
vasicek_jpy = None

# fx model
usd_krw_fx = None
jpy_krw_fx = None
usd_jpy_fx = None

#

scen.add_model(vasicek_usd)
scen.add_model(vasicek_krw)
scen.add_model(vasicek_jpy)
scen.add_model(usd_krw_fx)
scen.add_model(jpy_krw_fx)
scen.add_model(usd_jpy_fx)



