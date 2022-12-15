from random_address import real_random_address
import datetime
from datetime import timezone, timedelta
import random 
import os, sys
import json

if [] == 0: 
    print("yes")
else:
    print("no")

ticket_data = []
ticket_id = 704
note_id = 4025864
customer_id = 149018
admin_ids = [145423, 145424, 145425, 145426, 145427]
ticket_closed = True

end_date = datetime.datetime.now( timezone.utc ).replace( microsecond=0 )
ticket_timelog = end_date - timedelta( days=random.randint(4, 7) )
shipment_date = ticket_timelog - timedelta( days=random.randint(3, 10), hours=random.randint(5, 10) )
#      Example Data     #
issue_type = [ "Incident", "Faulty", "Damaged on Arrival", "Warranty"] 
group = [ "Refund", "Delivery Issue", "Replacement", "Reparation" ]
category = [ "phone", "laptop", "pc", "other" ]
progress = [ "Pending", "Waiting for Third Party", "Waiting for Customer" ]
products = {
    "phone" : [ "Mobile", "Landline" ],
    "laptop" : [ "Mac", "Acer", "Lenovo" ],
    "pc" : [ "Alienware", "Dell", "Custom" ],
    "furniture": ["Desk Chairs", "Desks"],
    "other" : [ "Accessories", "Office Utilities" ]
}
determined_category = random.choice(category)

def calculate_time( previous_ticket, ticket_id, ticket_closed ):
    # different types = response_time or shipment_time or initial_start_time
    # start_time = datetime.datetime.now( timezone.utc ).replace( microsecond=0 )
    if previous_ticket == [] or ticket_closed:
        ticket_closed = False
        start_time = datetime.datetime.now( timezone.utc ).replace( microsecond=0 )
    
        return start_time
    
    elif previous_ticket["activity"]["shipment_date"] in previous_ticket["activity"]:
        ticket_timelog = start_time + timedelta(hours=random.randint( 2, 6 ))
        
        return ticket_timelog
    
    else:
        
    
    # if ticket_closed:
    #     start_time = datetime.datetime.now( timezone.utc ).replace( microsecond=0 )
    #     return start_time
    # elif previous_ticket["ticket_id"] == ticket_id and :    
        

def response_time( ticket_started ):
    ticket_timelog = ticket_started + timedelta(hours=random.randint( 2, 6 ))
    return ticket_timelog

def determine_status( previous_ticket, performer_is_admin ):
    global ticket_closed
    if previous_ticket["activity"]["contacted_customer"] == False and performer_is_admin:
        return "Waiting for Customer" 
    elif performer_is_admin == False :
        if random.choice([True, False]) or previous_ticket["activity"]["status"] == "Pending":
            ticket_closed = True
            return random.choice(["Closed", "Resolved"])
        else:
            previous_ticket["activity"]["priority"] -= 1
            return "Pending" 
    else:
        return "Pending"
def new_note(): 
    note_id = note_id + 1
    
def assign_activity( previous_ticket, performer_id, performer_type, ticket_id, ticket_closed ):
    #   have if conditional where previous ticket is note than we make next ticket NOT note 
    if ticket_closed or len(ticket_data) == 1:
        # start new ticket thread
        return {
            "shipment_date": f'{calculate_time(previous_ticket, ticket_id, ticket_closed).strftime("%d-%m-%Y %H:%M:%S %z")}',
            "shipping_address": real_random_address(),
            "category" : determined_category,
            "contacted_customer" : random.choice([ True, False ]),
            "issue_type": random.choice(issue_type),
            "source" : random.randint( 1, 20 ),
            "status" : "Open",
            "priority" : random.randint( 2, 4),
            "group" : random.choice( group ),
            "agent_id" : performer_id,
            "requester" : random.randint(149900, 149998),
            "product" : random.choice(products[determined_category])
        }
    else:
        # continue existing thread
        return {
            "shipment_date": previous_ticket["activity"]["shipment_date"],
            "shipping_address": previous_ticket["activity"]["shipping_address"],
            "category": previous_ticket["activity"]["category"],
            "contacted_customer": True,
            "issue_type": previous_ticket["activity"]["issue_type"],
            "source": previous_ticket["activity"]["source"],
            "status": determine_status(previous_ticket, performer_type),
            "priority": random.randint(1, 5),
            "group": previous_ticket["activity"]["group"],
            "agent_id": previous_ticket["performer_id"],
            "requester": previous_ticket["activity"]["requester"],
            "product": previous_ticket["activity"]["product"]
        }

def generate_ticket( tickets_requested, previous_ticket, ticket_status ):
    global ticket_id, customer_id 
    if len(ticket_data) < tickets_requested :  
        for iteration in range( tickets_requested -1 ):
            
            if len(ticket_data) == 0 or ticket_closed:
                ticket_id = ticket_id + 1
                customer_id = customer_id + 1
                initial_performed_at = calculate_time(previous_ticket, ticket_id, ticket_status).strftime("%d-%m-%Y %H:%M:%S %z")
                ticket_data.append({
                    
                    "performed_at": initial_performed_at,
                    "ticket_id": ticket_id,
                    "performer_type": "user",
                    "performer_id": customer_id,
                    "activity": assign_activity( previous_ticket, customer_id, False, ticket_id, ticket_closed )

                })
                return generate_ticket( int(sys.argv[-1]), ticket_data[-1],  ticket_status)
            
            elif previous_ticket["performer_type"] == "user":
                admin_id = admin_ids[random.randint(0, 4)]
                ticket_data.append({
                    
                    "performed_at": calculate_time(previous_ticket, ticket_id, ticket_status).strftime("%d-%m-%Y %H:%M:%S %z"),
                    "ticket_id": ticket_id,
                    "performer_type": "admin",
                    "performer_id": admin_id,
                    "activity": assign_activity( previous_ticket, admin_id, True, ticket_id, ticket_closed )
                    
                })
    else:
        print("gen_ticket else")
        # generate_JSON_file( ticket_data )
                
    # generate_JSON_file( ticket_data )           
# def generate_JSON_file( generated_tickets ):
#     try:    
#         json_data = json.dumps( generated_tickets )
#         with open('json_ticket_data.json', 'w', encoding = 'utf-8') as outfile:
#             outfile.write( json_data ) 
#         print('Tickets have been created in the json_ticket_data.json file.')
#     finally:
#         outfile.close
        
generate_ticket( int(sys.argv[-1]) , ticket_data, ticket_closed )
print( json.dumps( ticket_data, indent=4 ))

# .strftime("%d-%m-%Y %H:%M:%S %z")