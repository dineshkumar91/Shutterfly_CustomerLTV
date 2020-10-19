# Shutterfly_CustomerLTV
Coding challenge from Shutterfly


# Overview - Simple LTV Calculation
- Simple LTV is calculated using the equation `52(a)` x `t` (here `t` = `10 years`)  
The main focus of this assignment is to compute the value for `a`

   where `a` = customer expenditure per visit x number of visits per week

   	   customer expenditure per visit = Total amount spent by the customer / Total no. of site visits by the customer
         number of site visits per week = Total no. of site visits by the customer / Total no. of weeks in consideration

- Total no. of weeks in consideration (timeframe) is obtained by subtracting the earliest event date and the latest event date. Sunday is considered to be the start of the week.

`Note:` In the formulae mentioned above, it can be seen that the `total no. of site visits by the customer` cancels out.   
LTV can be calculated by an  alternate equation without using the customer_site_visits:       
`52` * `Total amount spent by the customer` * `100` / `Total no. weeks in consideration`
However, in this assignment, the no. of customer site visits are also stored and used since it is an important business metric


# Directory structure
- src (Source code is present here - **src/simpleltv.py**)
- input (Input data is provided here - **input/input.txt**)
- output (The output simple LTV information is saved as a text file - **output/output.txt**)
- sample_input (One event for each type is provided here)
- tests (Unittest cases written to test the code as provided here - **tests/test_simpleltv.py**, a test input data file is also provided here **tests/test_input.txt**)


# Running the code - Input/Output
- The input file **input/input.txt** contains events spread across a few weeks for 5 different customers.  

- Run the source code **src/simpleltv.py**. A user input for the number of customers (X) is required. Enter an integer value between 1 to 5. 
This will display the top X customers and their corresponding LTV information. 

- The output of this program can also be found in the **output/output.txt** file


# Testing
- unittest module has been extensively used to test the code.

- 9 different test cases can be found in the **tests/test_simpleltv.py** file.

- To run unittest, open the shell, go to the `tests` directory containing the test and type `python -m unittest test_simpleltv`


# Design Decisions/Performance
- Two dictionaries are used to store the customer information `D1 (customer_site_visits)` & `D2 (customer_expenditure)`

- A list is used to store all the event times - `visit_times`. The total no. of weeks in consideration is computed from this list

- `ingest()` function updates the customer dictionaries based on event information. It takes O(1) time.

- Missing dollar values (Corner Case) are considered to be `0`.

- `TopXSimpleLTVCustomers` takes the customer dictionaries as input, computes LTV, sorts and displays the top X customers. This takes O(NlogN) time.


# Future Improvement
- Events are processed by the `ingest` function one at a time. Parallel processing techniques can be adopted for performance improvement in the future.

- The `visit_times` list has a space complexity of O(N). To save space, this list can be replaced by two variables that store the start_date and end_date (these variables can be updated after every event) 


# Requirements
unittest
