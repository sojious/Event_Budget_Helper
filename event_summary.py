def event_summary (event_name, total, status) :
    print (f"{event_name}: total {total} naira. {status}.")

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

total_cost = event_total (5,500,100,50000) # The required Example ------ Expected : "Study Day: total 10500 naira. Within budget.", Actual : "Study Day: total 10500 naira. Within budget."
status = budget_status(20000,total_cost)   
event_summary ("Study Day", total_cost,status)

total_cost = event_total (10,800,200,500)
status = budget_status(9000,total_cost)   # Different Event Name and total ------ Expected : Expected : "Birthday: total 10500 naira. Over budget.", Actual : "Study Day: total 10500 naira. Within budget.", Actual : "Birthday: total 10500 naira. Over budget."
event_summary ("Birthday", total_cost,status)


#----- Handover Note -----------------
'''
Component Owned : event_summary : A function that print a summary of the event including name, total and status
Tests run : 
            1. The required example
            2. A different example
Assumptions/Unresolved Issues : None

'''

