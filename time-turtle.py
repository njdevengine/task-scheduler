import time
import datetime
import os
from flask import Flask

app = Flask(__name__)
@app.route("/")

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

def task(letter,name,command,path):
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
        new_timestamps = " ".join(new_timestamps)
#if there is an update run the script, else sleep
#get the last known timestamp from the notepad file
        file = "test_"+str(letter)+".txt"
        with open(file, "rb") as f:
            first = f.readline()        # Read the first line.
            f.seek(-2, os.SEEK_END)     # Jump to the second last byte.
            while f.read(1) != b"\n":   # Until EOL is found...
                f.seek(-2, os.SEEK_CUR) # ...jump back the read byte plus one more.
            last = f.readline()         # Read last line.
            old_timestamps = last.decode()
        print(old_timestamps,"current")
        print(new_timestamps,"new")
#check for differences
        if old_timestamps != new_timestamps:
#             print(datetime.datetime.now())
#             print("****Update Found!**** Running Script...")
            os.system(command)
            old_timestamps = new_timestamps
            with open("test_"+str(letter)+".txt", "a") as f:
                f.write("\n")
                f.write(str(name),"****Update Found!**** Running Script...",str(datetime.datetime.now()))
                f.write("\n")
                f.write(" ".join(new_timestamps))
        else:
            print(datetime.datetime.now())
            print("No Changes Found! Sleeping 15...")
#############################################################################################
while True:
    task('a','clean snake','python my_script1.py',r'F:\your\file\directory\to\check\for\changes\\')
    task('b','sales snake','python my_script2.py',r'F:\your_other\file\directory\to\check\for\changes\\')
    time.sleep(60*15)
