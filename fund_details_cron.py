from crontab import CronTab

# the command path need to be changed according to folder where it is cloned.
cron = CronTab(user='harsh')
job = cron.new(command='python3 /home/harsh/drive/projects/mf-details-scrapper/run.py', comment='mf-details-cron')

job.setall('0 9,13,17 * * 1-5')
cron.write()


# cron.remove_all() to remove all the jobs 