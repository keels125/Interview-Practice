import datetime

def normalise(input_time):
    str_time = datetime.datetime.fromtimestamp(input_time)

    #used to figure out how many days we need to go back
    d = {"Sun":0, "Mon":1, "Tue":2, "Wed":3, "Thur":4, "Fri":5, "Sat":6}

    #each if statement calculates how much we need to change the input_time
    #for days, hours, mins, and secs
    if str_time.ctime()[:3]!="Sun":
        day_diff = d[str_time.ctime()[:3]]

    if str_time.ctime()[11:13]!="00":
        hour_diff = int((str_time.ctime()[11:13]))

    if str_time.ctime()[14:16]!="00":
        min_diff = int((str_time.ctime()[14:16]))

    if str_time.ctime()[17:19]!="00":
        sec_diff = int((str_time.ctime()[17:19]))

    str_time = str_time - datetime.timedelta(days = day_diff,
                                             hours = hour_diff,
                                             minutes = min_diff,
                                             seconds = sec_diff)
    return str_time
    
print(normalise(1479146637))
