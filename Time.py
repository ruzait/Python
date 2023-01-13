import datetime


dt1 = date(2022, 7, 14)       # print(dt1)
dt2 = date.today()      # print(dt2)
dt3 = date.today()   # print(dt3.month)    # print(dt3.year)   # print(dt3.day)

dt4 = date.isoformat(dt2)       # print(dt4) 1-mon, 2-tus...

dt5 = dt3.weekday()         # print(dt5)

print(dt5)

'''

'''# print years ONLY!
import datetime

my = datetime.date(2003, 8, 19)
tm = datetime.date.today()      # 2022-7-14
ag = tm.year - my.year - ((tm.month, tm.day) < (my.month, my.day))  # 2022-2003   07,14   08,19

print(f"{ag} years")'''

'''import time

#print(time.ctime(0))       # convert a time expressed in seconds
#print(time.time())         # return current seconds since epoch
#print(time.ctime(time.time()))

#time_object = time.localtime()
#print(time_object)
#l_time = time.strftime("%d %B %Y   %H:%M:%S", time_object)
#print(l_time)