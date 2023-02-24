from datetime import date, timedelta
yest = date.today() - timedelta(1)
tomo = date.today() + timedelta(1)
print('Current Date :',date.today())
print("Yesterday:",yest)
print("Tomorrow:",tomo)