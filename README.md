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
## Run_Date Examples
Used when you want to run a task at a particular date and time
# SaaS Scenario Example
