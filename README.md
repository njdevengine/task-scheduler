## Time Turtle Task Scheduler :alarm_clock:

![turtle time](time.png)

## Script is best run on a server or localhost
* I ran my code in Jupyter Notebook so its always running.
* Sniffs for changes and conditions including whether or not its a workday/workhour.
* Executes multiple scripts on a fifteen minute timer.
* Calculates time until next workday at 6pm and Weekends and sleeps til then.

```
#put me in the while loop to add scripts
task('task name string',r'path:to\changes\\','python script_filename.py')
```
Happy Automating!
