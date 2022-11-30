import datetime
from datetime import timedelta
import random 

# random.randint(0,5)

start_date = datetime.datetime.now() 
start_at = start_date - timedelta(days=random.randint(0,5))

print(start_at)

# end_date = start_date + timedelta(days=10)




# random_date = start_date + (end_date - start_date) * random.random()
# print(random_date)


# # First - Generate "metadata" information


# def generate_metadata_dates():
#     start_date = random_date
#     end_date = start_date + timedelta(days=2)
    
#     return { start_date, end_date }

# print( generate_metadata_dates())    
    
    

