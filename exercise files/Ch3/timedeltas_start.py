#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.now()
print("Today is: " + str(now))

# print today's date one year from now
print("One year from now will be: " + str(now + timedelta(days=365)))

# create a timedelta that uses more than one argument
print("in 2 days a 3 weeks it will be:" + str(now + timedelta(days=2, weeks=3)))

# calculate the date 1 week ago, formatted as a string
# print("two weeks ago was:" str(now -))
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %y")
print("one week ago was: " + s)
### How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4, 1)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print("April fools's day allready went by by %d days ago" % ((today-afd).days))
    afd=afd.replace(year = today.year+1)

# Now calculate the amount of time until April Fool's Day  
time_to_afd = afd-today
print("Its just ", time_to_afd.days, "Days until aprril fools day")

