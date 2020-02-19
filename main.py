import datetime
import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta, date
from matplotlib import cm

graph_list = []


starting_value = 0

bi_month = 0
AIP_OTB = 0
vacation_payout = 0

expensese = [
    ("KA", 15, 168),
    ("CI", 5, 108),
    ("Host Gator", 17, 11.95),
    ("Geico", 10, 138.57),
    ("Google Payments", 5, 4.99),
    ("Goolge Drive", 17, 1.99),
    ("Youtube Premium", 12, 11.99),
    ("medical", 1, 200),
    ("Dumbo", 15, 350)
]

### One Time Incomes

OTI = [
    ["Food Reimbursement", "2020-03-25", 29.64],
    ["API Bonus", "2020-03-25", 850.00],
    ["Paycheck - Feb Part 2", "2020-02-25", 1775.00],
    ["Last Savings Transfer", "2020-02-25", -750.00],
    ["Paycheck - Mar Part 1", "2020-03-10", 1775.00],
    ["Paycheck - Mar Part 2", "2020-03-25", 1775.00],
    ["Vacation - EOTF, is it prorated?", "2020-04-10", 1775.00*.33],
    ["Tax Refund", "2020-04-30", 1500.00],
]

start_date = date(2020, 2, 18)
#end_date = date(2015, 6, 2)
day_counter = 0

current_funds = 264.90
food_rate = 125/7.0
gas_rate = 35/7.0

x_time = []
y_funds = []


while (current_funds > 0 ):
    current_date = start_date + timedelta(day_counter)


    print(current_date.strftime("%Y-%m-%d"))
    for item in expensese:
        if int(current_date.strftime("%d")) == item[1]:
            current_funds -= item[2]
            print("Check", item[2])


    for item in OTI:
        if current_date.strftime("%Y-%m-%d") == item[1]:
            current_funds+=item[2]

    current_funds -= (food_rate + gas_rate)

    day_counter +=1
    x_time.append(current_date)
    y_funds.append(current_funds)


plt.scatter(x_time, y_funds, c=cm.hot(np.abs(y_funds)/10000), edgecolors='none')
plt.plot(x_time, y_funds)
plt.show()

