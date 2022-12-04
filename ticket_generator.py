from random_address import real_random_address
import datetime
from datetime import timezone, timedelta
import random 
import json
import argparse

tickets     = []
end_date    = datetime.datetime.now( timezone.utc ).replace(microsecond=0)
start_date  = end_date - timedelta( days=random.randint( 1,3 ) )
shipment_date_value = end_date - timedelta( days=random.randint(3, 10), hours=random.randint(5, 10) )
ticket_ids = [704]
note_ids = [4025864]
performer_id_value = random.randint(149900,150000)   

def generate_performer_type( number_of_tickets ):
    if len(number_of_tickets) % 50 == 1:
        performer_type_value = "Admin"
        return performer_type_value
    else:
        performer_type_value = "User"
        return performer_type_value

def generate_tickets( number_of_tickets ): 

    for iteration in range(number_of_tickets):

        def generate_activity():    
            # Examples for random data generation
            activities = [ "Delivery Issue", "Refund Request", "Other / Message" ]
            issue_type = [ "Incident", "Faulty", "Damaged on Arrival", "Warranty"] 
            group = [ "Refund", "Replacement", "Reparation" ]
            status_options = [ 
                "Open",
                "Close",
                "Resolved",
                "Waiting for Customer",
                "Waiting for Third Party",
                "Pending"  
            ]    
            category = [ "phone", "laptop", "pc", "other" ] 
            category_value = random.choice(category)
            products = {
                "phone" : [ "Mobile", "Landline" ],
                "laptop" : [ "Mac", "Acer", "Lenovo" ],
                "pc" : [ "Alienware", "Dell", "Custom" ],
                "other" : [ "Accessories", "Office Utilities" ]
            }
            
            # Generation of iterations activity
            if random.choice(activities) == "Other / Message":
                return {
                    "note" : {
                        "id" : note_ids[-1] + 1,
                        "type" : random.choice( group )
                    }
                }
            else:
                return {
                    "shipping_address": real_random_address(),
                    "shipment_date": f'{shipment_date_value.strftime( "%d-%m-%Y %H:%M:%S %z")}',
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
            "performed_at": f'{end_date.strftime( "%d-%m-%Y %H:%M:%S %z")}',
            "ticket_id": ticket_ids[-1] + 1,
            "performer_type" : generate_performer_type(ticket_ids),
            "performer_id" : performer_id_value,
            "activity" : generate_activity( )
        }
        
        tickets.append(activities_data)
        iteration = iteration + 1
        
# generate_tickets( int(input()) )
# print(json.dumps(generate_tickets( int(input()) ), sort_keys=False, indent=4) ) 

parser = argparse.ArgumentParser('Ticket Generator')
parser.add_argument('constructor', metavar='N', help='A given integer will generate that many Tickets', type=int )
# parser.add_argument('--')
args = parser.parse_args()
print(generate_tickets( args.constructor ) )
# print( args.constructor + json.dumps(generate_tickets( args._get_args ), sort_keys=False, indent=4) )