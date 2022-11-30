import datetime
from datetime import timedelta
import random 

######################## TEST ##############################
start_date  = datetime.datetime.now()
end_date    = start_date + timedelta(days=random.randint(1,3))

print(start_date)
print(end_date)
############################################################
   
# DECONSTRUCTING DATA EXAMPLE

#   metadata:
#       "start_at"          = datetime.datetime.now()   # when ticket begins being created by user
#       "end_at"            = datetime.datetime.now()   # when ticket is formally completed by user
#       "activites_count"   = len(activities_data)      # total amount of activites taken 
#                                                       by user in the creation of their ticket

#   activities_data: [
#       {
#           "performed_at"  = 