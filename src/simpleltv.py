from datetime import datetime, timedelta
import json

# Function to load json data from an input file and save as a list(events)
def json_parser(input_file):
    try:
        input_data = open(input_file,"r")
    except FileNotFoundError:
        raise
    events = json.load(input_data)
    input_data.close()
    return events   

# Function to ingest events and updates the customer dictionaries - 'D1'(customer_site_visits) and 'D2'(customer_expenditure)
# O(1) Time
def ingest(e,D1,D2,visit_times):
    if e['type'] == 'SITE_VISIT':
        cust_id = e['customer_id']
        timearray(e['event_time'],visit_times)     
        if cust_id  not in D1:
            D1[cust_id] = 1
        else:
            D1[cust_id] +=1       
    elif e['type'] == 'ORDER':
        cust_id = e['customer_id']
        if e['customer_id'] not in D2:
            D2[cust_id] = amount(e['total_amount'])
        else:
            D2[cust_id] += amount(e['total_amount'])       
    return D1,D2,visit_times

# Function to extract the dollar value - O(1) time
# Corner Case - missing data is considered as 0
def amount(total_amount):
    amount = total_amount.split(' ')[0]
    try:
        dollar_value = float(amount)
        return dollar_value
    except:
        return 0

# Function to append the event time to the 'visit_times' list (as a datetime object)  
def timearray(event_time,visit_times):
    event_time = event_time.split('T')[0]
    eventdate = datetime.strptime(event_time, '%Y-%m-%d')
    visit_times.append(eventdate)
    return

# Function to find the difference in weeks between the earliest event date and the latest event date
# Sunday is considered to be the start of the week
def week_difference(visit_times):
    start_date = min(visit_times)
    end_date = max(visit_times)
    start_date = (start_date - timedelta(days=start_date.weekday()+1))
    end_date = (end_date - timedelta(days=end_date.weekday()+1))
    time_delta = end_date - start_date
    week_delta = time_delta.days / 7
    return int(week_delta) + 1

# Function that takes the customer information as input, computes LTV and displays the top x results             
# O(NlogN) Time
def TopXSimpleLTVCustomers(x,D1,D2,total_weeks):
    LTV = dict()
    for key,value in enumerate(D1):
        '''
        Simple LTV is calculated with the formula 52 * a * t (here t = 100)
        a = customer expenditure per visit * number of visits per week
        customer expenditure per visit = Total amount spent by the customer / Total no. of site visits by the customer
        number of site visits per week = Total no. of visits by the customer / Total no. of weeks in consideration
        '''
        cust_expenditure = D2[value] / D1[value]
        visits_per_week = D1[value] / total_weeks
        simple_ltv = 52 * cust_expenditure * visits_per_week * 100
        '''
        In the above calculation it can be seen that the total no. of visits by the customer is not needed
        simple ltv can be calculated by this alternate equation without using D1 (customer_site_visits)
        ltv = 52 * D2[value] * 100 / total_weeks
        However, I have used no. of site visits in the calculation as it an important metric
        '''
        if value not in LTV:
            LTV[value] = simple_ltv
    LTV = dict(sorted(LTV.items(), key=lambda y: y[1], reverse=True)[:x])
    print(f'The Top {x} customers and their corresponding LTV values are')
    for key,value in enumerate(LTV):
        print(f'Customer ID: {value}     LTV: {round(LTV[value],2)}')
    return LTV      

# Funtion to save the output simple LTV information as a text file
def output_file(output_file_name,output_data):
    with open(output_file_name,'w') as f:
        for key,value in enumerate(output_data):
            f.write(f'Customer ID: {value}     LTV: {round(output_data[value],2)}\n')
    return
    
if __name__ == "__main__":
    D1 = dict()
    D2 = dict()
    visit_times = []
    events = json_parser("../input/input.txt")
    for event in events:
        D1,D2,visit_times = ingest(event,D1,D2,visit_times)
    x = int(input("Please enter an integer value between 1 to 5:\n"))
    if 1 <= x <=5:
        total_weeks = week_difference(visit_times)
        output_data = TopXSimpleLTVCustomers(x,D1,D2,total_weeks)
    else:
        print("Incorrect number provided")
    output_file("../output/output.txt",output_data)      
