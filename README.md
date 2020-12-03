# py-schedule
Learning task scheduling in Python and Django using APScheduler

# Trigger examples

## Interval Examples
Interval trigger is used when you want to run a job
at fixed intervals. eg every x minutes evey y hours etc
Sample use cases include:
Run a job every 4 hours
```python
sched.add_job(function, 'interval', hours=4)
```
Give the job a bound usng start and end times such that the task is executed every X hours within this time frame
```python
sched.add_job(function, 'interval', hours=4, start_date='2020-11-11 09:00:00', end_date='2021-01-25 11:00:00'
```
Run job every 2 weeks. To run the job monthly, set weeks=4
```python
sched.add_job(function, 'interval', weeks=2)
```
## Cron Examples
Used when you want to run a job periodically.
eg run job every 5th minute of every hour
run job every tuesday on 5 am
run a job every 3rd tuesday of the month
Some use cases include:

Schedule a task to run during summer(june to august) and winter(December to february)
on every 3rd friday at 2 AM, 3 AM, 4 AM and 5 AM
```python
sched.add_job(job_function, 'cron', month='6-8,12,1-2', day='3rd fri', hour='2-5')
```

Schedule task to run every last friday of the month. This can be to pay salaries
```python
sched.add_job(job_function, 'cron', day='last fri')
```

Schedule task to run hourly. Can be a data scrapping and analysis function
```python
sched.add_job(job_function, 'cron', hour='*')
```

Schedule a system maintenance script that runs hourly on the weekends from 1 AM to 5 AM
```python
sched.add_job(maintenance_func, 'cron', day_of_week['sat','sun'],hour=1-5')
```

Use combined triggers to generate new parameters eg,
Run a maintenance function every 2 hours on select days when you know traffic is less on your site.
```python
from apscheduler.triggers.combining import AndTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger


trigger = AndTrigger([IntervalTrigger(hours=3),
                      CronTrigger(day_of_week='sat,sun')])
scheduler.add_job(job_function, trigger)
```
Schedule a routine task to run every Sunday at 8 AM and every Friday at 1 PM to 3 PM
Could be a reminder task for Christians and Muslims to have their devotion
```python
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger
trigger = OrTrigger([CronTrigger(day_of_week='sun', hour=8),
                     CronTrigger(day_of_week='fri', hour='13-15')])
scheduler.add_job(devotion_reminder, trigger)
```
## Run_Date Examples
Used when you want to run a task at a particular date and time
```python
from datetime import datetime
scheduler.add_job(function,'date',run_date=datetime(2020, 12, 3, 10, 31, 0))
```
# SaaS Scenario Example
Take the example of a SaaS. It wishes to be sending newsletters every last friday of the month to its audience
The newsletter can be containing round ups for the month. You can also use an `OrTrigger` to combine
and have weekly triggers, eg every friday and monthly triggers eg every last sunday of the month
```python
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger
# single monthly newsletter job
sched.add_job(news_letter_send, 'cron', month='*')
# every month on specified day
sched.add_job(news_letter_send, 'cron', day='first mon')
# combine weekly and monthly
trigger = OrTrigger([CronTrigger(day_of_week='fri', hour=8),
                     CronTrigger(day='last fri', hour='7')])
scheduler.add_job(news_letter_send, trigger)
```

A function to check if your users are due for payment of your SaaS.
You would like this to run daily at a time when the traffic is not too much, lets say 1 AM
If payment is due the function sends email
```python
sched.add_job(check_payment_due, 'cron', day='*', hour=1)
```

A function that sends reminders and an invoice that payment is due.
The trigger will be the same, only that this function