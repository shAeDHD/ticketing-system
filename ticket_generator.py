import random_address 
from random_address import real_random_address
import datetime
from datetime import timedelta
import random 
import json

tickets = [ ]
requested_number = input("How many tickets? ")

def generate_tickets( number_of_tickets ): 
    
    ticket_ids = [704]
    note_ids = [4025864]
    
    def generate_ticket_id():
        new_ticket_id = ticket_ids[-1] + 1
        ticket_ids.append(new_ticket_id)
        return new_ticket_id
    ticket_id_value = generate_ticket_id()
    
    def generate_performer_id():
        performer_id = random.randint(149900,150000)
        return performer_id
    performer_id_value = generate_performer_id()
    
    def generate_requester_data():
        requester = random.randint(149900,149998)
        return requester
    requester_value = generate_requester_data()

    start_date  = datetime.datetime.now()
    end_date    = start_date + timedelta(days=random.randint(1,3))
    
    def generate_date( start_date, end_date ): 
        performed_at = start_date + timedelta(days=random.uniform(0.25 , (end_date - start_date).days +1))
        return performed_at
    activity_commencement_date = generate_date( start_date, end_date )

    def generate_shipment_date( iteration_generated_date ):
        date_before_complaint = iteration_generated_date - timedelta(days=random.randint( 3, 10 ))
        return date_before_complaint
    shipment_date_value = generate_shipment_date( activity_commencement_date )

    def generate_note_id():
        new_note_id = note_ids[-1] + 1
        note_ids.append(new_note_id)
        return new_note_id
    note_id_value = generate_note_id()
    
    def generate_boolean():
        boolean_value = False
        if random.randint(0, 1) == 0: boolean_value = True
        return boolean_value         
    contacted_customer_value = generate_boolean()
    
    def generate_random_activity( shipment_date_value ):    
    # Example activities/ticket topics
        activities = [ "Delivery Issue", "Refund Request", "Other / Message" ]
        activity_type = activities[random.randint( 0, 2 )] #NOTE for testing, change index value
        # Example issue types and groupings
        issue_type = [ "Incident", "Faulty", "Damaged on Arrival", "Warranty"] 
        group = [ "Refund", "Replacement", "Reparation" ]
        # Status values given from docs and random selection
        status_options = [ 
            "Open",
            "Close",
            "Resolved",
            "Waiting for Customer",
            "Waiting for Third Party",
            "Pending"  
        ]
        status_value = status_options[ random.randint( 0, (len(status_options)-1) ) ]
        # Example Categories and iteration selection        
        category = [ "phone", "laptop", "pc", "other" ] 
        category_value = category[random.randint( 0, len(category) -1 )]
        # Example Product Lines and iteration selection
        products = {
            "phone" : [ "Mobile", "Landline" ],
            "laptop" : [ "Mac", "Acer", "Lenovo" ],
            "pc" : [ "Alienware", "Dell", "Custom" ],
            "other" : [ "Accessories", "Office Utilities" ]
        }
        product_value = products[category_value][random.randint( 0,( len( products[category_value] ) -1 ) )]
        
        # Generation of iterations activity type
        if activity_type == "Other / Message":
            return {
                "note" : {
                    "id" : note_id_value,
                    "type" : group[random.randint( 0, len(group) -1 )]
                }
            }
        else:
            return {
                "shipping_address": real_random_address(),
                "shipment_date": f'{shipment_date_value}',
                "category" : category_value,
                "contacted_customer" : contacted_customer_value,
                "issue_type": issue_type[random.randint( 0, 3 )],
                "source" : random.randint( 1, 20 ),
                "status" : status_value,
                "priority" : random.randint( 1, 5),
                "group" : group[random.randint( 0, len(group) -1 )],
                "agent_id" : performer_id_value,
                "requester" : requester_value,
                "product" : product_value
            }
                
    activity_value = generate_random_activity( activity_commencement_date )
    
    iteration = 1
    while iteration <= number_of_tickets:
        
        if iteration % 50 == 0: 
            activities_data = {
                "performed_at": f'{activity_commencement_date}',
                "ticket_id": f'{ticket_id_value}',
                "performer_type" : 'Admin',
                "performer_id" : 149899,
                "activity" : f'{activity_value}'
            }
            iteration = iteration + 1
            tickets.append(activities_data)
        
        else:
            activities_data = {
                "performed_at": f'{activity_commencement_date}',
                "ticket_id": f'{ticket_id_value}',
                "performer_type" : 'User',
                "performer_id" : performer_id_value,
                "activity" : activity_value
            }
            iteration = iteration + 1
            
            tickets.append(activities_data)

# tickets_requested = input()
# NOTE -> To change the amount of tickets generated, change
#        the integer argument of generate_tickets() on line 137.
tickets.insert( 0, generate_tickets( int(requested_number) ) ) 

print(json.dumps(tickets, sort_keys=True, indent=4) )     #   check == true