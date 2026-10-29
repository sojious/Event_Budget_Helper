def event_total(attendees, food_per_person, transport_per_person, venue_cost):
    total = participant_cost(attendees, food_per_person, transport_per_person)
    return total + venue_cost

def participant_cost(attendees, food_per_person, transport_per_person):
    return attendees*(food_per_person + transport_per_person)
 

# Test Cases

total_cost = event_total(5,500,100,50000) # Normal atteendees cost - Expected : 53000, Actual : 53000
print(total_cost)

total_cost = event_total(0,500,100,50000) # Zero atteendees cost - Expected : 50,000, Actual : 50000
print(total_cost)


# Handover Note
'''
Component Owned : event_total : A function that calculates the total cost of the event using the participant cost and venue cost
What it returns : the total cost of the event
Tests run : 
            1. Normal attendees cost plus venue where the attendees cost, venue cost and other parameters are non-zero, 
            2. Zero attendees cost plus non-zero venue : where the attendees cost is zero and the venue cost and other parameters are non - zero
Assumptions/Unresolved Issues : None
'''