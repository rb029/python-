from datetime import datetime
from dateutil.relativedelta import relativedelta
given_date = datetime(2020,2,25).date()
months_to_add = 4
new_date = given_date+relativedelta(months=months_to_add)
print(new_date)