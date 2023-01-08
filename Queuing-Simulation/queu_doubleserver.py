#!/home/mohamed/anaconda3/bin/python3
"""
Author : Mohamed Wael Alsayed
Email  : mohamed.wael@gmail.com
"""
import numpy as np
random_numbers1 = [94, 73, 70, 82,25, 35, 61, 42, 48, 26, 88, 31, 90, 55, 95, 58, 70, 15, 73, 65, 74, 75,98]
# random_numbers1 = input().split()
# # random_numbers1 = list(map(int, random_numbers1))

random_numbers2 = [32, 96, 89, 32, 67, 48, 63, 99, 98, 66, 85, 58, 6, 39, 15, 2, 48, 63, 85, 61, 40, 16, 18, 52]
# random_numbers2 = input().split()
# # random_numbers2 = list(map(int, random_numbers2))

# # print(random_numbers1)
# # print(random_numbers2)
# # print("#"*50)
print("Enter running time for system ")
running_time = int(input())

print("IAT probapilities")
# IAT_numbers = [1,2,3,4]
IAT_numbers = input().split()
IAT_numbers = map(int,IAT_numbers)
# IAT_prob = [0.25,0.4,0.2,0.15]
IAT_prob = input().split()
IAT_prob = map(float,IAT_prob)
# IAT_cumulative = np.cumsum(IAT_prob)*100

print("service time distributions for Able")
# Albe_list = [2, 3, 4, 5]
Albe_list = input().split()
Albe_list = map(int,Albe_list)
# Albe_prob = [0.30, 0.28, 0.25, 0.17]
Albe_prob = input().split()
Albe_prob = map(float,Albe_prob)
# Albe_cumulative = np.cumsum(Albe_prob)*100

print("service time distributions for Baker")
# Baker_list = [2, 3, 4, 5]
Baker_list = input().split()
Baker_list = map(int,Baker_list)
# Baker_prob = [0.35, 0.25, 0.20, 0.2]
Baker_prob = input().split()
Baker_prob = map(float,Baker_prob)
# Baker_cumulative = np.cumsum(Baker_prob)*100

# def create_probaility_table(nuubers, probapilities):
#     dict= {}
#     for i,j in zip(nuubers, probapilities):
#         dict[i] = j
#     return dict

# IAT_table = create_probaility_table(IAT_numbers, IAT_prob)
# Albe_table = create_probaility_table(Albe_list, Albe_prob)
# Baker_table = create_probaility_table(Baker_list, Baker_prob)

# print(IAT_table)
# print(Albe_table)
# print(Baker_table)

def select_number(numbers, probabilities,x):
    cum_sum = np.cumsum(probabilities)*100
    cum_sum = list(map(int, cum_sum))
    i=0
    while(i<len(numbers)):
        if ((i==0) and (x<cum_sum[i])):
            return numbers[i]
        elif ((x>=cum_sum[i-1]) and (x<cum_sum[i])):
            return numbers[i]
        elif ((i==len(numbers)-1) and (x>=cum_sum[i])):
            print("Enter valid random number")
            break
        i += 1

print("ID","RN_IAT","IAT", "Clock", "RN_ST", "Able_begin", "Able_ST", "Able_end", "Able idle", "Baker_Begin", "Baker_ST", "Baker_end", "Baker_idle", "Q_Time", "Time_spent")

i = 0
IAT = 0
clock = 0
able_begin = 0
able_ST = 0
able_end = 0
able_idle = 0
baker_begin = 0
baker_ST = 0
baker_end = 0
baker_idle = 0
Q_time = 0
Time_spent = 0
average_waiting = 0
able_idle_sum = 0

while((able_end<=running_time) and (baker_end<=running_time)):
    if(i >0):
        IAT = select_number(IAT_numbers, IAT_prob, random_numbers1[i-1])
        clock = clock + IAT
    if ((clock >= able_end) and (clock>=baker_end)):
        baker_ST = select_number(Baker_list, Baker_prob, random_numbers2[i])
        baker_begin = clock
        baker_idle = baker_begin - baker_end
        baker_end = baker_begin + baker_ST
        Q_time = 0
        time_spent = baker_ST
        print(i,random_numbers1[i], IAT, clock, random_numbers2[i], "*", "*", "*", "*", baker_begin, baker_ST, baker_end, baker_idle, Q_time, time_spent)
    elif((clock<baker_end) and (clock>=able_end)):
        able_ST = select_number(Albe_list, Albe_prob, random_numbers2[i])
        able_begin = clock
        able_idle = able_begin - able_end
        Q_time = 0
        able_end = able_begin + able_ST
        time_spent = able_ST
        print(i,random_numbers1[i], IAT, clock, random_numbers2[i], able_begin, able_ST, able_end, able_idle,"*", "*", "*", "*", Q_time, time_spent)
    elif ((clock>=baker_end) and (clock<able_end)):
        baker_ST = select_number(Baker_list, Baker_prob, random_numbers2[i])
        baker_begin = clock
        baker_idle = baker_begin - baker_end
        baker_end = baker_begin + baker_ST
        Q_time = 0
        time_spent = baker_ST
        print(i,random_numbers1[i], IAT, clock, random_numbers2[i], "*", "*", "*", "*", baker_begin, baker_ST, baker_end, baker_idle, Q_time, time_spent)
    elif((clock<baker_end) and (clock<able_end)):
        if(baker_end>able_end):
            able_ST = select_number(Albe_list, Albe_prob, random_numbers2[i])
            able_begin = able_end
            able_idle = 0
            Q_time = able_begin - clock
            time_spent = able_ST + Q_time
            able_end = able_begin + able_ST
            print(i, random_numbers1[i], IAT, clock, random_numbers2[i], able_begin, able_ST, able_end, able_idle,"*", "*", "*", "*", Q_time, time_spent)
        elif(baker_end<able_end):
            baker_ST = select_number(Baker_list, Baker_prob,random_numbers2[i])
            baker_begin = baker_end
            baker_idle = 0
            Q_time = baker_begin - clock
            time_spent = baker_ST + Q_time
            baker_end = baker_begin + baker_ST
            print(i, random_numbers1[i], IAT, clock, random_numbers2[i], "*", "*", "*", "*", baker_begin, baker_ST, baker_end, baker_idle, Q_time, time_spent)

    average_waiting = average_waiting + Q_time
    able_idle_sum = able_idle_sum + able_idle
    i =i+1

average_waiting = average_waiting / i+1
print(average_waiting)
able_idle_sum = 1-(able_idle_sum/max(able_end, baker_end))
print(able_idle_sum*100)