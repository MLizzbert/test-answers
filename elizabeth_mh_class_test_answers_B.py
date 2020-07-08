import re
html_text = open('python_class_test.html').read()

pdata = re.findall('YELLOW', html_text)
pdata1 = re.findall('BROWN', html_text)
pdata2 = re.findall('WHITE', html_text)
pdata3 = re.findall('BLUE', html_text)
pdata4 = re.findall('BLACK', html_text)
pdata5 = re.findall('ORANGE', html_text)
pdata6 = re.findall('GREEN', html_text)
pdata7 = re.findall('PINK', html_text)
pdata8 = re.findall('RED', html_text)
pdata9 = re.findall('ARSH', html_text)
pdata10 = re.findall('BLEW', html_text)
pdata11 = re.findall('CREAM', html_text)

print(pdata)
print(pdata1)
print(pdata2)
print(pdata3)
print(pdata4)
print(pdata5)
print(pdata6)
print(pdata7)
print(pdata8)
print(pdata9)
print(pdata10)
print(pdata11)

#Storing in dictionary
thisdict =	{
  "YELLOW": 5,
  "BROWN": 6,
  "WHITE": 16,
  "BLUE": 30,
  "BLACK": 1,
  "ORANGE": 9,
  "GREEN": 10,
  "PINK": 5,
  "RED": 9,
  "ARSH": 1,
  "BLEW": 1,
  "CREAM": 2
}

print(thisdict)

values = [5, 6, 16, 30, 1, 9, 10, 5, 9, 1, 1, 2]


#Number 1
import numpy as np

value = np.mean(values)
print(value)  

if value >= 7.9:
  print('The mean color is ORANGE and RED')
else:
  print('No mean color')  


#Number 2
import sorting
from sorting import bubble
from scipy import stats

value1 = sorting.bubble(values)

print(value1)

value1a = stats.mode(value1)
print(value1a, 'BLACK, ARSH, and BLEW are mostly worn throughout the week')


# NUmber 3
value2 = np.median(value1)
print(value2)

if value2 >= 5:
  print('The median color is YELLOW and PINK')
else:
  print('No median color')    
        

# Number 4 - the variance of colors
value3 = np.var(values)
print(value3, 'is the variance of colors')


# Number 5 - probability 
value4 = stats.probplot(values)
print(value4, 'is the probability that the color is RED')


# Number 6
import psycopg2
from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection




# Number 7
# Recursive function to search x in arr[l..r]  
def recSearch( arr, l, r, x): 
    if r < l: 
        return -1
    if arr[l] == x: 
        return l 
    if arr[r] == x: 
        return r 
    return recSearch(arr, l+1, r-1, x) 
  
# Driver Code  
arr = [12, 34, 54, 2, 3] 
n = len(arr) 
x = 3
index = recSearch(arr, 0, n-1, x) 
if index != -1: 
    print("Element", x,"is present at index %d" %(index))
else: 
    print("Element %d is not present" %(x))


# Number 8
import random
# Creating a set of digits: {0, 1, .... 9}
digits = set(range(10))
# Generating a random integer, 1 <= first <= 9
first = random.randint(1, 9)
# Removing it from the set, then take a sample of
# 3 distinct elements from the remaining values
last_3 = random.sample(digits - {first}, 3)
print(str(first) + ''.join(map(str, last_3)))
index = recSearch(arr, 0, n-1, x) 
if index != -1: 
    print("Element", x,"is present at index %d" %(index) )
else: 
    print("Element %d is not present" %(x))

# Number 9 - Fibonacci sequence
x,y=0,1

while y<50:
    print(y)
    x,y = y,x+y
