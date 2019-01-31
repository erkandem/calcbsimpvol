"""
Notes on Data Sets
===================
While it is easy to make up some random data this will not result in
something meaningful since BS is not linear. These data sets are obfuscated
but have the structure real world data would have...if it were real data.

Some notes on the keys of the JSON data files:

cl_20171115.json
^^^^^^^^^^^^^^^^^^^
Data on crude oil with expiry on 15. Nov, 2017

**d20161209**: Data of 09. Dec, 2016

**S**: underlying price

**cp**: call[+1] or put[-1]

**K**: strike price

**P**: option price

**tau**: Time until expiry in years

**moneyness**: Here: log(S/K)

**q**: Here: fictional yield from reinvesting cash above margin threshold for the risk free rate

**r**: risk free rate estimated from treasuries for that specific `time until expiry`

**mlb_rational**: result obtained from `calcBsImpVol.m` with additional proprietary filtering, if needed

**delta**: a raw delta estimate calculated from the iVol from `mlb_rational`

    

reference_sample.json
^^^^^^^^^^^^^^^^^^^^^^
Data taken out of a data collection of a third-party vendor (indicated by (-#-)) and added columns from calculations

**d20170921**: Data of 21. Sep, 2017

**cp**: (-#-)

**P**: (-#-)

**S**: (-#-)

**K**: (-#-)

**tau**: calculated

**r**: calculated

**q**: trailing 12 month dividend yield ESTIMATE

**py_rational**: iVol calculated obtained from calc_ivol.py

**ref_iv_clean(-#-)**: iVol stated in the third-party reference supplied; set to NaN where ``ref_iv_is_interpolated`` was ``true``

**ref_iv_is_interpolated**: proprietary model based interpolation/extrapolation by third party vendor

**mlb_blsimpv_clean**: iVol calculated from the built in function in MATLAB; set to NaN where ``ref_iv_is_interpolated`` was `true`

**mlb_rational_clean**: iVol calculated from calcBsImpVol with additional proprietary filtering, if needed; set to NaN where ``ref_iv_is_interpolated`` was `true`

**py_rational_clean**: raw data obtained from calc_ivol.py; set to NaN where ``ref_iv_is_interpolated`` was ``true``
        
    
spy_20190118.json:
^^^^^^^^^^^^^^^^^^^
SPY options data with expiry on 18. Jan, 2019

**d20171226**: Data of 26. Dec, 2017

**q**: trailing 12 month dividend yield ESTIMATE

"""


