def FCFS(arrival_time,burst_time):
    n=len(arrival_time)
    d={}
    for i in range(len(arrival_time)):
        d[i]=[arrival_time[i],burst_time[i]]
            
    d = dict(sorted(d.items(), key=lambda item: item[1][0]))
    CT=0
    TAT=0
    WT=0
    for i in d:
        CT += d[i][1]
        TAT += CT-d[i][0]
        WT = TAT-CT
        
    return (WT/n,TAT/n)


def SJS(arrival_time, burst_time):
    WT = [0] * len(arrival_time)
    TAT = [0] * len(arrival_time)
    n = len(arrival_time)
    completed = [False] * n
    total_time = 0
    remaining_bt = burst_time.copy()
    while True:
        min_bt = float('inf')
        shortest = -1
        for i in range(n):
            if not completed[i] and arrival_time[i] <= total_time and remaining_bt[i] < min_bt:
                min_bt = remaining_bt[i]
                shortest = i
        if shortest == -1:
            break
        completed[shortest] = True
        total_time += burst_time[shortest]
        WT[shortest] = total_time - arrival_time[shortest] - burst_time[shortest]
        TAT[shortest] = WT[shortest] + burst_time[shortest]
    return (sum(WT)/n, sum(TAT)/n)


def PS(arrival_time, burst_time, priority):
    n = len(arrival_time)
    WT = [0] * n
    TAT = [0] * n
    processes = [(i, arrival_time[i], burst_time[i], priority[i]) for i in range(n)]
    processes.sort(key=lambda x: x[3])
    total_time = 0
    for i in range(n):
        process_id, at, bt, _ = processes[i]
        if at > total_time:
            total_time = at
        WT[process_id] = total_time - at
        total_time += bt
        TAT[process_id] = WT[process_id] + bt
    return (sum(WT)/n, sum(TAT)/n)


def RR(arrival_time, burst_time, quantum):
    n = len(arrival_time)
    WT = [0] * n
    TAT = [0] * n
    remaining_bt = burst_time.copy()
    time = 0
    while any(remaining_bt):
        for i in range(n):
            if remaining_bt[i] > 0:
                if remaining_bt[i] <= quantum:
                    time += remaining_bt[i]
                    WT[i] = time - arrival_time[i] - burst_time[i]
                    remaining_bt[i] = 0
                else:
                    time += quantum
                    remaining_bt[i] -= quantum
                TAT[i] = WT[i] + burst_time[i]
    return (sum(WT)/n,sum(TAT)/n)


arrival_time = [0,4,5,6]
burst_time = [24,3,3,12]
priority = [3,1,4,2]

print(FCFS(arrival_time,burst_time))
print(SJS(arrival_time,burst_time))
print(PS(arrival_time,burst_time,priority))
print(RR(arrival_time,burst_time,4))