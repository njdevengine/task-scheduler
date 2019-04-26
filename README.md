## Time Turtle Task Scheduler :alarm_clock: :turtle:
# What is Time Turtle?
Time Turtle schedules scripts to run on your machine.
It considers the workhour to run only during workhours.
I made it because I am trying to automate data cleaning processes,
I also made it so that others can trigger my code without knowing Python.
They can drop a file to be checked against our database in a shared drive folder.
Time Turtle will see the changes in modified date timestamps and execute different scripts.

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
Happy Automating! :computer:
