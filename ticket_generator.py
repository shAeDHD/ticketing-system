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
        
    print(performed_at)
    
    # print(performed_at)
    
performed_at(start_date, end_date)
############################################################
   
# DECONSTRUCTING DATA EXAMPLE

#   metadata:
#       "start_at"          = datetime.datetime.now()   # when ticket begins being created by user
#       "end_at"            = datetime.datetime.now()   # when ticket is formally completed by user
#       "activites_count"   = len(activities_data)      # total amount of activites taken 
#                                                       by user in the crea`tion of their ticket

#   activities_data: [
#       {
#           "performed_at"  = 