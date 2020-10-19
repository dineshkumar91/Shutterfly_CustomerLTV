import unittest
from datetime import datetime
import sys
sys.path.insert(0, '../src')
from simpleltv import *

class Testsimpleltv(unittest.TestCase):

    # Test 1: Provided a sample input file to test the working of json_parser funtion
    def test_json_parser(self):
        self.assertEqual(json_parser("test_input.txt"),[{"type": "CUSTOMER", "verb": "NEW", "key": "cust_12345", "event_time": "2020-10-15T12:46:46.384Z"}])

    # Test 2: Test if the function raises an error when input file is not present 
    def test_no_input_file(self):        
        self.assertRaises(FileNotFoundError,json_parser,"../input/random.txt")

    # Test 3: Test if dollar value is extracted properly
    def test_dollar_amount(self):
        self.assertEqual(amount("10.50 USD"),10.50)
        
    # Test 4: Corner case - Test if null values are handled
    def test_null_dollar_amount(self):    
        self.assertEqual(amount(""),0)

    # Test 5: Test if the difference in number of weeks is computed correctly
    def test_week_difference(self):
        self.assertEqual(week_difference([datetime(2020, 1, 6),datetime(2020, 1, 13), datetime(2020, 1, 21),datetime(2020, 1, 23)]),3)

    # Test 6: Corner case - If all events occur on the same day, the week output should be 1 not 0
    def test_week_difference_zero(self):
        self.assertEqual(week_difference([datetime(2020, 1, 6),datetime(2020, 1, 6)]),1)

    # Test 7: Test if the ingest funtion updates the D2(customer_expenditure) dictionary
    def test_ingest_order(self):
        e = {"type": "ORDER", "verb": "NEW", "key": "68d84e5d1a43", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "cust_1", "total_amount": "10 USD"}
        self.assertEqual(ingest(e,{},{},[]),({},{'cust_1':10},[]))

    # Test 8: Test if the ingest function updates the D1(customer_site_visits) dictionary and the visit_time array
    def test_ingest_site_visit(self):
        e = {"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f", "event_time": "2020-10-18T12:45:52.041Z", "customer_id": "cust_1", "tags": [{"some key": "some value"}]}
        self.assertEqual(ingest(e,{},{},[]),({'cust_1':1},{},[datetime(2020, 10, 18, 0, 0)]))

    # Test 9: Test the working of the TopXSimpleLTV function by providing sample D1(customer_site_visits), D2(customer_expenditure) and no. of weeks
    def test_TopXSimpleLTV(self):
        D1 = {'cust1':3,
              'cust2':2,
              'cust3':2
             }
        D2 = {'cust1':25,
              'cust2':10,
              'cust3':30
             }
        self.assertAlmostEqual(TopXSimpleLTVCustomers(2,D1,D2,4),{'cust3':39000,'cust1':32500})
        '''
        the calculation here is - for cust_1 = 52 * (3/4) * (25/3) * 100 which equals 32500
                                      cust_2 = 52 * (2/4) * (10/2) * 100 which equals 13000
                                      cust_3 = 52 * (2/4) * (30/2) * 100 which equals 39000                        
        '''
        

