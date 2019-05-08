import time
import datetime
import os
print(r"""
  _   _                _              _   _      
 | | (_)              | |            | | | |     
 | |_ _ _ __ ___   ___| |_ _   _ _ __| |_| | ___ 
 | __| | '_ ` _ \ / _ \ __| | | | '__| __| |/ _ \
 | |_| | | | | | |  __/ |_| |_| | |  | |_| |  __/
  \__|_|_| |_| |_|\___|\__|\__,_|_|   \__|_|\___|
                    __
         .,-;-;-,. /'_\
       _/_/_/_|_\_\) /
     '-<_><_><_><_>=/\
       `/_/====/_/-'\_\
        ""     ""    ""
""")
#start by checking if its Saturday or Sunday
#if it is calc seconds till 9am next business day and sleep
n=0
old_timestamps_a = "start"
old_timestamps_b = "start"

def task_a(name,x,path):
    global old_timestamps_a
# check if its Saturday
    print(name)
    a = datetime.datetime.now()
    if a.isoweekday() == 6:
        a += datetime.timedelta(days=2)
        a = a.replace(hour=9,minute=0,second=0,microsecond=0)
        now = datetime.datetime.now()
        c = a - now
        wait_time = c.seconds
        print('Its Saturday... sleeping',wait_time,"seconds...")
        time.sleep(wait_time)
#check if its Sunday
    elif a.isoweekday() == 7:
        a += datetime.timedelta(days=1)
        a = a.replace(hour=9,minute=0,second=0,microsecond=0)
        now = datetime.datetime.now()
        c = a - now
        wait_time = c.seconds
        print('Its Sunday... sleeping',wait_time,"seconds...")
        time.sleep(wait_time)
#check if its work hours
    now = datetime.datetime.today().time()
    work_hours = [9,10,11,12,13,14,15,16,17]
    if now.hour not in work_hours:
        a = datetime.datetime.now()
        a += datetime.timedelta(days=1)
        a = a.replace(hour=9,minute=0,second=0,microsecond=0)
        now = datetime.datetime.now()
        c = a - now
        wait_time = c.seconds
        print(datetime.datetime.now())
        print("Its not time to work... sleeping",wait_time,"seconds...")
        time.sleep(wait_time)
#check for changes in file modification timestamps
    else:
        print("Checking for Changes...")
        new_timestamps = []
        for i in os.listdir(path):
            z = os.stat(path+i).st_mtime
            y = time.gmtime(z)
            a = time.strftime("%m/%d/%Y %H:%M:%S",y)
            new_timestamps.append(a)
#if there is an update run the script, else sleep
            print(old_timestamps_a,"current")
            print(new_timestamps,"new")
        if old_timestamps_a != new_timestamps:
            print(datetime.datetime.now())
            print("****Update Found!**** Running Script...")
            os.system(x)
            old_timestamps_a = new_timestamps
        else:
            print(datetime.datetime.now())
            print("No Changes Found! Sleeping 15...")
    global n
    n+=1
    print("Run num:",n)
    print("\n")
    
#############################################################################################
def task_b(name,x,path):
    global old_timestamps_b
# check if its Saturday
    print(name)
    a = datetime.datetime.now()
    if a.isoweekday() == 6:
        a += datetime.timedelta(days=2)
        a = a.replace(hour=9,minute=0,second=0,microsecond=0)
        now = datetime.datetime.now()
        c = a - now
        wait_time = c.seconds
        print('Its Saturday... sleeping',wait_time,"seconds...")
        time.sleep(wait_time)
#check if its Sunday
    elif a.isoweekday() == 7:
        a += datetime.timedelta(days=1)
        a = a.replace(hour=9,minute=0,second=0,microsecond=0)
        now = datetime.datetime.now()
        c = a - now
        wait_time = c.seconds
        print('Its Sunday... sleeping',wait_time,"seconds...")
        time.sleep(wait_time)
#check if its work hours
    now = datetime.datetime.today().time()
    work_hours = [9,10,11,12,13,14,15,16,17]
    if now.hour not in work_hours:
        a = datetime.datetime.now()
        a += datetime.timedelta(days=1)
        a = a.replace(hour=9,minute=0,second=0,microsecond=0)
        now = datetime.datetime.now()
        c = a - now
        wait_time = c.seconds
        print(datetime.datetime.now())
        print("Its not time to work... sleeping",wait_time,"seconds...")
        time.sleep(wait_time)
#check for changes in file modification timestamps
    else:
        print("Checking for Changes...")
        new_timestamps = []
        for i in os.listdir(path):
            z = os.stat(path+i).st_mtime
            y = time.gmtime(z)
            a = time.strftime("%m/%d/%Y %H:%M:%S",y)
            new_timestamps.append(a)
#if there is an update run the script, else sleep
            print(old_timestamps_b,"current")
            print(new_timestamps,"new")
        if old_timestamps_b != new_timestamps:
            print(datetime.datetime.now())
            print("****Update Found!**** Running Script...")
            os.system(x)
            old_timestamps_b = new_timestamps
        else:
            print(datetime.datetime.now())
            print("No Changes Found! Sleeping 15...")
    global n
    n+=1
    print("Run num:",n)
    print("\n")
#############################################################################################
while True:
    task_a('clean snake','python my_script1.py',r'F:your\file\directory\to\check\for\changes\\')
    task_b('sales snake','python my_script2.py',r'F:your_other\file\directory\to\check\for\changes\\')
    time.sleep(60*15)
