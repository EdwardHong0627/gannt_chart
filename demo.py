from gannt_chart.ganntchart import GanntChart
from random import randint


class Job:
    def __init__(self, name='test', starting_time=0, processing=5, machine=1):
        self.name = name
        self.starting_time = starting_time
        self.processing_time = processing
        self.machine = machine


job_list = []

for i in range(5):
    job = Job('J'.join(str(i)), randint(0, 25), randint(1, 5))
    job_list.append(job)
file = GanntChart(1, 50, 30)

for j in job_list:
    file.add_job(j.name, j.machine, j.starting_time, j.processing_time, fill='red')

file.save_to_file('demo')
