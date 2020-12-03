from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from datetime import date, datetime

def periodic_task(val):
    print(f'I am a periodic task with the input {val}')
scheduler = BackgroundScheduler(daemon=True)# the daemon=True parameter allows killing the thread when main program exits
# add job
# date as a trigger using date only
scheduler.add_job(periodic_task,'date',run_date=date(2020, 12, 3),args=['Date as the trigger'])
# date as a trigger using date and time
scheduler.add_job(periodic_task,'date',run_date=datetime(2020, 12, 3, 10, 31, 0),args=['Date as the trigger'])

# run the provide function every minute
scheduler.add_job(periodic_task,'interval',seconds=3,args=['Input to background task'])
# print all jobs every 5   secnds
scheduler.add_job(lambda : scheduler.print_jobs(),'interval',seconds=5)
# using the cron trigger. Run every minute
scheduler.add_job(periodic_task,'cron',minute='*',args=['Fancy function'])

#start job
scheduler.start()
app = Flask(__name__)
if __name__ == "__main__":
    app.run('0.0.0.0',port=5001)