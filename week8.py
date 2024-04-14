import datetime as dt

#1. For how many seconds have you been alive?
birth_date = dt.datetime(year = 1997, month=8, day=23, hour=1,minute=1)
dt_now = dt.datetime.now()
alive=dt_now - birth_date
seconds = alive.total_seconds()
res = "I have been alive for "+str(seconds) + " seconds."
print(res)

#How old will you be in 1,340 days
days = 1340
total = dt.datetime.now() + dt.timedelta(days=days)
alive = total - birth_date
myage = alive.days/365
res= 'In '''+str(days)+''' days, I will be '''+str(myage)+ ' years old.'
print(res)