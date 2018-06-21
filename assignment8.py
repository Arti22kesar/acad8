#Ques1.

print("we represents time in a waythat's easy for us to understand. However,python stores it in tuples"
      "These python are made of nine numbers.."
    "INDEX   FIELD            DOMAIN OF VALUE"
      "0     Year(4digits)     ex-1995"
      "1     Month             1to12"
      "2     Day               1to31"
      "3     Hour              0to23"
      "4     Minute            0to59"
      "5     second            0to61"
      "6     Day of week       0to6(MONDAY TO SUNDAY"
      "7     Day of year       1to336(julian day"
      "8     DST               -1,0,1")


#Ques2.

import datetime
d=datetime.datetime.now().strftime('%H: %M: %S')
print(d)

#Ques3.

import datetime
d=datetime.datetime.today()
print(d.month)

#Ques4.

import datetime
d=datetime.datetime.today()
print(d.day)


#Ques5.

import datetime
d=datetime.date.today()
d.strftime("%d %M %Y ")
print(d.day)

#Ques6.

import datetime,time
print(time.asctime(time.localtime()))

#Ques7.
import math
a=int(input("enter a number:"))
print(math.factorial(a))

#Ques8.

import math
a=int(input("enter number:"))
b=int(input("enter number:"))
print(math.gcd(a,b))

#Ques9.1

import os
print(os.getcwd())

#Ques9.2

import os
print(os.environ)