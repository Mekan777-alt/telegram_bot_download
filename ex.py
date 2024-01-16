from datetime import datetime, timedelta

now = datetime.now()
one_day = timedelta(days=1)
new_date = now + one_day

date = new_date - now
print(date.total_seconds() // 60 // 60)