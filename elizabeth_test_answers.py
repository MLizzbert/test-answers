import re
import numpy as np
import sorting
import random
import psycopg2
from sorting import bubble
from scipy import stats
from numpy import var


# A - Extraction of colors from html file
html_text = open('python_class_test.html', 'r')
pdata = html_text.read()
html_text.close()

txt = re.compile(r'<td>(.*?)[,](.*?)</td>')
data = txt.findall(pdata)
print(data)


# B - Storing in a dictionary
html_ = open('python_class_test.html').read()
pdatt = re.findall('YELLOW', html_)
pdatt1 = re.findall('BROWN', html_)
pdatt2 = re.findall('WHITE', html_)
pdatt3 = re.findall('BLUE', html_)
pdatt4 = re.findall('BLACK', html_)
pdatt5 = re.findall('ORANGE', html_)
pdatt6 = re.findall('GREEN', html_)
pdatt7 = re.findall('PINK', html_)
pdatt8 = re.findall('RED', html_)
pdatt9 = re.findall('ARSH', html_)
pdatt10 = re.findall('BLEW', html_)
pdatt11 = re.findall('CREAM', html_)

dat = [pdatt, pdatt1, pdatt2, pdatt3, pdatt4, pdatt5, pdatt6, pdatt7, pdatt8, pdatt9, pdatt10, pdatt11]
print(dat)

z = []
for w in dat:
    for x in w:
        z.append(x)
print(z)
print(len(z))

freq = {"YELLOW":0, "BROWN":0, "WHITE":0, "BLUE":0, "BLACK":0, "ORANGE":0, "GREEN":0, "PINK":0, "RED":0, "ARSH":0, "BLEW":0, "CREAM":0}

for dat in z:
    if dat in freq:
        freq[dat]+=1

    else:
        freq[dat]=1

print(freq)

# B
q = list(freq.values())  # To convert dict to list of values
print(q)
print(len(q))

# B 1
value = np.mean(q)  # To calculate the mean of values
print(value)

if value == 9:  # To know if their's a mean color or not
    print('The mean color is ORANGE and RED')
else:
    print('No mean color')

# B 2
highest_freq = 30
if highest_freq >= 30:   # To determine the mostly worn color of shirt in the week
    print("The color mostly worn throughout the week is BLUE")
else:
    print("Others")

# B 3
value1 = sorting.bubble(q)   # To determine the color that is median
print(value1)
value1a = np.median(value1)
print(value1a)

if value1a >= 5.5:
    print("The color that is median is YELLOW AND PINK")
else:
    print("No median color")

# B 4
value2 = np.var(q)  # To get the variance of colors
print(value2)   # value2 is the variance of colors

# B 5
value3 = stats.probplot(q)   # value3 is the color is red
print(value3)   # value3 is the probability that the color is red

# B 6
freq =[("1", "YELLOW", "5"), ("2", "BROWN", "6"), ("3", "WHITE", "16"), ("4", "BLUE", "30"), ("5", "BLACK", "1"),
       ("6", "ORANGE", "9"), ("7", "GREEN", "10"), ("8", "PINK", "5"), ("9", "RED", "9"), ("10", "ARSH", "1"),
       ("11", "BLEW", "1"), ("12", "CREAM", "2")]

def InsertData(Data):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="gfR12",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="ml_db")
        cursor = connection.cursor()

        #to print postgres version
        print(connection.get_dsn_parameters(), "\n")

        # printing the postgres version
        cursor.execute("SELECTversion ();")
        record=cursor.fetchone()
        print("you are connected to -",record, "\n")

        sql_insert_query = """ INSERT INTO ml_dbschema, "Color" (id, color. VALUES (%s, %s, %s)"""

#B 7
# Recursive function to search x in arr[l..r]
def recSearch(arr, l, r, x):
    if r < l:
        return -1
    if arr[l] == x:
        return l
    if arr[r] == x:
        return r
    return recSearch(arr, l + 1, r - 1, x)


# Driver Code
arr = [12, 34, 54, 2, 3]
n = len(arr)
x = 3
index = recSearch(arr, 0, n - 1, x)
if index != -1:
    print("Element", x, "is present at index %d" % (index))
else:
    print("Element %d is not present" % (x))

# Number 8

# Creating a set of digits: {0, 1, .... 9}
digits = set(range(10))
# Generating a random integer, 1 <= first <= 9
first = random.randint(1, 9)
# Removing it from the set, then take a sample of
# 3 distinct elements from the remaining values
last_3 = random.sample(digits - {first}, 3)
print(str(first) + ''.join(map(str, last_3)))
index = recSearch(arr, 0, n - 1, x)
if index != -1:
    print("Element", x, "is present at index %d" % (index))
else:
    print("Element %d is not present" % (x))

# Number 9 - Fibonacci sequence
x, y = 0, 1

while y < 50:
    print(y)
    x, y = y, x + y



