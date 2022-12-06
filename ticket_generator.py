from random_address import real_random_address
import datetime
from datetime import timezone, timedelta
import random 
import json
# import argparse       # TODO - utilise ArgParse for bashrun program

#       GLOBAL VARIABLES        #
activites_data  = [ ]
ticket_id       = 704
note_id         = 4025864
performer_id    = 149018   
ticket_closed   = False
end_date      = datetime.datetime.now( timezone.utc ).replace(microsecond=0)
start_date    = end_date - timedelta( days=random.randint(4, 7) )
response_time = start_date - timedelta(hours=random.randint(5, 12))
shipment_date = start_date - timedelta( days=random.randint(3, 10), hours=random.randint(5, 10) )
acc_opened    = shipment_date - timedelta( days=random.randint(1, 3), hours=random.randint(5, 10) )

#      Example Data     #
issue_type          = [ "Incident", "Faulty", "Damaged on Arrival", "Warranty"] 
group               = [ "Refund", "Delivery Issue", "Replacement", "Reparation" ]
category            = [ "phone", "laptop", "pc", "other" ]
progress            = [ "Pending", "Waiting for Third Party", "Waiting for Customer" ]
products            = {
    "phone" : [ "Mobile", "Landline" ],
    "laptop" : [ "Mac", "Acer", "Lenovo" ],
    "pc" : [ "Alienware", "Dell", "Custom" ],
    "furniture": ["Desk Chairs", "Desks"],
    "other" : [ "Accessories", "Office Utilities" ]
}
determined_category = random.choice(category)


#       FUNCTIONS       #
#   Randomised Logic to determine activity status utilising previous generated ticket 
def determine_status():    
    if activites_data[-1]["activity"]["contacted_customer"]:
        if random.choice([True, False]):
            global performer_id 
            performer_id += 1 
            global ticket_closed 
            ticket_closed = True
            new_shipment_date()          
            return random.choice(["Resolved", "Closed"])
        else:
            return random.choice(progress)
    else:
        return "Open"            
#   Updates Global variables and return time in correct format    
def determine_response_time():
    global response_time
    response_time = response_time + timedelta(hours=random.randint(2, 6))
    return response_time.strftime("%d-%m-%Y %H:%M:%S %z")     
def new_ticket_start_date():
    global start_date 
    global ticket_closed
    ticket_closed = False
    start_date = end_date - timedelta(days=random.randint(1, 3), hours=random.randint(5, 10))
    return start_date.strftime("%d-%m-%Y %H:%M:%S %z")
def new_shipment_date():
    global shipment_date
    shipment_date = start_date - timedelta( days=random.randint(3, 10), hours=random.randint(5, 10) )
    return shipment_date.strftime("%d-%m-%Y %H:%M:%S %z")
#   Randomised data for activty  
def generate_activities():   
    if "note" in activites_data[-1]["activity"]: 
        return {
            "shipping_address": real_random_address(),
            "shipment_date": f'{shipment_date.strftime( "%d-%m-%Y %H:%M:%S %z")}',
            "category" : determined_category,
            "contacted_customer" : random.choice([ True, False ]),
            "issue_type": random.choice(issue_type),
            "source" : random.randint( 1, 20 ),
            "status" : "Open",
            "priority" : random.randint( 1, 5),
            "group" : random.choice( group ),
            "agent_id" : activites_data[-1]["performer_id"],
            "requester" : random.randint(149900,149998),
            "product" : random.choice(products[determined_category])
        }  
    else:
        return {
            "shipping_address": activites_data[-1]["activity"]["shipping_address"],
            "shipment_date": activites_data[-1]["activity"]["shipment_date"],
            "category": activites_data[-1]["activity"]["category"],
            "contacted_customer": True,
            "issue_type": activites_data[-1]["activity"]["issue_type"],
            "source": activites_data[-1]["activity"]["source"],
            "status": determine_status(),
            "priority": random.randint(1, 5),
            "group": activites_data[-1]["activity"]["group"],
            "agent_id": activites_data[-1]["performer_id"],
            "requester": activites_data[-1]["activity"]["requester"],
            "product": activites_data[-1]["activity"]["product"]
        }
#   Ticket Constructor    
def generate_tickets( number_of_tickets ): 
    for iteration in range(number_of_tickets):
        global ticket_id 
        ticket_id += 1
        global note_id
        note_id += 1
        if len(activites_data) == 0 or ticket_closed:  
            ticket_data = {
                "performed_at": f'{new_ticket_start_date()}',
                "ticket_id": ticket_id,
                "performer_type" : "user",
                "performer_id" : performer_id,
                "activity" : {
                    "note" : {
                        "id" : note_id,
                        "type" : random.randint(1, 4),
                    },
                }
            }        
            activites_data.append(ticket_data)
        else:
            ticket_data = {
                "performed_at": determine_response_time(),
                "ticket_id": ticket_id,
                "performer_type" : "user",
                "performer_id" : performer_id,
                "activity" : generate_activities( )

            }
            activites_data.append(ticket_data)

generate_tickets( int(input('Please input desired number of tickets: ')) )
print(json.dumps( activites_data, indent=4 ))