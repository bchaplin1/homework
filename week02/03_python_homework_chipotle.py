'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
BASIC LEVEL
PART 1: Read in the data with csv.reader() and store it in a list of lists called 'data'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''

import csv

cd 'c:\ml\dat7\data'
with open ('chipotle.tsv','rU') as f:
     data = [row for row in csv.reader(f,delimiter='\t')]
     


'''
BASIC LEVEL
PART 2: Separate the header and data into two different lists.
'''
header = data[0]
data = data[1:]     



'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!
'''


sum([float(d[4].replace('$','')) for d in data])/len(set([d[0] for d in data]))

'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''

drinks = set()
for d in data:
    if d[2] == 'Canned Soda' or d[2] == 'Canned Soft Drink':
        drinks.add(d[3])
        
print drinks
        

'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''
topCt = 0
burritoCt = 0

for d in data:
    if d[2] == 'Burrito' :
        topCt += len(d[3].split('[')[-1].split(','))
        burritoCt+=1
        
avgCt = topCt / float(burritoCt) 
print 'average number of toppings per burrito is ' + str(avgCt)        


'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''
from collections import defaultdict

chips = [d  for d in data if d[2].startswith('Chips')]
d = defaultdict(int)
for order in chips:
    d[order[2]]+=int(order[1])

print d.items()    
    



'''
BONUS: Think of a question about this data that interests you, and then answer it!
'''
'''
is there a correlation between meat selection and toppings, like fat content?
let's put them in a dictionary and find out
'''

chicken = [d  for d in data if d[2].startswith('Chicken')]
steak = [d  for d in data if d[2].startswith('Steak')]

orderSum = 0

print 'chicken' + str(sum([float(d[4].replace('$','')) for d in chicken])/len(set([d[0] for d in chicken])))
print 'steak' + str(sum([float(d[4].replace('$','')) for d in steak])/len(set([d[0] for d in steak])))


