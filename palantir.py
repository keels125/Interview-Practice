def getMinTimeDifference(times):
    sorted_times = sorted(times)
    
    n = len(sorted_times)
    for i in range(n):
        time = sorted_times[i]
        
        hour = int(time[:2])
        minutes = int(time[3:])

        total = (hour*60) + minutes
        if (i==0 and total<60):
            total += (60*24)
        sorted_times[i] = total

    minTimeDif = abs(sorted_times[0] - sorted_times[1])
    for i in range(n):
        if i==(n-1):
            temp = abs(sorted_times[i] - sorted_times[0])
            if temp < minTimeDif:
                minTimeDif = temp
        elif abs(sorted_times[i] - sorted_times[i+1])<minTimeDif:
            minTimeDif = abs(sorted_times[i] - sorted_times[i+1])

    return minTimeDif






def getSuspiciousList(transactions):
    people = {}
    n = len(transactions)

    susp = []
    
    for i in range(n):
        tran = transactions[i].split('|')

        name = tran[0]
        money = tran[1]
        loc = tran[2]
        time = tran[3]

        if money>3000:
            if name not in susp:
                susp.append(name)

        elif name in people:
            prev = people[name]
            if loc!=prev[1] and prev[2]<=(60+time):
                susp.append(name)
        else:
            people[name] = [money, loc, time]

    return susp








def main():
    t = ["Shilpa|500|California|63", "Tom|25|New York|615",
         "Krasi|9000|California|1230", "Tom|25|New York|1235",
         "
    
    print(getSuspiciousList(

    
main()
