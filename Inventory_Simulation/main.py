import numpy as np
"""
Author: Mohamed Wael Alsayed 
Email: mohamed.wael.elsuid@gmail.com
code link: https://github.com/MohamedWaelAlsayed/Inventory_Simulation
"""

def select_lead(leads: list, probs: list, r: int):
    """This function take leads ,their probabilities and random number, then map it to lead time"""
    cum_sum = np.cumsum(probs) * 10
    cum_sum = list(map(round, cum_sum))
    i = 0
    while i < len(leads):
        if (i == 0) and (r <= cum_sum[i]) and (r != 0):
            return leads[i]
        elif (r > cum_sum[i - 1]) and (r <= cum_sum[i]):
            return leads[i]
        elif r == 0 and (i == len(leads) - 1):
            return leads[i]
        elif (i == len(leads) - 1) and (r >= cum_sum[i]):
            print("Enter Valid Number")
            break
        i += 1


def select_demand(demands: list, probabilities: list, r: int):
    cum_sum = np.cumsum(probabilities) * 100
    cum_sum = list(map(round, cum_sum))
    i = 0
    while i < len(demands):
        if (i == 0) and (r <= cum_sum[i]) and (r != 0):
            return demands[i]
        elif (r > cum_sum[i - 1]) and (r <= cum_sum[i]):
            return demands[i]
        elif r == 0 and (i == len(demands) - 1):
            return demands[i]
        elif (i == len(demands) - 1) and (r >= cum_sum[i]):
            print("Enter valid random number")
            break
        i += 1


leads = [1, 2, 3]
# lead = list(map(int, input("Enter lead numbers: ")))
lead_prob = [0.6, 0.3, 0.1]
# lead_prob = list(map(float, input("Enter lead probabilities: ")))
Random_Lead = [5, 0, 3, 4, 8]
# Random_Lead = list((int, input("enter random lead: ").split()))

demands = [0, 1, 2, 3, 4]
# demands = list(map(int, input("enter demands: ")))
demand_probs = [0.10, 0.25, 0.35, 0.21, 0.09]
# demand_probs = list(map(float, input("enter demand probabilities: ")))
Random_Demand = [24, 35, 65, 81, 54, 3, 87, 27, 73, 70, 47, 45, 48, 17, 9, 42, 87, 26, 36, 40, 7, 63, 19, 88, 94]
# Random_Demand = list(map(int, input("enter random demand: ").split()))
# Standard Inventory level
# M = int(input("Enter standard Inventory level: "))
M = 11
# Periodic review length
# N = int(input("Enter periodic review length: "))
N = 5
# No_of_cycles = int(input("Enter no of cycles: "))
No_of_cycles = 5
# start_quantity = int(input("Enter start quantity: "))
start_quantity = 3
inventory_begin = start_quantity
inventory_end = 0
# Shortage
short = 0
lead = 0
order = 0
# Number of cycles
# c = int(input("enter number of cycles: "))
c = 1
# added_Quantity = int(input("enter added_Quantity: "))
added_Quantity = 8
# day_addedQuantity = int(input("enter when to add quantity: "))
day_addedQuantity = 2
average_end = 0
number_of_shortages = 0


for day in range(1, No_of_cycles * N + 1):
    demand = select_demand(demands, demand_probs, Random_Demand[day - 1])
    if inventory_begin - demand >= 0:
        inventory_end = inventory_begin - demand
        short = 0
    else:
        inventory_end = 0
        short += abs(inventory_begin - demand)

    average_end += inventory_end
    if short > 0:
        number_of_shortages += 1
    print("Cycle: ", c, ' Days: ', day, " Inventory Begin: ", inventory_begin, " RN D.: ", Random_Demand[day - 1],
          " Demand: ", demand, " Inventory End: ", inventory_end, "Short", short, end="")
    if day % N == 0:
        lead = select_lead(leads, lead_prob, Random_Lead[c - 1])
        order = M - inventory_end + short
        print(" Order: ", order, " Random Lead: ", Random_Lead[c - 1], " Lead: ", lead)
        c += 1
        inventory_begin = inventory_end
    elif day < day_addedQuantity + 1:
        lead = day_addedQuantity - day
        if lead == 0:
            inventory_begin = inventory_end + added_Quantity
        else:
            inventory_begin = inventory_end
        print(" Order: ", "*", " Random Lead: ", "*", " Lead: ", lead)

    elif lead > 0:
        lead -= 1
        if lead == 0:
            inventory_begin = inventory_end + order - short
            short = 0
        else:
            inventory_begin = inventory_end
        print(" Order: ", "*", " Random Lead: ", "*", " Lead: ", lead)

    elif lead == 0:
        inventory_begin = inventory_end
        print(" Order: ", "*", " Random Lead: ", "*", " Lead: ", "*")

print("Average End of Inventory: ", average_end/(N*No_of_cycles), " Units")
print(f"The number of shortage times = {number_of_shortages} times out of {N*No_of_cycles} days.")
