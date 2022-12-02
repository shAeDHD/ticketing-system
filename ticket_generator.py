import random_address 
from random_address import real_random_address
import datetime
from datetime import timedelta
import random 

######################## TEST ##############################
start_date  = datetime.datetime.now()
end_date    = start_date + timedelta(days=random.randint(1,3))
 
# def activity_commenced_at( start_date, end_date ): 
    
    # time_between_dates = end_date - start_date
    # print(time_between_dates)     #   check == true
    
    # days_between_dates = time_between_dates.days
    # print(days_between_dates)     #   check == true
    
    # random_number_of_days = random.uniform(0.25, days_between_dates)
    # print(random_number_of_days)  #   check == true
    
    # performed_at = datetime.timedelta(days=random_number_of_days)
    # print(performed_at)           #   check == true
    
    # performed_at = start_date + timedelta(days=random.uniform(0.25 , (end_date - start_date).days +1))
    
    # return performed_at
        
print(start_date)
print(activity_commenced_at(start_date, end_date))
print(end_date)




        




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
#               "issue_type"            = incident, delivery,
#               "source"                = random.randomInt()
#               "status"                = open, close, pending, Resolved, Waiting for Customer, Waiting for Third Party
#               "priority"              = randomInt(1 , 4)
#               "group"                 = refund, replacement, reparation
#               "agent_id"              = random.randomInt(149000, 150000)
#               "requester"             = random.randomInt(149000, 150000)
#               "product"               = mobile,    
#           }
#       }


###########################################
# DETAILS #

# Metadata is time period being queried for, and number of tickets during that period 
# Activities_data, then is a list of all tickets 

tickets = []
    
def generate_tickets( number_of_tickets ): #NOTE: need to use self?
    
    
    performer_type = [ "User", "Admin" ]
    phone = [ "Mobile", "Landline" ]
    laptop = [ "Mac", "Acer", "Lenovo" ]
    pc = [ "Alienware", "Dell", "Custom" ]
    other = [ "Accessories", "Office Utilities" ]
    
    category = [ 'Phone', 'Laptop', 'PC', 'Other' ] 
    issue_type = [ 'Incident', 'Delivery' ]  
    status = [ 'Open', 'Close', 'Pending', 'Resolved' ]
    group = [ 'refund', 'replacement', 'reparation' ]
    
    performer_ids = []
    ticket_ids = [704]
    note_ids = [4025864]
    
    def generate_date( start_date, end_date ): 
    
    # time_between_dates = end_date - start_date
    # print(time_between_dates)     #   check == true
    
    # days_between_dates = time_between_dates.days
    # print(days_between_dates)     #   check == true
    
    # random_number_of_days = random.uniform(0.25, days_between_dates)
    # print(random_number_of_days)  #   check == true
    
    # performed_at = datetime.timedelta(days=random_number_of_days)
    # print(performed_at)           #   check == true
    
        performed_at = start_date + timedelta(days=random.uniform(0.25 , (end_date - start_date).days +1))
    
        return performed_at
    activity_commencement_date = generate_date( start_date, end_date )
   
    def generate_ticket_id():
        new_ticket_id = ticket_ids[-1] + 1
        ticket_ids.append(new_ticket_id)
        return new_ticket_id
    ticket_id_value = generate_ticket_id
    
    def generate_performer_id():
        performer_id = random.randomint(149900,150000)
        return performer_id
    performer_id_value = generate_performer_id()

    def generate_shipment_date( iteration_generated_date ):
        date_before_complaint = iteration_generated_date - timedelta(days=random.randint( 3, 10 ))
        return date_before_complaint
    shipment_date_value = generate_shipment_date( activity_commencement_date )
        
    def generate_note_id():
        new_note_id = note_ids[-1] + 1
        note_ids.append(new_note_id)
        return new_note_id
    
    def generate_boolean():
        boolean_value = False
        if random.randint(0, 1) == 0: boolean_value = True
        return boolean_value         
    contacted_customer_value = generate_boolean()


    def generate_random_activity( shipment_date_value ):
        activities = [ "Delivery Issue", "Refund Request", "Other / Message" ]
        activity_type = activities[random.randint( 0, 2 )]
        
        if activity_type == "Delivery Issue":
            return {
                "shipping_address": real_random_address(),
                "shipment_date": shipment_date_value,
                "category" : "Delivery Issue",
                "contacted_customer" : contacted_customer_value
            }
        

        
            
    iteration = 1
    
    while iteration <= len(number_of_tickets):
        if iteration % 50 == 0: 
            activities_data = {
                "performed_at": activity_commencement_date,
                "ticket_id": ticket_id_value,
                "performer_type" : 'Admin',
                "performer_id" : 149899,
                "activity" : generate_random_activity( activity_commencement_date )
            }
        else:
            activities_data = {
                "performed_at": activity_commencement_date,
                "ticket_id": ticket_id_value,
                "performer_type" : 'User',
                "performer_id" : performer_id_value,
                "activity" : generate_random_activity( activity_commencement_date )
                
            }
