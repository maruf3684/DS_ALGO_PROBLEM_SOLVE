class Date(object):
    def get_date(self):
        return "28/11/2021"

class Time(Date):
    def get_time(self):
        return "8.29 AM"

dt=Date()
tm=Time()
print(tm.get_time())
print(tm.get_date())