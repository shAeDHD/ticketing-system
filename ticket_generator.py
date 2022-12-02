import random_address 
from random_address import real_random_address
import datetime
from datetime import timedelta
import random 

######################## TEST ##############################
start_date  = datetime.datetime.now()
end_date    = start_date + timedelta(days=random.randint(1,3))

# print(start_date)
# print(end_date)
 
def performed_at( start_date, end_date ): 
    
    # time_between_dates = end_date - start_date
    # days_between_dates = time_between_dates.days
    # random_number_of_days = random.uniform(0.25, days_between_dates)
    # performed_at_basic = datetime.timedelta(days=random_number_of_days)
    
    performed_at = datetime.timedelta(days=random.uniform(0.25 , (end_date - start_date).days +1))
        
    # print(performed_at)     #   test == true
performed_at(start_date, end_date)

############################################################
   
# DECONSTRUCTING DATA EXAMPLE

#   metadata:
#       "start_at"          = datetime.datetime.now()   # when ticket begins being created by user
#       "end_at"            = datetime.datetime.now()   # when ticket is formally completed by user
#       "activites_count"   = len(activities_data)      # total amount of activites taken 
#                                                       by user in the creation of their ticket

user_ids = []
ticket_ids = [704]
note_ids = [4025864]

def generate_user_id():
    new_user_id = random.randomint(149000,150000)
    if new_user_id not in user_ids:
        user_ids.append(new_user_id)
        return new_user_id
    else:
        generate_user_id()
        
def generate_ticket_id():
    new_ticket_id = ticket_ids[-1] + 1
    ticket_ids.append(new_ticket_id)
    return new_ticket_id

def generate_note_id():
    new_note_id = note_ids[-1] + 1
    note_ids.append(new_note_id)
    return new_note_id
    

#   activities_data: [
#       {
#           "performed_at"      = performed_at(start_date, end_date)
#           "ticket_id"         = generate_ticket_id()
#           "performer_type"    = "user"        # maybe user/admin?
#           "performer_id"      = generate_user_id())  
#           "activity"          = {
#               "note"          = {
#                   "id"        = generate_note_id()
#                   "type"      = random.randomint( 1, 4 )
#               }
#           }         




#           "activity"          = {    
#               "shipping_address"      = N/A or real_random_address()
#               "shipment_date"         = 
#               "category"              = phone, laptop, desktop, 
#               "contacted_customer"    = boolean
#               "issue_type"            = incident, delivery_failure, 
#               "source"                = random.randomInt()
#               "status"                = open, close, pending, Resolved, Waiting for Customer, Waiting for Third Party
#               "priority"              = randomInt(1 , 4)
#               "group"                 = refund, 
#               "agent_id"              = random.randomInt(149000, 150000)
#               "requester"             = random.randomInt(149000, 150000)
#               "product"               = mobile,    
#           }
#       }



