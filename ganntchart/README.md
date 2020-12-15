# Installation
`$ pip install git+https://github.com/EdwardHong0627/gannt_chart`

# Importing
`from ganntchart.ganntchart import GanntChart`  
# Usage
*  First of all, we need to initialize the blank gannt chart 
with specified number of machine, total length of gannt chart, and the sale size.\
\
i.e.,
```
result =GanntChart(num_of_machine=2, 
                   total_length=50, 
                   scale=20)
```
\
The statement above means that result is an instance of object Gannt Chart.

* Second we can call the add_job function to append a job information:
```
result.add_job(job_name='J_1', 
               machine=0, 
               starting_time=0, 
               processing_time=5)
```
\
* you can also assign the fill-color and stroke-color of jobs in Gannt chart by adding arg in the add job function as below:
```
result.add_job(job_name='J_1', 
               machine=0, 
               starting_time=0, 
               processing_time=5,
               fill= '#00FF00',
               stroke= '#FF00FF')

```
\
* Finally, we can call save_to_file function to save our Gannt chart as a svg_file  
`result.save_to_file(file_name='result')`