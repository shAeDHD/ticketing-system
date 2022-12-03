from random_address import real_random_address
import datetime
from datetime import timedelta
import random 
import json

tickets = []
requested_number = input()

def generate_tickets( number_of_tickets ): 

    iteration = 1
    
    while iteration <= number_of_tickets:
        
        ticket_ids = [704]
        note_ids = [4025864]
        start_date  = datetime.datetime.now()
        end_date    = start_date + timedelta(days=random.randint(1,3))
        
        performer_id_value = random.randint(149900,150000)
        
        def generate_date( start_date, end_date ): 
            performed_at = start_date + timedelta(days=random.uniform(0.25 , (end_date - start_date).days +1))
            return performed_at
        activity_commencement_date = generate_date( start_date, end_date )
        
        def generate_performer_type( number_of_tickets ):
            if len(number_of_tickets) % 50 == 1:
                performer_type_value = "Admin"
                return performer_type_value
            else:
                performer_type_value = "User"
                return performer_type_value
            
        def generate_random_activity( ):    
    
            # Example activities/ticket topic
            activities = [ "Delivery Issue", "Refund Request", "Other / Message" ]
            activity_type = random.choice(activities)
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
            # Example Categories and iteration selection        
            category = [ "phone", "laptop", "pc", "other" ] 
            category_value = random.choice(category)
            # Example Product Lines and iteration selection
            products = {
                "phone" : [ "Mobile", "Landline" ],
                "laptop" : [ "Mac", "Acer", "Lenovo" ],
                "pc" : [ "Alienware", "Dell", "Custom" ],
                "other" : [ "Accessories", "Office Utilities" ]
            }
            
            # Generation of iterations activity type
            if activity_type == "Other / Message":
                return {
                    "note" : {
                        "id" : note_ids[-1] + 1,
                        "type" : random.choice( group )
                    }
                }
            else:
                return {
                    "shipping_address": real_random_address(),
                    "shipment_date": f'{activity_commencement_date - timedelta(days=random.randint( 3, 10 ))}',
                    "category" : category_value,
                    "contacted_customer" : random.choice([True, False]),
                    "issue_type": random.choice(issue_type),
                    "source" : random.randint( 1, 20 ),
                    "status" : random.choice(status_options),
                    "priority" : random.randint( 1, 5),
                    "group" : random.choice(group),
                    "agent_id" : performer_id_value,
                    "requester" : random.randint(149900,149998),
                    "product" : random.choice(products[category_value])
                }
                         
        activities_data = {
            "performed_at": f'{activity_commencement_date}',
            "ticket_id": ticket_ids[-1] + 1,
            "performer_type" : generate_performer_type(ticket_ids),
            "performer_id" : performer_id_value,
            "activity" : generate_random_activity( )
        }
        
        tickets.append(activities_data)
        iteration = iteration + 1
        
generate_tickets( int(requested_number) )
print(json.dumps(tickets, sort_keys=False, indent=4) ) 