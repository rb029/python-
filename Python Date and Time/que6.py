from datetime import datetime , timedelta
given_date = datetime(2020,3,22,10,00,00)
print("Given date:")
days_to_add= 7
res_date =given_date+timedelta(days=days_to_add,hours=12)
print("New date:")
print(res_date)
