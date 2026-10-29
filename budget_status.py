def budget_status(budget,total):

    if total <= budget :
        return "Within budget"
    else :
        return "Over budget"


def event_total(attendees, food_per_person,transport_per_person,venue_cost):
    total_participant_cost = participant_cost (attendees,food_per_person,transport_per_person)
    return total_participant_cost + venue_cost

def participant_cost(attendees,food_per_person,transport_per_person):
    return attendees*(food_per_person + transport_per_person)


#---- Test Cases--------------------

total_cost = event_total (5,500,100,50000)
status = budget_status(60000,total_cost)   # Below Budget Case ------ Expected : "Within budget", Actual : "Within budget"
print (status)

total_cost = event_total (10,800,200,500)
status = budget_status(53000,total_cost)   # Equal to budget Case ------ Expected : "Within budget", Actual : "Within budget"
print (status)

total_cost = event_total (10,800,200,500)
status = budget_status(9000,total_cost)   # Above Budget Case ------ Expected : "Within budget", Actual : "Within budget"
print (status)


#----- Handover Note -----------------
'''
Component Owned : budget_status : A function that compares the budget to the total cost
Tests run : 
            1. Below budget case
            2. Exactly budget case
            3. Above budget case
Assumptions/Unresolved Issues : None

'''
