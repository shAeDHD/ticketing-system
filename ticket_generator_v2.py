from random_address import real_random_address
import datetime
from datetime import timezone, timedelta
import random 
import json
# import argparse       # TODO - utilise ArgParse for bashrun program

#       Random date & time generation
end_date    = datetime.datetime.now( timezone.utc ).replace(microsecond=0)
start_date  = end_date - timedelta( days=random.randint( 1,3 ) )
shipment_date_value = start_date - timedelta( days=random.randint(3, 10), hours=random.randint(5, 10) )
acc_opened = shipment_date_value - timedelta( days=random.randint(1, 3), hours=random.randint(5, 10) )

ticket_id = 704
note_id = 4025864
performer_id = 149018

issue_type = [ "Incident", "Faulty", "Damaged on Arrival", "Warranty"] 
group = [ "Refund", "Delivery Issue", "Replacement", "Reparation" ]
category = [ "phone", "laptop", "pc", "furniture", "other" ] 
products = {
    "phone" : [ "Mobile", "Landline" ],
    "laptop" : [ "Mac", "Acer", "Lenovo" ],
    "pc" : [ "Alienware", "Dell", "Custom" ],
    "furniture": ["Desk Chairs", "Desks"],
    "other" : [ "Accessories", "Office Utilities" ]
}


def generate_tickets( requested_amount ):


    
    for iteration in range(requested_amount):
        determined_category = random.choice(category)
        determined_product  = random.choice(products[determined_category])
        determined_issue    = random.choice(issue_type)
        determined_group    = random.choice(group)
        activites_value     = random.choice([2, 3, 4])
        
        ticket_id          = ticket_id + 1
        note_id            = note_id + 1
        performer_id       = performer_id + 1
        
        metadata = {
            "start_at"          : acc_opened,
            "end_at"            : end_date,
            "activites_value"   : activites_value
        }

        activites_data = [
            {
                "performed_at"      : f'{start_date.strftime( "%d-%m-%Y %H:%M:%S %z")}',
                "ticket_id"         : ticket_id,
                "performer_type"    : "user",
                "performer_id"      : performer_id,
                "activity"          : {
                    "note"  : {
                        "id"    : note_id,
                        "type"  : random.randint(1,5)
                    }
                }
            },
            {
                "shipping_address"      : "n/a",
                "shipment_date"         : shipment_date_value,
                "category"              : determined_category,
                "contacted_customer"    : True,
                "issue_type"            :
            }
        ]