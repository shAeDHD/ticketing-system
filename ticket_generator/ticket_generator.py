from random_address import real_random_address
import datetime
from datetime import timezone, timedelta
import random 
import os, sys
import json

generated_tickets = []

ticket_data = {
    "ticket_number": 704,
    "note_id": 4025864,
    "customer_id": 149018,
    "admin_ids": [145423, 145424, 145425, 145426, 145427],
    "ticket_closed": True,
    "issue_type": ["Incident", "Faulty", "Damaged on Arrival", "Warranty"],
    "group": ["Refund", "Delivery Issue", "Replacement", "Reparation"],
    "category": [ "phone", "laptop", "pc", "other" ],
    "products": {
        "phone" : [ "Mobile", "Landline" ],
        "laptop" : [ "Mac", "Acer", "Lenovo" ],
        "pc" : [ "Alienware", "Dell", "Custom" ],
        "furniture": ["Desk Chairs", "Desks"],
        "other" : [ "Accessories", "Office Utilities" ]
    },
    "end_date": datetime.datetime.now( timezone.utc ).replace(microsecond=0),
    "ticket_timelog": datetime.datetime.now( timezone.utc ).replace(microsecond=0),
}

def determine_status( i, info ):
    info["ticket_closed"] = True
    if i == 0:
        return "Open"
    elif i == 1: 
        return "Waiting on Customer"
    elif i == 2 or i == 3:
        return "Pending"
    else:
        info["ticket_closed"] = True
        return random.choice(["Resolved", "Closed"])

def generate_activity( info, existing_tickets, iteration ):
    determined_category = random.choice(info["category"])
    if iteration >= 2:
        last_ticket = existing_tickets[-1]
        activity_data = {
            "shipping_address": last_ticket["activity"]["shipping_address"],
            "shipment_date": last_ticket["activity"]["shipment_date"],
            "category": last_ticket["activity"]["category"],
            "contacted_customer": True,
            "issue_type": last_ticket["activity"]["issue_type"],
            "source": last_ticket["activity"]["source"],
            "status": determine_status( iteration, ticket_data ),
            "priority": last_ticket["activity"]["priority"] - 1,
            "group": last_ticket["activity"]["group"],
            "agent_id": last_ticket["activity"]["agent_id"],
            "requester": last_ticket["activity"]["requester"],
            "product": last_ticket["activity"]["product"]
        }
        return activity_data
    else:
        activity_data = {
            "shipping_address": real_random_address(),
            "shipment_date": (info["ticket_timelog"] - timedelta(hours=28)).strftime("%d-%m-%Y %H:%M:%S %z"),
            "category": determined_category,
            "contacted_customer": False,
            "issue_type": random.choice(info["issue_type"]),
            "source": random.choice([ 1, 2, 3, 4 ]),
            "status": determine_status( iteration, ticket_data ),
            "priority": 4,
            "group": random.choice(info["group"]),
            "agent_id": info["customer_id"],
            "requester": random.choice(info["admin_ids"]),
            "product": random.choice(info["products"][determined_category])
        }    
        return activity_data

def create_tickets( tickets_requested, tickets_made, info ):
    
    batches_required = tickets_requested / 5 if tickets_requested % 5 == 0 else tickets_requested / 5 + 1 
    
    for iteration in range( int(batches_required) ):

        for iteration in range( 5 ):
            
            if iteration == 0:                
                info["ticket_timelog"] = info["end_date"] - timedelta(days=random.randint(1, 3), hours=random.randint(5, 10))                
                info["ticket_number"] = info["ticket_number"] + 1
                info["customer_id"] = info["customer_id"] + 1
                info["note_id"] = info["note_id"] + 1
                
                ticket = {                     
                    "performed_at": info["ticket_timelog"].strftime("%d-%m-%Y %H:%M:%S %z"),
                    "ticket_id": info["ticket_number"],
                    "performer_type": "user",
                    "performer_id": info["customer_id"],
                    "activity": 
                    {
                        "note": 
                        {
                            "id": info["note_id"],
                            "type": random.choice([ 1, 2, 3, 4 ])
                        }
                    }                                
                }
                tickets_made.append(ticket)
            elif iteration == 1:
                info["ticket_timelog"] = info["ticket_timelog"] + timedelta(hours=random.randint(2, 6))
                
                ticket = {                    
                    "performed_at": info["ticket_timelog"].strftime("%d-%m-%Y %H:%M:%S %z"),
                    "ticket_id": info["ticket_number"],
                    "performer_type": "user",
                    "performer_id": info["customer_id"],
                    "activity": generate_activity( ticket_data, tickets_made, iteration )        
                }
                tickets_made.append(ticket)
            else:                
                info["ticket_timelog"] = info["ticket_timelog"] + timedelta(hours=random.randint(2, 6))
                
                ticket = {                    
                    "performed_at": info["ticket_timelog"].strftime("%d-%m-%Y %H:%M:%S %z"),
                    "ticket_id": info["ticket_number"],
                    "performer_type": "user",
                    "performer_id": info["customer_id"],
                    "activity": generate_activity( ticket_data, tickets_made, iteration )        
                }
                tickets_made.append(ticket)
    generate_JSON_file( generated_tickets, tickets_requested )       

def generate_JSON_file( generated_tickets, ticket_quantity ):
    try:
        json_data = (json.dumps(generated_tickets[0:ticket_quantity], indent=4))
        with open("ticket_data.json", "w", encoding = "utf-8") as outfile:
            outfile.write( json_data )
    finally:
        outfile.close

create_tickets( int(sys.argv[-1]), generated_tickets, ticket_data )