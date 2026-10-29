def participant_cost(attendees, food_per_person, transport_per_person):
    return attendees*(food_per_person + transport_per_person)



# Test Cases

total_participant_cost = participant_cost (5,500,100) # Normal Atteende Count Test - Expected:3000, Actual:3000
print (total_participant_cost)

total_participant_cost = participant_cost (0,500,100) #  Zero Attendee Test - Expected: 0, Actual : 0
print (total_participant_cost)



# Handover Note

'''
Component Owned : participant_cost : A function that calculates the total cost to be incured by all the particiupants who are  attending the event
What it returns : the total cost incured by the participants
Tests run : 
            1. Normal attendees count where the attendees count is non-zero, 
            2. Zero attendees count : where the attendees count is zero 
Assumptions/Unresolved Issues : None

'''
