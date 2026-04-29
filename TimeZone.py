from datetime import datetime
import pytz

a=pytz.timezone("Asia/Tokyo")
b=datetime.now(a)
print(b)

for i in pytz.all_timezones:
    print(i)
