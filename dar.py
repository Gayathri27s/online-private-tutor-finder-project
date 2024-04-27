
from datetime import datetime
from datetime import timedelta
from datetime import date

Begindatestring = date.today()

# print begin date 
print("Beginning date")
print(Begindatestring)

# calculating end date by adding 4 days 
Enddate = Begindatestring + timedelta(days=4)

# printing end date 
print("Ending date")
print(Enddate) 