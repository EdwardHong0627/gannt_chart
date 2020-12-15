from gannt_chart.ganntchart import GanntChart

svg = GanntChart(1, 30, 20)

starting_time = [0, 3, 8]
processing_time = [3, 5, 10]

for k, v in enumerate(starting_time):
    svg.add_job("J".join(str(k)), 1, v, processing_time[k], fill='#00FF00', stroke='#FF00FF')

svg.save_to_file("demo")
