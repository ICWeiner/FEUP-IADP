from dateutil.relativedelta import relativedelta
from datetime import datetime

datetime.fromtimestamp(1485714600).strftime("%A, %B %d, %Y %I:%M:%S")


start_seconds  = int(input("Number of seconds since the epoch of the first date:"))
end_seconds = int(input("Number of seconds since the epoch of the second  date:"))

start_date = datetime.fromtimestamp(start_seconds)
end_date = datetime.fromtimestamp(end_seconds)



difference_in_years = relativedelta(end_date, start_date).years


print("Number of years between " + str(start_date.date()) + " and " + str(end_date.date()) + " = " + str(difference_in_years))