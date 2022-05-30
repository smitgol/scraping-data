import schedule
import time
import os

print('Scheduler initialised')
schedule.every(10).seconds.do(lambda: os.system('scrapy crawl stock -o items.csv'))
print('Next job is set to run at: ' + str(schedule.next_run()))

while True:
    schedule.run_pending()
    time.sleep(1)
