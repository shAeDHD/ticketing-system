require 'sqlite3'
require 'pry'
require 'active_record'
require 'json'

ActiveRecord::Base.establish_connection(
    :adapter => 'sqlite3',
    :database => 'database.db'
)
class Metadata < ActiveRecord::Base
    has_one :ticket_header
    has_many :other_activities, through: :ticket_header
    has_one :note_activity, through: :ticket_header
    def create
        # Where multiple activities share the same performer id,
        # create a Metadata.new. That has a start_at 
        # which is set as before the earliest 
        # ticket.performed_at and ends at time.now.
        # the activites_count is activites.length.
        # metadata = Metadata.new
        # metadata.activites_count =
        puts "made to metadata new" 
    end

    def start_time(  )
        # parse string time into date time

        # take random number of hours/days from this date
    end
end
class Ticket_Header < ActiveRecord::Base
    has_many :other_activities
    belongs_to :metadata
    def create
    end
end
class Note_Activity < ActiveRecord::Base
    belongs_to :ticket_header
    # belongs_to :metadata, through: :ticket_header
    def create 
    end
end
class Other_Activity < ActiveRecord::Base
    belongs_to :ticket_header
    # belongs_to :metadata, through: :ticket_header
    def create
    end
end

parent_file = File.expand_path("..", Dir.pwd)
file = File.open(File.expand_path("#{parent_file}/ticket_generator/ticket_data.json"))
ticket_data = JSON.load file
file.close 
puts ActiveRecord::Base.connection.tables

######      MAPS JSON DATA INTO DB TABLES       ######
ticket_data.map do | ticket_iteration |
    
    iteration_th = Ticket_Header.new
    iteration_th.performed_at = ticket_iteration.dig("performed_at"),
    iteration_th.ticket_id = ticket_iteration.dig("ticket_id"),
    iteration_th.performer_type = ticket_iteration.dig("performer_type")
    iteration_th.performer_id = ticket_iteration.dig("performer_id")
    iteration_th.save

    activity = ticket_iteration.fetch("activity")

    if activity.has_key?("note")
        #   Put Note data into database
        note = Note_Activity.new 
        note.id = activity.dig( "note", "id" )
        note.note_type = activity.dig( "note", "type" )
        note.save
        #   For each note, we want to create a Metadata record as 
        #   each chain of tickets can only have one note. To this, 
        #   we will tie the 'performer_id' for easy identification.
        metadatum = Metadata.new
        metadatum.performer_id = ticket_iteration.dig("performer_id")
        # metadatum.start_at = Metadata.start_time
        puts ticket_iteration.fetch("performed_at")
        metadatum.save

    else
        other = Other_Activity.new 
        other.shipping_address = activity.dig( "shipping_address" )
        other.shipment_date = activity.dig( "shipment_date" )
        other.category = activity.dig( "category" )
        other.contacted_customer = activity.dig( "contacted_customer" )
        other.issue_type = activity.dig( "issue_type" )
        other.source = activity.dig( "source" )
        other.status = activity.dig( "status" )
        other.priority = activity.dig( "priority" )
        other.group_id = activity.dig( "group_id" )
        other.agent_id = activity.dig( "agent_id" )
        other.requester = activity.dig( "requester" )
        other.product = activity.dig( "product" )
        other.save
        # if other.status == "Resolved" || other.status == "Closed"

    end #   end else/if
end     #   end JSON data mapping


pry binding
puts "Finished!"