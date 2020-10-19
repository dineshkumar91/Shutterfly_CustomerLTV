# Shutterfly_CustomerLTV
Coding challenge from shutterfly

# Overview - Simple LTV Calculation
Simple LTV is calculated using the equation 52(a) x t (t = 10 years)
The main focus of this assignment is to compute the value for 'a'

where a = customer expenditure per visit x number of visits per week
customer expenditure per visit = Total amount spent by the customer / Total no. of site visits by the customer
number of site visits per week = Total no. of visits by the customer / Total no. of weeks in consideration

Total no. of weeks in consideration (timeframe) is obtained by subtracting the earliest event date and the latest event date. 
Sunday is considered to be the start of the week

# Directory strtucture
- src (Source code is present here - src/simpleltv.py)
- input (Input data is provided here - input/input/txt)
- output (The output simple LTV information is saved as a text file - output/output.txt)
- sample_input (One event for each type is provided here)
- tests (Unittest cases written to test the code as provided here - tests/test_simpleltv.py, a sample test input file is also provided - tests/test_input.txt)
