from apscheduler.schedulers.background import BackgroundScheduler

schedule = BackgroundScheduler(daemon=True)# the daemon=True parameter allows killing the thread when main program exits
