from apscheduler.schedulers.background import BackgroundScheduler

def periodic_task(val):
    print(f'I am a periodic task with the input {val}')
schedule = BackgroundScheduler(daemon=True)# the daemon=True parameter allows killing the thread when main program exits
# add job
# print all jobs every 5   secnds
schedule.add_job(lambda : schedule.print_jobs(),'interval',seconds=5)
# run the provide function every minute
schedule.add_job(periodic_task('Input to background task'),'interval',minutes=1)

#start job
schedule.start()